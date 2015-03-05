import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty, StringProperty
from kivy.adapters.listadapter import ListAdapter

__version__ = '0.0.1'

with open('services.json') as f:
    services = json.loads(f.read().decode('utf8'))

text = """
.. _top:

{service_name}

**About the service**

{about}

{offers}

**About the organisation**

{about_org}

{service_availibility}

**Contact**

{telephone}

{email}

Address: {address}

{website}
"""


class ServiceTypeList(BoxLayout):
    def __init__(self, **kwargs):
        self.list_adapter = ListAdapter(
            data=services.keys(),
            args_converter=self.services_converter,
            cls=ServiceTypeListItem
        )
        super(ServiceTypeList, self).__init__(**kwargs)

    def services_converter(self, index, service):
        return dict(name=service)


class ServiceTypeListItem(ListItemButton):
    name = StringProperty()


class ServiceList(BoxLayout):
    list_view = ObjectProperty()

    def __init__(self, service_type, **kwargs):
        super(ServiceList, self).__init__(**kwargs)
        self.list_view.adapter.data.extend(services[service_type].keys())

    def disability_converter(self, index, disability):
        result = dict(name=disability)
        return result


class ServiceListItem(ListItemButton):
    name = StringProperty()


class ServiceInfoPage(BoxLayout):
    def __init__(self, service_type, service_name, **kwargs):
        self.service_name = service_name

        service_info = services[service_type][service_name]
        service_about = service_info['about']
        about_organisation = service_info['about_organisation']

        service_offers = service_info.get('service_offers')
        service_offers_text = ''
        if service_offers:
            for offer in service_offers:
                service_offers_text += ' * {}\n'.format(offer)

        service_availibility = service_info.get('service_availibility')
        if service_availibility:
            service_availibility_text = \
                '**Who can use the service?**\n\n{}'.format(
                    service_availibility)
        else:
            service_availibility_text = ''

        contact = service_info['contact']
        telephone_text = 'Telephone: {}'.format(contact.get('telephone', 'n/a'))
        email_text = 'Email: {}'.format(contact.get('email', 'n/a'))
        address = contact['address']

        address_text = ''
        for addr_info in address.values():
            if addr_info:
                address_text += '{},\n'.format(addr_info)

        address_text = address_text.rstrip(',')  # Remove last ','
        website = 'Website: {}'.format(service_info.get('website', 'n/a'))
        service_name_text = self.service_name + '\n{}'.format('=' * len(self.service_name))

        self.text = text.format(
            service_name=service_name_text,
            about=service_about,
            offers=service_offers_text,
            about_org=about_organisation,
            service_availibility=service_availibility_text,
            telephone=telephone_text,
            email=email_text,
            address=address_text,
            website=website
        )
        super(ServiceInfoPage, self).__init__(**kwargs)


class CareAppRoot(BoxLayout):

    def new_service_info_page(self, service):
        self.service_info_page = ServiceInfoPage(self.service_type, service)
        self.clear_widgets()
        self.add_widget(self.service_info_page)

    def show_services_list(self, service_type):
        self.clear_widgets()
        self.services_list = ServiceList(service_type)
        self.service_type = service_type
        self.add_widget(self.services_list)

    def show_service_types(self):
        self.clear_widgets()
        self.add_widget(ServiceTypeList())


class CareApp(App):
    pass

if __name__ == '__main__':
    CareApp().run()

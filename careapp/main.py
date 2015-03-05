import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty, StringProperty
from kivy.adapters.listadapter import ListAdapter

__version__ = '0.0.1'

with open('services.json') as f:
    services = json.loads(f.read())


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
        service_offers = service_info['service_offers']
        about_organisation = service_info['about_organisation']
        service_availibility = service_info['service_availibility']

        contact = service_info['contact']
        telephone = contact['telephone']
        email = contact['email']
        address = contact['address']
        house_name = address['house_name']
        street_name = address['street_name']
        town = address['town']
        city = address['city']
        postcode = address['postcode']

        full_address = '{}\n{}\n{}\n{}\n{}\n'.format(
            house_name,
            street_name,
            town,
            city,
            postcode
        )
        website = service_info['website']

        offers_rst_text = ''
        for offer in service_offers:
            offers_rst_text += ' * {}\n'.format(offer)
        self.text = """
.. _top:

{service_name}

**About the service**

{about}

{offers}

**About the organisation**

{about_org}

**Who can use the service?**

{service_availibility}

**Contact**

Telephone: {telephone}

Email: {email}

Address:

    {house_name},\n
    {street_name},\n
    {town},\n
    {city},\n
    {postcode}\n

Website: {website}
""".format(
            service_name=self.service_name + '\n' + '=' * len(self.service_name),
            about=service_about,
            offers=offers_rst_text,
            about_org=about_organisation,
            service_availibility=service_availibility,
            telephone=telephone,
            email=email,
            house_name=house_name,
            street_name=street_name,
            town=town,
            city=city,
            postcode=postcode,
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

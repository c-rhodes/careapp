__version__ = '0.0.1'

import kivy
import json

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.listview import ListItemButton, ListView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.utils import get_color_from_hex
from kivy.adapters.listadapter import ListAdapter

with open('services.json') as f:
    services = json.loads(f.read())


class ServiceTypeList(BoxLayout):
    services_list = ObjectProperty()

    def __init__(self, **kwargs):
        super(ServiceTypeList, self).__init__(**kwargs)
        self.list_adapter = ListAdapter(
            data=services.keys(),
            args_converter=self.services_converter,
            cls=ServiceTypeListItem
        )
        self.services_list = ListView(adapter=self.list_adapter)
        anchor = AnchorLayout(anchor_y='top', height='40dp', size_hint_y=None)
        grid = GridLayout(cols=1, row_default_height='40dp', row_force_default=True)
        grid.add_widget(Label(text='Select a service category from the list below for more services.'))
        anchor.add_widget(grid)
        self.add_widget(anchor)
        self.add_widget(self.services_list)

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

    def show_userselect(self):
        self.clear_widgets()
        self.add_widget(UserSelectForm()) 


class ServiceListItem(ListItemButton):
    name = StringProperty()


class ServiceInfoPage(BoxLayout):
    def __init__(self, name, **kwargs):
        self.name = name
        super(ServiceInfoPage, self).__init__(**kwargs)


class CareAppRoot(BoxLayout):

    def new_service_info_page(self, service):
        self.service_info_page = ServiceInfoPage(service)
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

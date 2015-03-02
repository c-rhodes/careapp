__version__ = '0.0.1'

import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.listview import ListItemButton, ListView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.utils import get_color_from_hex
from kivy.adapters.listadapter import ListAdapter

DISABILITIES = ['Disability {}'.format(i)  for i in range(100)]
services = {
    'carer': ['Alzheimer\'s Society', 'Carer\'s Reablement'],
    'caree': ['test', 'test2']
}

class UserSelectForm(FloatLayout):

    def show_services_list(self, user):
        print(user)
        self.clear_widgets()
        self.services_list = ServiceList(user)
        self.add_widget(self.services_list)


class ServiceList(BoxLayout):
    list_view = ObjectProperty()

    def __init__(self, user, **kwargs):
        super(ServiceList, self).__init__(**kwargs)
        self.app = CareApp.get_running_app()
        self.list_view.adapter.data.extend(services[user])

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

class CareApp(App):
    pass    

if __name__ == '__main__':
    CareApp().run()

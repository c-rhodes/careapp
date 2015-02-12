__version__ = '0.0.1'

import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.listview import ListView, ListItemButton
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.label import Label

DISABILITIES = [dict(text='Disability {}'.format(i), is_selected=False)  for i in range(100)]

class UserSelectScreen(Screen):
    pass


class DisabilitiesScreen(Screen):
    list_view = ObjectProperty()

    def __init__(self, **kwargs):
        super(DisabilitiesScreen, self).__init__(**kwargs)
    
        # simple_list_adapter = SimpleListAdapter(
        #     data=["Item #{0}".format(i) for i in range(100)],
        #     cls=Label)
        # self.list_view = ListView(adapter=simple_list_adapter)
    
        # self.list_adapter = ListAdapter(
        #     data=DISABILITIES,
        #     args_converter=self.args_converter,
        #     cls=ListItemButton,
        #     selection_mode='single',
        #     allow_empty_selection=False
        # )
        # self.list_view = ListView(adapter=self.list_adapter)
        # self.add_widget(self.list_view)

    def on_list_view(self, instance, view):
        print('on_list_view')
        if view:
            view.adapter.data = DISABILITIES

    def args_converter(self, row_index, obj):
        return dict(text=obj['text'], size_hint_y=None, height=25)

    def disability_converter(self, index, disability):
        result = dict(name=disability)
        return result


class DisabilityListItem(BoxLayout):
    name = StringProperty()


class CareAppScreenManager(ScreenManager):
    pass


class CareApp(App):
    pass


if __name__ == '__main__':
    CareApp().run()

__version__ = '0.0.1'

import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.utils import get_color_from_hex

DISABILITIES = ['Disability {}'.format(i)  for i in range(100)]


class UserSelectScreen(Screen):
    pass


class DisabilitiesScreen(Screen):
    list_view = ObjectProperty()

    def __init__(self, **kwargs):
        super(DisabilitiesScreen, self).__init__(**kwargs)

    def disability_converter(self, index, disability):
        result = dict(name=disability)
        return result


class DisabilityInfoScreen(Screen):
    pass

class DisabilityListItem(ListItemButton):
    name = StringProperty()


class CareAppScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(CareAppScreenManager, self).__init__(**kwargs)

    def new_disability_info_screen(self, disability):
        if not self.has_screen(disability):
            s = DisabilityInfoScreen(name=disability)
            self.add_widget(s)

        self.current = disability


class CareApp(App):
    pass


if __name__ == '__main__':
    CareApp().run()

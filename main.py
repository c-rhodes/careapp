__version__ = '0.0.1'

import kivy

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.listview import ListView


class DisabilityForm(ListView):
    disabilities = ObjectProperty()

    def __init__(self, user):
        self.user = user
    
    def get_services(self):
        disabilities = ['mental', 'physical', 'diagnosis: raw dogger']
        self.disabilities.item_strings = disabilities


class CareForm(FloatLayout):

    def __init__(self):
        super(CareForm, self).__init__()

    def select_user(self, user):
        self.user = user
        self.clear_widgets()
        self.disability_form = DisabilityForm(self.user)
        self.add_widget(self.disability_form)
        print(user)


class Care(App):

    def __init__(self):
        super(Care, self).__init__()


if __name__ == '__main__':
    Care().run()

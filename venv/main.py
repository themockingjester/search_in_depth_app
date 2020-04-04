import os

from kivy.app import App

from kivy.uix.behaviors import ButtonBehavior

from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


class searchitemclass(Widget):
    output1 = ObjectProperty(None)
    entry1 = ObjectProperty(None)


class MainApp(App):
    def build(self):
        ############################# attaching the main screen #########################
        self.screen_manager = ScreenManager()
        self.connect_page = MainScreen()
        screen1 = Screen(name='mainscreen')
        screen1.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen1)
        ########################### attaching the search item screen #################
        self.info_page = searchitemclass()
        screen = Screen(name='searchitemscreen')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager

    def mainscreen_to_searchitemclass(self):
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'searchitemscreen'

    def searchitemclass_to_mainscreen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'mainscreen'

    def go(self):
        # here i want to print entry1 objectproperty value
        pass


class ImageButton(ButtonBehavior, Image):
    pass


class MainScreen(Widget):
    pass

MainApp().run()

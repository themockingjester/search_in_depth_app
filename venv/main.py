from kivy.app import App
from kivy.uix.codeinput import CodeInput
from kivy.lang import Builder
#:include Newcan.kv

from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import *
from kivy.uix import *
import kivy.factory
import kivy.uix.behaviors
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


class Newcan(Widget):
    pass


class MainApp(App):
    def build(self):
        ############################# attaching the main screen #########################
        self.screen_manager = ScreenManager()
        self.connect_page = MainScreen()
        screen1 = Screen(name='mainscreen')
        screen1.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen1)
        self.info_page = Newcan()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager

    def mainscreen_to_searchitemclass(self):
        print('ghfgjh')
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'Info'

    def searchitemclass_to_mainscreen(self):
        print('ghfgjh')
        self.screen_manager.transition.direction = 'up'
        self.screen_manager.current = 'mainscreen'


class ImageButton(ButtonBehavior, Image):
    pass


class MainScreen(Widget):
    pass


MainApp().run()

import os
import time

from kivy.app import App
import threading
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
        ##############################################################################
        self.status = 0
        return self.screen_manager

    def mainscreen_to_searchitemclass(self):
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'searchitemscreen'

    def searchitemclass_to_mainscreen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'mainscreen'

    def pause(self):
        self.status = 1

    def play(self):
        self.status = 0

    def go(self):
        self.t1 = threading.Thread(target=self.starttraversing)
        self.t1.start()

    def starttraversing(self):
        # here i want to print entry1 objectproperty value
        # self.info_page.entry1.text
        lis3 = list()

        req = self.info_page.entry1.text
        z = '/'
        self.func(z, lis3, req)
        print(('oooooooooookkkkkkkkkk'))

    def func(self, path, lis3, req):
        while (self.status == 1):
            pass
        dirs = list()

        path1, dirs1, files = next(os.walk(path))
        for i in dirs1:
            m = path + "/" + i
            try:
                path1, dirs2, files2 = next(os.walk(m))
                dirs.append(i)
            except:
                continue

        if path not in lis3:
            lis3.append(path)
            # print(path)
        else:
            pass

        if len(dirs) == 0 and len(files) == 0:
            str = path
            str1 = list(str[::-1])
            lis2 = list()
            ctr = 0
            for i in str1:
                if i != '/' and ctr == 0:

                    pass
                elif (ctr == 1):
                    lis2.append(i)
                elif i == '/':

                    ctr += 1


                else:
                    pass
            lis2 = ''.join(lis2)
            lis2 = lis2[::-1]
            path = lis2
            self.func(path, lis3, req)
        else:
            if len(files) != 0:
                for i in files:

                    m = path + "/" + i
                    if m not in lis3:
                        if req in i:
                            lis3.append(m)
                            m += '\n\n\n'
                            self.info_page.output1.text += m
                            print(m)
                    else:

                        continue
            else:
                pass
            if len(dirs) != 0:
                for i in dirs:
                    m = path + "/" + i

                    if m not in lis3:
                        if i == req:
                            lis3.append(m)
                            m += '\n\n\n'

                            print(m)
                            self.info_page.output1.text += m

                        if i != "__pycache__":
                            self.func(m, lis3, req)
                    else:
                        str = m
                        str1 = list(str[::-1])
                        lis2 = list()
                        ctr = 0
                        for j in str1:
                            if j != '/' and ctr == 0:

                                pass
                            elif (ctr == 1):
                                lis2.append(j)
                            elif j == '/':

                                ctr += 1


                            else:
                                pass
                        lis2 = ''.join(lis2)
                        lis2 = lis2[::-1]
                        path = lis2
                        continue


class ImageButton(ButtonBehavior, Image):
    pass


class MainScreen(Widget):
    pass


MainApp().run()

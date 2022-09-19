from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.app import MDApp


class FirstScreen(Screen):
    def go_prev_screen(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

    def go_next_screen(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'


class SecondScreen(Screen):
    big_img = ObjectProperty()

    def update_big_img(self, path, *args):
        self.big_img.source = path

    def go_prev_screen(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

    def go_next_screen(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'


class MainApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm


MainApp().run()
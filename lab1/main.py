from kivymd.app import MDApp
from kivy.factory import Factory
from ScreenMaster import ScreenMaster
from content import Content
from first_screen import FirstScreen
from second_screen import SecondScreen


Factory.register('SecondScreen', cls=SecondScreen)
Factory.register('FirstScreen', cls=FirstScreen)
Factory.register('ScreenMaster', cls=ScreenMaster)
Factory.register('Content', cls=Content)


class MainApp(MDApp):
    def build(self):
        return Factory.Content()


MainApp().run()


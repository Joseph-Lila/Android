import Tasks
from kivy.factory import Factory
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        return Factory.ScreenMaster()


MainApp().run()

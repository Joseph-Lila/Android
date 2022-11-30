from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp

Builder.load_file("Tasks/screen_master.kv")


class ScreenMaster(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Light",
                "height": dp(56),
                "on_release": lambda x="Light": self.menu_callback(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": f"Dark",
                "height": dp(56),
                "on_release": lambda x="Dark": self.menu_callback(x),
            }
        ]
        self.menu = MDDropdownMenu(
            items=self.menu_items,
            width_mult=4,
        )

    def callback(self, button, touch):
        self.menu.caller = button
        if touch.button == 'right':
            self.menu.open()

    def make_dark(self):
        MDApp.get_running_app().theme_cls.theme_style = "Dark"
        MDApp.get_running_app().theme_cls.primary_palette = "Orange"

    def make_light(self):
        MDApp.get_running_app().theme_cls.theme_style = "Light"
        MDApp.get_running_app().theme_cls.primary_palette = "Red"

    def menu_callback(self, text_item):
        if text_item == 'Dark':
            self.make_dark()
        elif text_item == 'Light':
            self.make_light()
        self.menu.dismiss()

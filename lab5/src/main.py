from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from core.gui.view.screens import SCREENS, ScreensGenerator


class MyMVPApp(MDApp):
    title = "LLK Railway Station"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.material_style = "M3"

        return ScreensGenerator().generate_resulted_view()


if __name__ == '__main__':
    MyMVPApp().run()

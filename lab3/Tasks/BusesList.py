from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem


Builder.load_file("Tasks/buses_list.kv")


class BusesList(Screen):
    container = ObjectProperty()

    def go_back(self, *args):
        self.manager.current = 'third'

    def on_enter(self, *args):
        self.container.clear_widgets()
        for i, elem in enumerate(self.manager.ids['activity_3'].buses.get_collection(), start=1):
            self.container.add_widget(OneLineListItem(text=f'{i}. {elem.bus_number} ({elem.brand})'))

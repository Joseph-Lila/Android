from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem


Builder.load_file("Tasks/task_3_tip_b.kv")


class Task3TipB(Screen):
    container = ObjectProperty()

    def go_back(self, *args):
        self.manager.current = 'third'

    def on_enter(self, *args):
        self.container.clear_widgets()
        cnt = 1
        for i, elem in enumerate(self.manager.ids['activity_3'].buses.get_collection(), start=1):
            if 2022 - elem.creation_year > 10:
                self.container.add_widget(OneLineListItem(text=f'{cnt}. {elem.bus_number} ({elem.brand})'))
                cnt += 1


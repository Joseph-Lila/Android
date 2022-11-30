from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem


Builder.load_file("Tasks/task_3_tip_c.kv")


class Task3TipC(Screen):
    container = ObjectProperty()

    def go_back(self, *args):
        self.manager.current = 'third'

    def on_enter(self, *args):
        cnt = 1
        self.container.clear_widgets()
        for i, elem in enumerate(self.manager.ids['activity_3'].buses.get_collection(), start=1):
            if elem.vehicle > 100000:
                self.container.add_widget(OneLineListItem(text=f'{cnt}. {elem.bus_number} ({elem.brand})'))
                cnt += 1



from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem


Builder.load_file("Tasks/task_3_tip_a.kv")


class Task3TipA(Screen):
    container = ObjectProperty()
    route_number = ObjectProperty()

    def go_back(self, *args):
        self.manager.current = 'third'

    def search_buses(self, *args):
        self.container.clear_widgets()
        cnt = 1
        for i, elem in enumerate(self.manager.ids['activity_3'].buses.get_collection(), start=1):
            if str(elem.route_number) == self.route_number.text:
                self.container.add_widget(OneLineListItem(text=f'{cnt}. {elem.bus_number} ({elem.brand})'))
                cnt += 1

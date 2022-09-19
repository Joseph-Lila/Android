from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog

from Controllers.Models.Bus import Bus

Builder.load_file("Tasks/add_bus.kv")


class AddBus(Screen):
    fio = ObjectProperty()
    bus_number = ObjectProperty()
    route_number = ObjectProperty()
    brand = ObjectProperty()
    creation_year = ObjectProperty()
    vehicle = ObjectProperty()

    def go_back(self, *args):
        self.manager.current = 'third'

    def on_enter(self, *args):
        self.__clear_text_fields()

    def __clear_text_fields(self):
        self.fio.text = ''
        self.bus_number.text = ''
        self.route_number.text = ''
        self.brand.text = ''
        self.creation_year.text = ''
        self.vehicle.text = ''

    def add_bus(self, *args):
        fio = self.fio.text
        bus_number = self.bus_number.text
        try:
            route_number = float(self.route_number.text)
        except:
            route_number = 1
        brand = self.brand.text
        try:
            creation_year = int(self.creation_year.text)
        except:
            creation_year = 2001
        try:
            vehicle = float(self.vehicle.text)
        except:
            vehicle = 0
        self.manager.ids['activity_3'].buses.get_collection().append(
            Bus(fio, bus_number, route_number, brand, creation_year, vehicle)
        )
        self.__clear_text_fields()
        MDDialog(
            text="New bus was added!",
            radius=[20, 7, 20, 7],
        ).open()


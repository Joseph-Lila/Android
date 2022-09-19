from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.factory import Factory

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem

from Train import Train


class MainBody(MDBoxLayout):
    def show_activities(self, *args):
        self.first_check.disabled = False
        self.second_check.disabled = False

    def go_to_first_railway_station(self, *args):
        self.master.current = "first_railway_station"

    def go_to_second_railway_station(self, *args):
        self.master.current = "second_railway_station"


class ScreenMaster(ScreenManager):
    pass


class FirstScreen(Screen):
    def on_kv_post(self, base_widget):
        self.train_collection = [
                Train('Train 1', 'Гомель', 'Минск'),
                Train('Train 2', 'Москва', 'Минск'),
                Train('Train 3', 'Москва', 'Гоа'),
                Train('Train 4', 'Гоа', 'Варанаси'),
                Train('Train 5', 'Варанаси', 'Минск'),
            ]
        for train in self.train_collection:
            new_btn = Button(text=f"{train.title}\n<From>: {train.departure}\n<To>: {train.destination}")
            new_btn.bind(on_press=self.send_data)
            self.cont.add_widget(new_btn)

    def send_data(self, instance):
        text = instance.text
        self.manager.main_body.text_field.text += text + "\n"
        self.manager.current = 'main_activity'


class SecondScreen(Screen):
    def on_kv_post(self, base_widget):
        self.train_collection = [
            Train('Train 6', 'Гомель', 'Минск'),
            Train('Train 7', 'Москва', 'Минск'),
            Train('Train 8', 'Москва', 'Гоа'),
            Train('Train 9', 'Гоа', 'Варанаси'),
            Train('Train 10', 'Варанаси', 'Минск'),
        ]
        unique_destinations = set([train.destination for train in self.train_collection])
        self.spinner.values = tuple(unique_destinations)
        self.spinner.text = "All"
        for train in self.train_collection:
            new_list_item = OneLineListItem(text=f"{train.title} <From>: {train.departure} <To>: {train.destination}")
            new_list_item.bind(on_press=self.send_data)
            self.lst.add_widget(new_list_item)

    def send_data(self, instance):
        text = instance.text
        self.manager.main_body.text_field.text += text + "\n"
        self.manager.current = 'main_activity'

    def get_actual_items(self, *args):
        needed_destination = self.spinner.text
        self.lst.clear_widgets()
        for train in self.train_collection:
            if train.destination == needed_destination:
                new_list_item = OneLineListItem(text=f"{train.title} <From>: {train.departure} <To>: {train.destination}")
                new_list_item.bind(on_press=self.send_data)
                self.lst.add_widget(new_list_item)


Factory.register(classname="FirstScreen", cls=FirstScreen)
Factory.register(classname="SecondScreen", cls=SecondScreen)
Factory.register(classname="MainBody", cls=MainBody)
Factory.register(classname="ScreenMaster", cls=ScreenMaster)


class MainApp(MDApp):
    def build(self):
        return Factory.ScreenMaster()


MainApp().run()

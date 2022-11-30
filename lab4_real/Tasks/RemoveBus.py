from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from functools import partial


Builder.load_file("Tasks/remove_bus.kv")


class RemoveBus(Screen):
    container = ObjectProperty()

    def go_back(self, *args):
        self.manager.current = 'third'

    def on_enter(self, *args):
        self.__update_list()

    def __update_list(self, *args):
        self.container.clear_widgets()
        for i, elem in enumerate(self.manager.ids['activity_3'].buses.get_collection(), start=1):
            self.container.add_widget(OneLineListItem(text=f'{i}. {elem.bus_number} ({elem.brand})',
                                                      on_press=partial(self.remove_item, i - 1)))

    def remove_item(self, index, *args):
        self.dialog = MDDialog(
            text="Remove bus?",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_press=self.close_dialog,
                ),
                MDFlatButton(
                    text="REMOVE",
                    on_press=partial(self.remove_by_index, index)
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss(force=True)

    def remove_by_index(self, index, *args):
        item_to_remove = self.manager.ids['activity_3'].buses.get_collection()[index]
        self.manager.ids['activity_3'].buses.get_collection().remove(item_to_remove)
        self.__update_list()
        self.close_dialog()

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget

Builder.load_file("Tasks/second_task.kv")


class IconItem(OneLineIconListItem):
    def __init__(self, msg, manager, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(IconLeftWidget(icon='star'))
        self.msg = msg
        self.manager = manager

    def on_press(self):
        num = int(self.text.split(' ')[-1])
        self.manager.ids[f'activity_{num}'].ids['my_data'].text = "Data: " + self.msg


class SecondTask(Screen):
    def go_next_screen(self, *args):
        self.manager.current = 'third'

    def go_prev_screen(self, *args):
        self.manager.current = 'first'

    def send_data(self, text, *args):
        MDDialog(
            title='Choose activity to send data',
            type='simple',
            items=[
                IconItem(text="Task 1 -- Activity 1", msg=text, manager=self.manager),
                IconItem(text="Task 3 -- Activity 3", msg=text, manager=self.manager),
            ]
        ).open()

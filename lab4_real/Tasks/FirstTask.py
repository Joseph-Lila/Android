from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


Builder.load_file("Tasks/first_task.kv")


class FirstTask(Screen):
    train_list = ObjectProperty()
    ans_field = ObjectProperty()

    def go_next_screen(self, *args):
        self.manager.current = 'second'

    def go_prev_screen(self, *args):
        self.manager.current = 'third'

    def get_info(self, *args):
        self.ans_field.text = ''
        for res in self.train_list.train_collection.dictionary[self.train_list.text]:
            self.ans_field.text += res + '\n'
        self.ans_field.text += '\n\nИменно эти поезда проезжают через ' + self.train_list.text

import random
import threading
import time

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from Controllers.Models.Bus import Bus
from Controllers.Models.BusCollection import BusCollection
from Controllers.Models.DataLoader import DataLoader
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressbar import MDProgressBar

Builder.load_file("Tasks/third_task.kv")


class ThirdTask(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.buses = None

    def on_kv_post(self, *args):
        self.progressbar = MDProgressBar(value=0)
        self.dialog = MDDialog(
            title="Please, wait...",
            type='custom',
            content_cls=self.progressbar
        )
        self.dialog.open()
        my_thread = threading.Thread(target=self.process_progress_bar)
        my_thread.start()
        self.buses = BusCollection(
            DataLoader.load()
        )

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)

    def process_progress_bar(self):
        for i in range(10):
            self.progressbar.value += random.randint(10, 30)
            if self.progressbar.value >= 100:
                self.dialog_close()
                break
            time.sleep(1)

    def go_next_screen(self, *args):
        self.manager.current = 'first'

    def go_prev_screen(self, *args):
        self.manager.current = 'second'

    def save_data(self, *args):
        data = self.buses.get_collection()
        data = [elem.as_dict() for elem in data]
        DataLoader.save(data)

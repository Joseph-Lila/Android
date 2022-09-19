from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from Controllers.Models.Bus import Bus
from Controllers.Models.BusCollection import BusCollection

Builder.load_file("Tasks/third_task.kv")


class ThirdTask(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.buses = BusCollection(
            [
                Bus("FIO 1", "BUS11101", 1, "Brand 1", 2020, 10000),
                Bus("FIO 2", "BUS11102", 2, "Brand 2", 2002, 1000000),
                Bus("FIO 3", "BUS11103", 3, "Brand 3", 2022, 10),
                Bus("FIO 4", "BUS11104", 1, "Brand 4", 2019, 150000),
                Bus("FIO 5", "BUS11105", 2, "Brand 1", 2018, 200000),
                Bus("FIO 6", "BUS11106", 3, "Brand 2", 2020, 9000),
                Bus("FIO 7", "BUS11107", 1, "Brand 3", 2001, 5000),
            ]
        )

    def go_next_screen(self, *args):
        self.manager.current = 'first'

    def go_prev_screen(self, *args):
        self.manager.current = 'second'

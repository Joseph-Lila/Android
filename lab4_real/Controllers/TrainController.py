from kivy.uix.spinner import Spinner
from Controllers.Models.Train import Train
from Controllers.Models.TrainCollection import TrainCollection


class TrainWidget(Spinner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.train_collection = TrainCollection(
            [
                Train('Train 1', 'Гомель', 'Минск'),
                Train('Train 2', 'Москва', 'Минск'),
                Train('Train 3', 'Москва', 'Гоа'),
                Train('Train 4', 'Гоа', 'Варанаси'),
                Train('Train 5', 'Варанаси', 'Минск'),
            ]
        )
        self.values = self.train_collection.dictionary.keys()
        self.text = self.values[0] if len(self.values) > 0 else 'Empty'

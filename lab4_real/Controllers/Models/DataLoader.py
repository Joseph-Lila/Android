import json
from Controllers.Models.Bus import Bus


class DataLoader:
    DATA_SOURCE_PATH = "/home/loki/PycharmProjects/Android/lab4_real/data.json"

    @staticmethod
    def load():
        with open(DataLoader.DATA_SOURCE_PATH, "r") as f:
            data = json.load(f)
            data = data['elements']
            data = [Bus(**elem) for elem in data]
            return data

    @staticmethod
    def save(data):
        data = {
            "elements": data
        }
        with open(DataLoader.DATA_SOURCE_PATH, "w") as f:
            json.dump(data, f, indent=4)

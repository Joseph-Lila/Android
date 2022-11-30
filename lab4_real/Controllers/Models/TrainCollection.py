from Controllers.Models.Train import Train


class TrainCollection:
    def __init__(self, collection: list):
        self.dictionary = dict()
        self.collection = collection
        self.dictionary = self.__split_by_departures_or_destinations()

    def __split_by_departures_or_destinations(self):
        dictionary = dict()
        for elem in self.collection:
            if elem.departure not in dictionary.keys():
                dictionary[elem.departure] = [elem.title]
            else:
                if elem.title not in dictionary[elem.departure]:
                    dictionary[elem.departure].append(elem.title)
            if elem.destination not in dictionary.keys():
                dictionary[elem.destination] = [elem.title]
            else:
                if elem.title not in dictionary[elem.destination]:
                    dictionary[elem.destination].append(elem.title)
        return dictionary

from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


class Bank:
    currencies = ['RUB', 'USD', 'BYN', 'EUR']
    # (from, to): value
    koefs = {
        ('BYN', 'RUB'): 23.3,
        ('BYN', 'USD'): .387,
        ('BYN', 'EUR'): .3801,
        ('EUR', 'BYN'): 2.6308,
        ('USD', 'BYN'): 2.5843,
        ('RUB', 'BYN'): .0429,
    }


class MainWidget(Screen):
    amount = ObjectProperty()
    ans = ObjectProperty()
    currency = ObjectProperty()
    koef = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.mode = 'покупка'
        self.chosen_currency = 'RUB'
        self.koef.text = str(Bank.koefs['BYN', self.chosen_currency])

    def change_mode(self, mode, *args):
        self.mode = mode
        if self.mode == 'покупка':
            self.koef.text = str(Bank.koefs['BYN', self.chosen_currency])
        else:
            self.koef.text = str(Bank.koefs[self.chosen_currency, 'BYN'])

    def change_currency(self, *args):
        self.chosen_currency = self.currency.text
        if self.mode == 'покупка':
            self.koef.text = str(Bank.koefs['BYN', self.chosen_currency])
        else:
            self.koef.text = str(Bank.koefs[self.chosen_currency, 'BYN'])

    def calculate(self, *args):
        if isfloat(self.amount.text):
            if self.mode == 'покупка':
                self.ans.text = str(float(self.amount.text) * Bank.koefs[('BYN', self.chosen_currency)])
            else:
                self.ans.text = str(float(self.amount.text) * Bank.koefs[(self.chosen_currency, 'BYN')])
        else:
            self.ans.text = 'Введите сумму!!!'


class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWidget(name='main'))
        return sm


MainApp().run()

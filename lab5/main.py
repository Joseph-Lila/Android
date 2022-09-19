from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.utils.fitimage import FitImage


class MyListItem(GridLayout):
    def __init__(self, source : str, title : str, population: int, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.padding = 30
        self.spacing = 20
        self.add_widget(FitImage(source=source))
        additional_grid = GridLayout(rows=2)
        additional_grid.add_widget(MDLabel(text=title))
        additional_grid.add_widget(MDLabel(text=f'Популяция: {population}'))
        self.add_widget(additional_grid)


class Body(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = [
            ('images/but.png', 'Голубянка', 200000),
            ('images/but1.png', 'Пестокрыльница', 345000),
            ('images/but3.png', 'Павлиний глаз', 345620),
            ('images/but4.png', 'Монарх', 2341567),
            ('images/but5.png', 'Адмирал', 8765400),
        ]
        for elem in data:
            self.ids.container.add_widget(MyListItem(elem[0], elem[1], elem[2]))


class MainApp(MDApp):
    def build(self):
        return Body()


MainApp().run()
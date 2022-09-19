from kivy.uix.boxlayout import BoxLayout


class Content(BoxLayout):
    def change_text(self, *args):
        self.ids['label'].text = "Прокопенко А.Р. <-> ИП-42"

    def go_next_screen(self, *args):
        print("next")
        self.screen_master.current = 'second'

    def go_prev_screen(self, *args):
        self.screen_master.current = 'first'
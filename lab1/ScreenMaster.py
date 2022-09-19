from kivy.uix.screenmanager import ScreenManager, SwapTransition


class ScreenMaster(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SwapTransition()
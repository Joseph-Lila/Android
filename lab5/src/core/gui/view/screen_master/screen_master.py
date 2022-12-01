""" Module core.gui.view.screen_master """


from pathlib import Path

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

from core.service_layer.observer import Observer


class ScreenMasterView(ScreenManager, Observer):
    """ A class that implements the visual presentation `ScreenMaster` """

    presenter = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)  # register the view as an observer

    def model_is_changed(self):
        """ The method is called when the model changes. """

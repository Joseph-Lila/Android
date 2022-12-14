""" Module core.gui.view.main_container """

from pathlib import Path

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.card import MDCard

from core.service_layer.observer import Observer


class MainContainerView(MDCard, Observer):
    """ A class that implements the visual presentation `MainContainerModel` """

    presenter = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)  # register the view as an observer

    def model_is_changed(self):
        """ The method is called when the model changes. """

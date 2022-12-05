from kivymd.uix.screen import MDScreen
from core.service_layer.observer import Observer
from kivy.properties import ObjectProperty
from kivy_garden.mapview import MapView, MapMarker


class MapScreenView(MDScreen, Observer):
    """ A class that implements the visual representation `MapScreenModel` """

    presenter = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        mapview = MapView(zoom=13, lat=52.405806, lon=30.938826)
        m1 = MapMarker(lat=52.405806, lon=30.938826)
        m2 = MapMarker(lat=52.433972643600406, lon=30.99330579640694)
        mapview.add_marker(m1)
        mapview.add_marker(m2)
        self.add_widget(mapview)

    def model_is_changed(self):
        """ The method is called when the model changes. """

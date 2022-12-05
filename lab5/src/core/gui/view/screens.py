from core.gui.model.main_container import MainContainerModel
from core.gui.model.screen_master import ScreenMasterModel
from core.gui.model.map_screen import MapScreenModel
from core.gui.presenter.main_container import MainContainerPresenter
from core.gui.presenter.screen_master import ScreenMasterPresenter
from core.gui.presenter.map_screen import MapScreenPresenter

SCREENS = {
    # name screen
    "screen master": {
        "model": ScreenMasterModel,
        "presenter": ScreenMasterPresenter
    },
    "main container": {
        "model": MainContainerModel,
        "presenter": MainContainerPresenter
    },
    "map screen": {
        "model": MapScreenModel,
        "presenter":  MapScreenPresenter
    }
}


class ScreensGenerator:
    """
    Creating and adding screens to the screen manager.
    You should not change this cycle unnecessarily. He is self-sufficient.
    """
    def __init__(self, screens=SCREENS):
        self.screens = screens

    def generate_resulted_view(self):
        screen_master_view = self._generate_screen_master(['map screen'])
        main_container_view = self._generate_view('main container')
        main_container_view.add_widget(screen_master_view)
        return main_container_view

    def _generate_view(self, key):
        model = self.screens[key]['model']()
        presenter = self.screens[key]['presenter'](model)
        view = presenter.get_screen()
        view.name = key
        return view

    def _generate_screen_master(self, screens_keys: list):
        screen_master_view = self._generate_view('screen master')
        for screen_key in screens_keys:
            screen_master_view.add_widget(self._generate_view(screen_key))
        return screen_master_view

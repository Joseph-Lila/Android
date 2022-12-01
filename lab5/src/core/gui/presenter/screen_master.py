from core.gui.view.screen_master.screen_master import ScreenMasterView


class ScreenMasterPresenter:
    """ The `ScreenMasterPresenter` class represents a presenter implementation. """

    def __init__(self, model):
        self.model = model
        self.view = ScreenMasterView(presenter=self, model=self.model)

    def get_screen(self):
        """ The method creates get the view. """

        return self.view

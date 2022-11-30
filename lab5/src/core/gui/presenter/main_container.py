from core.gui.view.main_container.main_container import MainContainerView


class MainContainerPresenter:
    """
    The `MainContainerPresenter` class represents a presenter implementation.
    Coordinates work of the view with the model.

    The presenter implements the strategy pattern. The presenter connects to
    the view to control its actions.
    """

    def __init__(self, model):
        """
        The constructor takes a reference to the model.
        The constructor creates the view.
        """

        self.model = model
        self.view = MainContainerView(presenter=self, model=self.model)

    def get_screen(self):
        """ The method creates get the view. """

        return self.view


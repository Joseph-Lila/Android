from kivymd.app import MDApp
from core.gui.model.main_container import MainContainerModel
from core.gui.presenter.main_container import MainContainerPresenter
from core.service_layer.unit_of_work.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork


class MyMVPApp(MDApp):
    title = "LLK Railway Station"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = MainContainerModel(SqlAlchemyUnitOfWork())
        self.presenter = MainContainerPresenter(self.model)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "700"

        return self.presenter.get_screen()


if __name__ == '__main__':
    MyMVPApp().run()

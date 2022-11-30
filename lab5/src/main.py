from core.service_layer.unit_of_work.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork
from core.domain.bus import Bus
from core.domain.train import Train
from core.adapters import orm
from sqlalchemy import create_engine

orm.start_mappers()
uow = SqlAlchemyUnitOfWork()

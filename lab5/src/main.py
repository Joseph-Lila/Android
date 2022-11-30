from core.service_layer.unit_of_work.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork
from core.domain.bus import Bus
from core.adapters import orm


orm.start_mappers()
uow = SqlAlchemyUnitOfWork()
with uow:
    uow.buses.add(Bus(fio='Driver\'s FIO', bus_number="LAWYERUP", route_number=1,
                      brand="LLK", creation_year=2010, vehicle=2.3))
    buses = uow.buses.list()
    for item in buses:
        print(item)

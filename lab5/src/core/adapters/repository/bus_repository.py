""" Module core.adapters.repository.bus_repository """
from typing import List, Optional

from core.adapters.repository.abstract_repository import AbstractRepository
from core.domain.bus import Bus


class BusRepository(AbstractRepository):
    """ Repository for bus items. """
    def __init__(self, session):
        self.session = session

    def add(self, item: Bus) -> None:
        self.session.add(item)

    def get_by_id(self, item_id: int) -> Optional[Bus]:
        return self.session.query(Bus).filter_by(item_id == item_id).one()

    def list(self) -> List[Bus]:
        return self.session.query(Bus).all()

    def update(self, item: Bus) -> None:
        self.session.query(Bus).filter_by(item_id == item.item_id).update(
            fio=item.fio, bus_number=item.bus_number, route_number=item.route_number,
            brand=item.brand, creation_year=item.creation_year, vehicle=item.vehicle)

    def delete(self, item: Bus) -> None:
        self.session.query(Bus).filter_by(item_id == item.item_id).delete()

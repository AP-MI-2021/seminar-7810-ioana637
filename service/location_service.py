from domain.Locatie import Locatie
from domain.LocationValidator import LocationValidator
from repository.comanda_repository import OrderRepository
from repository.locatie_repository import LocatieRepository


class LocationService:
    '''
    '''

    def __init__(self, location_repo: LocatieRepository, location_validator: LocationValidator, order_repo: OrderRepository):
        '''
        '''
        self.__repository = location_repo
        self.__validator = location_validator
        self.__order_repository = order_repo

    def add_location(self, id, strada, numar, bloc, scara, indicatii):
        '''

        '''
        location = Locatie(id,strada, numar, bloc, scara, indicatii)
        self.__validator.validate(location)
        self.__repository.create(location)

    def delete_location(self, id):
        pass

    def get_all(self) -> [Locatie]:
        return self.__repository.read()


    def sort_streets(self):
        streets = self.get_all()
        return sorted(streets, key=lambda x: len(x.indicatii), reverse=True)

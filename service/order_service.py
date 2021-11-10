from domain.Car import Car
from domain.Comanda import Comanda


class OrderService:
    '''
    '''

    def __init__(self, order_repo, order_validator, car_repo, location_repo):
        '''
        '''
        self.__repository = order_repo
        self.__validator = order_validator
        self.__car_repo = car_repo
        self.__location_repo = location_repo

    def add_order(self, id, car_id, locatie_id, time, cost_km, distance, status):
        '''

        '''
        if self.__car_repo.read(car_id) == None:
            raise ValueError('Car not found')
        if self.__location_repo.read(locatie_id) == None:
            raise ValueError('Location not found')

        order = Comanda(id, car_id, locatie_id, time, cost_km, distance, status)
        self.__validator.validate(order)
        self.__repository.create(order)


    def delete_order(self, id):
        pass

    def get_all(self):
        return self.__repository.read()


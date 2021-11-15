from domain.Car import Car
from domain.CarDTO import CarDTO
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

    def sort_cars(self):
        orders = self.get_all()
        cars = {}
        for order in orders:
            car_id = order.car_id
            car = self.__car_repo.read(car_id)
            cost_mediu = order.cost_km
            if (car_id in cars):
                cars[car_id].suma_cost = cars[car_id].suma_cost + cost_mediu
                cars[car_id].nr_cost+=1
            else:
                carDTO = CarDTO(car.id, car.indicativ, car.confort, car.plata_card, car.model, order.cost_km, 1)
                cars[car_id] = carDTO
        return sorted(cars.values(), key = lambda car: car.suma_cost / car.nr_cost)

    def search_full_text(self, search_text):
        cars = self.__car_repo.read()
        orders = self.get_all()
        result = []
        for car in cars:
            if (car.search_text(search_text)):
                result.append(car)
        for order in orders:
            if (order.search_text(search_text)):
                result.append(order)

        for el in result:
            if (isinstance(el,Car)):
                print('este masina')
            if (isinstance(el,Comanda)):
                print('este comanda')





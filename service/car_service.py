from domain.Car import Car


class CarService:
    """

    """

    def __init__(self, car_repo, car_validator, order_repo):
        """

        :param car_repo:
        :param car_validator:
        :param order_repo:
        """
        self.__repository = car_repo
        self.__validator = car_validator
        self.__order_repository = order_repo

    def add_car(self, id, indicativ, confort, plata_card, model):
        """

        :param id:
        :param indicativ:
        :param confort:
        :param plata_card:
        :param model:
        :return:
        """
        car = Car(id, indicativ, confort, plata_card, model)
        self.__validator.validate(car)
        self.__repository.create(car)

    def delete_car(self, id):
        if len(self.__order_repository.findByCarId(id)) > 0:
            raise ValueError('Masina nu poate fi stearsa')
        self.__repository.delete(id)

    def get_all(self):
        return self.__repository.read()
from domain.Locatie import Locatie


class LocationService:
    '''
    '''

    def __init__(self, location_repo, location_validator, order_repo):
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

    def get_all(self):
        return self.__repository.read()





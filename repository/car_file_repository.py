import pickle

class CarFileRepository:
    '''
    Repository for storing data in memory
    '''

    def __init__(self, filename):
        '''
        Creates an in memory repository.
        '''
        self.__storage = {}
        self.__filename = filename or 'cars.pkl'

    # metode CRUD
    # CRUD = Create
    #        Read
    #        Update
    #        Delete


    def __load_from_file(self):
        try:
            with open(self.__filename, 'rb') as f_read:
                self.__storage = pickle.load(f_read)
        except FileNotFoundError:
            self.__storage.clear()
        except Exception:
            self.__storage.clear()

    def __save_to_file(self):
        with open(self.__filename, 'wb') as f_write:
            pickle.dump(self.__storage, f_write)

    def create(self, car):
        '''
        Adds a new car.
        :param car: the given car
        :return: -
        :raises: KeyError if the id already exists
        '''
        self.__load_from_file()
        car_id = car.id
        if car_id in self.__storage:
            raise KeyError('The car id already exists!')
        self.__storage[car_id] = car
        self.__save_to_file()

    def read(self, car_id=None):
        '''
        Gets a car by id or all the cars
        :param car_id: optional, the car id
        :return: the list of cars or the car with the given id
        '''
        self.__load_from_file()
        if car_id is None:
            return self.__storage.values()

        if car_id in self.__storage:
            return self.__storage[car_id]
        return None

    def update(self, car):
        '''
        Updates car.
        :param car: the car to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        self.__load_from_file()
        car_id = car.id
        if car_id not in self.__storage:
            raise KeyError('There is no car with that id!')
        self.__storage[car_id] = car
        self.__save_to_file()

    def delete(self, car_id):
        '''
        Deletes a car.
        :param car_id: the car id to delete.
        :return: -
        :raises KeyError: if no car with car_id
        '''
        self.__load_from_file()
        if car_id not in self.__storage:
            raise KeyError('There is no car with that id!')
        del self.__storage[car_id]
        self.__save_to_file()

    def clear(self):
        self.__storage.clear()
        self.__save_to_file()

class UserInterface:
    def __init__(self, car_service, location_service, order_service):
        self.__car_service = car_service
        self.__location_service = location_service
        self.__order_service = order_service

    def __print_menu(self):
        print("""
        1. Masini
        2. Locatii
        3. Comenzi
        """)

    def __print_menu_car(self):
        print("""
        1. Adaugare masina
        2. Editare
        3. Stergere 
        a. afisare
        b. Back
        """)

    def __print_menu_order(self):
        print("""
        1. Adaugare comanda
        2. Editare
        3. Stergere 
        a. afisare
        b. Back
        """)

    def __print_menu_location(self):
        print("""
        1. Adaugare locatie
        2. Editare
        3. Stergere 
        a. afisare
        b. Back
        """)

    def __show_cars(self):
        while True:
            self.__print_menu_car()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_masini_add()
            elif op == '2':
                self.__handle_masini_remove()
            elif op == 'a':
                self.__show_list(self.__car_service.get_all())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __handle_masini_remove(self):
        try:
            id_car = int(input('Dati id-ul de sters: '))
            self.__car_service.remove_car(id_car)
        except Exception as ex:
            print(ex)

    def __handle_masini_add(self):
        try:
            id_car = int(input('ID-ul: '))
            indicator = int(input('Indicativul: '))
            comfort_level = input('Nivelul de comfort (standard, high, premium): ')
            card_payment = input('Plata cu cardul (da sau nu): ')
            model = input('Modelul: ')
            self.__car_service.add_car(
                id_car,
                indicator,
                comfort_level,
                card_payment,
                model
            )
            print('Masina a fost adaugata!')
        except Exception as ex:
            print('Eroare:', ex)

    def __show_list(self, objects):
        for object in objects:
            print(object)

    def runUI(self):
        while (True):
            self.__print_menu()
            op = input('Optiune: ')
            if op == '1':
                self.__show_cars()
            elif op == '2':
                self.__show_locations()
            elif op == '3':
                self.__show_orders()
            elif op == 'x':
                break
            else:
                print('Comanda invalida!')

    def __show_locations(self):
        while True:
            self.__print_menu_location()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_location_add()
            elif op == 'a':
                self.__show_list(self.__location_service.get_all())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __show_orders(self):
        while True:
            self.__print_menu_order()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_order_add()
            elif op == 'a':
                self.__show_list(self.__order_service.get_all())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __handle_location_add(self):
        try:
            id_location = input('ID-ul: ')
            street_name= input('Numele strazii: ')
            number = input('Numarul strazii: ')
            block = input('Scara: ')
            building = input('Cladirea: ')
            notes = input('Observatii: ')
            self.__location_service.add_location(
                id_location,
                street_name,
                number,
                block,
                building,
                notes
            )
            print('Locatia a fost adaugata!')
        except Exception as err:
            print('Eroare:', err)

    def __handle_order_add(self):
        try:
            id_order = input('ID-ul comenzii: ')
            id_car = input('ID-ul masinii: ')
            id_location = input('ID-ul locatiei: ')
            final_time = input('Timpul final: ')
            km_cost = input('Costul per km: ')
            distance = input('Distanta parcursa: ')
            status = input('Starea comenzii: ')
            self.__order_service.add_order(
                id_order,
                id_car,
                id_location,
                final_time,
                km_cost,
                distance,
                status
            )
            print('Comanda a fost adaugata!')
        except Exception as err:
            print('Erori:', err)




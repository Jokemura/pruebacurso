from codecs import ascii_encode


class Car:
    
    def __init__(self, brand, year, plate, seats):
        self.brand= brand 
        self.year= year
        self.plate= plate
        self.seats= seats

    def get_brand(self):
        return self.brand
    
    def set_brand(self, new_brand):
        self.__brand= new_brand

        
    def show_car(self):
        print(f'El carro es de la marca {self.__brand}, del anio {self.year} ')
        print(f'Y tiene placa numero {self.plate}')

    def type_car(self):
        if self.seats > 20:
            return 'La unidad vehicular es un bus'
        elif self.seats > 10 and self.seats < 20 :
            return 'La unidad vehicular es una combi'
        else:
            return 'La unidad vehicular es un carro normal'

vehiculo = Car('Suzuki'. 2010, 'ABC-456, 4')
print(show_car(vehiculo))
print(type_car(vehiculo))


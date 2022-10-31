class Figura: 

    def __init__(self, nombre, area, x, y)
        self.nombre= nombre
        self.__area= area
        self.x= x
        self.y= y
    
    def get_area(self):
        return self.__area

    def set_area(self, area_nueva):
        self.__area = area_nueva
    
    def mostrar_figura(self):
        print(f'la figura se llama {self.nombre} \nTiene un area de {self.__area} m 2 \n e inicia en las cordenadas {self.x}, {self.y}')





# class A:
#     def usoA(self):
#         print('Uso de Clase A')
# class B:
#     def usoB(sef):
#         print('Uso de clase B')
# class AB(A, B):
import math
class Figura:
    def __init__(self, lados) -> None:
        self.lados = lados

    def area (sef):
        pass

class Circulo(Figura):
    def __init__(self, radio) -> None:
        super().__init__(l0)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2
    

class Rectangulo(Figura):
    def __init__(self, base, altura) -> None:
            super().__init__(lado)
            self.base= base
            self.altura = altura
    def area(self):
        return self.base * self.altura

class cuadrado(Rectangulo):
    def __init__(self, lado) -> None:
        super().__init__(lado, lado)






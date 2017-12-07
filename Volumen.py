from abc import abstractmethod
from math import pi

class Figura(object):
    def __init__(self, radio, altura, volumen):
        self.radio = radio
        self.altura = float(altura)
        self.volumen = float(volumen)

    @abstractmethod
    def tipo_figura(self):
        pass

class Esfera(Figura):
    def calcularVolumen(self):
        self.radio = float(input("\nValor del radio de la esfera: "))
        self.volumen = (4*pi*self.radio*self.radio)/3
        print("El volumen de su esfera es de", str(self.volumen), "m^3")

    def tipo_figura(self):
        return 'esfera'

class Cilindro(Figura):
    def calcularVolumen(self):
        self.radio = float(input("\nValor del radio del cilindro: "))
        self.altura = float(input("Valor de la altura del cilindro: "))
        self.volumen = pi*self.radio*self.radio*self.altura
        print("El volumen de su cilindro es de", str(self.volumen), "m^3")

    def tipo_figura(self):
        return 'cilindro'

class Cono(Figura):
    def calcularVolumen(self):
        self.radio = float(input("\nValor del radio del cono: "))
        self.altura = float(input("Valor de la altura del cono: "))
        self.volumen = (pi*self.radio*self.radio*self.altura)/3
        print("El volumen de su cono es de", str(self.volumen), "m^3")

    def tipo_figura(self):
        return 'cono'

if __name__ == '__main__':
    seguir = 's'

    print("\tCalculación de Volumenes")
    print("\nOpciones: Esfera, Cilindro, Cono")

    while(seguir == 'S' or seguir == 's'):
        esf = Esfera
        cil = Cilindro
        con = Cono

        respuesta = input("Escriba el nombre de una figuras en las opciones para calcular su Volumen: ")

        while respuesta not in ('esfera', 'cilindro', 'cono'):
            print("\nFigura no reconocida.")
            respuesta = input("Introduzca otra figura: ")
        if respuesta.lower() == 'esfera':
            esf.calcularVolumen(Esfera)
        elif respuesta.lower() == 'cilindro':
            cil.calcularVolumen(Cilindro)
        elif respuesta.lower() == 'cono':
            con.calcularVolumen(Cono)

        seguir = str(input("\nPara otra figura: oprima S. Para terminar programa: oprima otra tecla."))
        print("\n")
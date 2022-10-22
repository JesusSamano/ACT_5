from Particula import Particulas


class admpart:
    def __init__(self):
        self.__almpart = []

    def agregar_final(self, Particula:Particulas):
        self.__almpart.append(Particula)

    def agregar_inicio(self, Particula:Particulas):
        self.__almpart.insert(0, Particula)
    
    def mostrar(self):
        for Particula in self.__almpart:
            print(Particula)

particula01 = Particulas(id=1, origen_x=2, origen_y=3, destino_x=4, destino_y=5, velocidad=6, red=7, green=8, blue=9, distancia=10)
print(particula01)
particula02 = Particulas(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(particula02)
admpart = admpart()
admpart.agregar_inicio(particula02) 
admpart.agregar_final(particula01)
admpart.mostrar



        
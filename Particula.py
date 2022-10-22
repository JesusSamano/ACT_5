import math
#5
from algoritmos import distancia_euclidiana
#1
class Particulas:
    def __init__(self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red=0, green=0, blue=0, distancia =0 ):
           
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green 
        self.__blue = blue
        #3
        self.__distancia = distancia_euclidiana (origen_x, origen_y, destino_x, destino_y)    


#2
    #Imprimir valores de atributos
    def __str__(self):
         print("\n")
         return (
            
            "id: " + str(self.__id ) + "\n"+
            "origen_x: " + str(self.__origen_x ) + "\n"+
            "origen_y: " + str(self.__origen_y ) + "\n"+
            "destino_x: " + str(self.__destino_x ) + "\n"+
            "destini_y: " + str(self.__destino_y ) + "\n"+
            "velocidad: " + str(self.__velocidad ) + "\n"+
            "red: " + str(self.__red ) + "\n"+
            "green: " + str(self.__green ) + "\n"+
            "blue: " + str(self.__blue ) + "\n"+
            "distancia: " + str(self.__distancia ) + "\n"
         )   
#Asignar valores a los atributos 
#particula01 = Particulas(id=1, origen_x=2, origen_y=3, destino_x=4, destino_y=5, velocidad=6, red=7, green=8, blue=9, distancia = distancia_euclidiana)
#print(particula01)
#particula02 = Particulas(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
#print(particula02)
        
        
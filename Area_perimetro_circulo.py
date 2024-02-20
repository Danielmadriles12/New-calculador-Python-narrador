# Class perimetro circulo y area

from re import X

from math import *

class Circulo:
    def __init__(self,radio,diametro):
        self.diametro = diametro
        self.radio = radio
        
        
    def perimetro (self):
        
        
        #self.perimetro_circulo = float (self.perimetro_circulo)         
        resultado = 2 * pi * self.radio 
        print (" \n\tEl perimetro del circulo con un radio de ",self.radio," es ",resultado)
        
        
    def area (self):
        
       self.area_circulo = pi * self.radio **2
       return (self.area_circulo)

from math import nan
from turtle import color
from typing import Self, Type

# Narracion
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

class Calculador:
    
    
    def __init__(self,num1,num2):
        import numpy as np

        # Variables de operaciones constructor.

        self.num1 = num1
        self.nun2 = num2
        
        

        # Operaciones de sumar, restar, multiplicar y dividir.

        self.sumar = num1+num2
        self.restar = num1-num2
        self.multiplicar = num1*num2
        self.dividir = num1/num2
        self.area = (self.num1 * self.nun2)
        self.perimetro =((self.num1+self.nun2)*2)
        self.raiz = np.sqrt( self.num1)
        
        
        
        

# funciones de operaciones:

        

    def operracion_area_perimetro(self):

        print("\n\t\t\tEl perimetro de rectangulo es ",self.perimetro, "\tEl area es",self.area,"\n")
        # Narracion


    def operacion_sumar (self):

        print ("\n\t\t\tResultado de sumar  ", self.num1," mas " ,self.nun2," es ",self.sumar,"\n")
        
        reproducir = "El resultado de sumar "+ str  (self.num1) + "mas"+ str(self.nun2)+"es"+str (self.sumar)
        speaker.Speak(reproducir)
       
   
    def operacion_restar (self):
        
        print ("\n\t\t\tEl residuo de ", self.num1," entre " ,self.nun2," es ",self.restar,"\n")
        
        reproducir = "El residuo de "+str  (self.num1) + "entre"+ str(self.nun2)+"es"+str (self.restar)
        speaker.Speak(reproducir)
        
    def operacion_multiplicar (self):
        
        print ("\n\t\t\tResultado de multiplicar  ", self.num1," por " ,self.nun2," es ",self.multiplicar,"\n")
        
        reproducir = "Resultado de multiplicar "+str  (self.num1) + "por"+ str(self.nun2)+"es"+str (self.multiplicar)
        speaker.Speak(reproducir)

    def operacion_dividir (self):
        resul,resto = divmod(self.num1,self.nun2)
        
        
        print ("\n\t\t\t Resultado de dividir ", self.num1," entre " ,self.nun2," es ",self.dividir," \t Con un resto de ",resto,"\n")
        reproducir = "Resultado de dividir "+str  (self.num1) + "entre"+ str(self.nun2)+"es"+str (self.dividir)+" con un resto de "+str (resto)
        speaker.Speak(reproducir)
        
        
    def  operacion_raiz (self):
                
        if self.num1 < -1:
            print ("\n\t El resultado no es valido ")

        elif self.num1 >-1:
            print ("\n\t\t\t Resultado de la raiz de  ", self.num1," es ",self.raiz)
            reproducir = "Resultado de la rrait de"+str  (self.num1) + "es"+ str(self.raiz)
            speaker.Speak(reproducir)
        

    def menu_portada(self):
                
        archivo = open("menu.txt")# Abre el archivo
        menu = archivo.read()# Lee el archivo y lo escribe en la variable menu
        archivo.close()# Cierra el archivo
        print(menu)# Imprime el archivo por pantalla
        
    def menu_color(self):
                
            archivo = open("menu_color.txt")# Abre el archivo
            menu_color = archivo.read()# Lee el archivo y lo escribe en la variable menu
            archivo.close()# Cierra el archivo
            print(menu_color)# Imprime el archivo por pantalla
            #  AQUI ESTA EL FINAL DEL MODULO 1



   

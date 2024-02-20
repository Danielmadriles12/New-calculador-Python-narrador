
# media de numeros
import statistics

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

class Estadistica:
    def __init__(self):

        
        self.cantidadNumeros = int (input("\n Introduce de cuantos numeros quieres hacer la media "))# Cantidad de Numeros
        self.listaNumeros = []# Definicion de la lista numeros vacia
        
    def medias(self):
              
           # Creacion de la lista de numeros para hcer las estadisticas
            
        print (" introduce los numeros para hacer la estadistica ")
        for cantidadNumerosFinal in range(self.cantidadNumeros):
            print(" \nIntroduce numero ",cantidadNumerosFinal+1)
            valor = float (input("\n\t "))
            
            self.listaNumeros.append(valor)
        
        print ("\n La estadistica de los numeros ",self.listaNumeros, " seria: ")
        resultado = statistics.median(self.listaNumeros)
        
         #
        
        print (" \nMadia:    ",statistics.mean(self.listaNumeros))
        print (" \nMediana:  ",statistics.median(self.listaNumeros))
        print (" \nModa:     ",statistics.mode(self.listaNumeros))
        print (" \nVarianza: ",statistics.variance(self.listaNumeros))
        resultado1 = statistics.mean(self.listaNumeros)
        reproducir = "La media "+str( resultado1)
        speaker.Speak(reproducir)
        resultado2 = statistics.median(self.listaNumeros)
        reproducir = "La mediana "+str( resultado2)
        speaker.Speak(reproducir)
        resultado3 = statistics.mode(self.listaNumeros)
        reproducir = "La moda "+str( resultado3)
        speaker.Speak(reproducir)
        resultado4 = statistics.variance(self.listaNumeros)
        reproducir = "La varianza "+str( resultado4)
        speaker.Speak(reproducir)

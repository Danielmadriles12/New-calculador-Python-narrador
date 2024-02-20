from ast import Str
from tkinter import SEL
from ClassCalculador import \
    Calculador
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

class BinarioDecimal:
    
    def __init__(self,num10):    
               
        self.num10 = num10
        
        self.numero_original  = self.num10 # Aqui guardamos el binario oiginal 
        self.ndecimal = 0
        self.num10 = self.num10[::-1]# Invertimos el binario, para poder pasarlo a decimal; porque se empieza desde la derecha
        self.contador = 0
        self.potencia = 0
        self.numero_original = self.num10
        self.n_binario = 0
        

    def operacion_hexa (self):
        self.num10 = self.num10[::-1]
        self.resultado = int(self.num10,16)
        print ("\n\t El numero decimal del numero hexadecimal de ",self.num10," es ",self.resultado)
        reproducir = "El numero decimal del numero hexadecimal de "+str (self.num10)+" es "+ str (self.resultado)
        speaker.Speak(reproducir)
        
        

       
    def operacion_binario (self):
            reproducir = " estas en  binario"
            speaker.Speak(reproducir)
            try:
                for self.nbinario in self.num10:# Separamos el binario para poder hacerlo decimal
    
     
                    self.n_binario = int (self.nbinario)# Lo convertimos en entero para hacer operaciones
                    if self.n_binario >1 or self.n_binario < 0:# aqui vemos que es binario si no sale
                        print ("\t No es numero binario !!!!")
                        self.ndecimal = 0
                        break
                
                    resultado = (self.n_binario * 2)**self.potencia # Formula binario decimal
                    self.potencia +=1
                    self.ndecimal = self.ndecimal + resultado
                    print ("\t  ",self.nbinario,"* 2 ^",self.potencia," = ",resultado)
    

                print ("\n Resultado de sumar es ",self.ndecimal,", seria el numero decimal del binario ",self.numero_original,"\n" )
                reproducir = "Resultado de sumar es "+ str (self.ndecimal)+", seria el numero decimal del binario "+self.numero_original
                speaker.Speak(reproducir)
        
            except ValueError: # Aqui seria en caso de introducir teclas por error
                print (" !!!! No vale, no es binario !!!!")
                self.ndecimal = 0

 

import win32com.client
import math

speaker = win32com.client.Dispatch("SAPI.SpVoice")
class PotenciaNumero:
    
    def __init__ (self,base,exponente):
        self.base= base
        self.exponente = exponente
    
    def operacion (self):
        
        #self.resultado1 = self.base**self.exponente
        self.resultado = math.pow(self.base,self.exponente)
        print (" \n\tEl resultaddo de elevar el numero {a} a la pontecia {b} es {c}".format (a=self.base,b= self.exponente,c = self.resultado))
        #print (" \n\tEl resultaddo de elevar el numero {a} a la pontecia {b} es con ** {c}".format (a=self.base,b= self.exponente,c = self.resultado1))
        reproducir = "El resultao de elevar el numero "+str (self.base)+" a la potencia de  "+ str (self.exponente)+" es "+str (self.resultado)
        speaker.Speak(reproducir)
        
    
        
        

from ast import Import
import os
from typing import Self
from os import system

from Area_perimetro_circulo import Circulo
from ClassPrincipal import El_principal



class BucleCirculo:
    
    #def __init__(self):
        
        def principal():
             
        
        
            while True:
    
                print ("""

                                    MENU
           
                       A) AREA DE UN CIRCULO
           
                       P) PERIMETRO CIRCULO
                   
                       R) REGRESAR 
                        
                       L) LIMPIAR LA PANTALLA
           
    
            """)
                menu = input (" OPCION > \t")
                menu = menu.upper()
    
                if menu == "A":
        
                    radio = float (input (" \n\tINTRODUCE EL RADIO DEL CIRCULO\t "))
        
                    area = Circulo(radio,0)
                    print ("\n\t El area del circulo con un radio de ",radio," es ",area.area())
        
                elif menu == "P":
                    radio = float (input (" \n\tINTRODUCE EL RADIO DEL CIRCULO\t "))
        
                    perimetro = Circulo(radio,0)
                    perimetro.perimetro()
                    
                
                elif menu =="R":
                    system ("cls")
                    eje_calculadora = El_principal
                    eje_calculadora.principal()
                
                elif menu == "L":
                    system ("cls") 
            
            else:
                print(" !!! ADIOS !!!")
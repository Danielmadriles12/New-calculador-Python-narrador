 
from turtle import color
from typing import Self

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


class El_principal:

    def principal():# Funcion principal
        
        import time  # Importador de la pausa (TIME)
        import webbrowser  # Importador para invocar una pagina web
        from os import system

        import numpy as np

        from clases_color import Color
        from PotenciaNumero import PotenciaNumero
        # importaciones de las clases
        from ClassBinario import BinarioDecimal
        from ClassCalculador import Calculador  # Importador de la clase Calculador y fucion _init__
        from menuCirculo import BucleCirculo
        from PotenciaNumero import PotenciaNumero
        from EstadisticasNumeros import Estadistica
        
        system ("title Calculadora en Python con Class")# Cambia el titulo de la consola
        portada = Calculador(1,1)
        portada.menu_portada()# LLama al menu

        #Bucle del programa:
        tecla = "\n INTRODUCE LA LETRA DEL TIPO DE OPERACION \n\n\t"
        
        while True:# Bucle del cuerpo del programa, llamadas a funciones y correccion de posibles errores de entrada de codigo por el usuario
            try:
                
                print (tecla)
                reproducir = tecla+" Cee para limpiar la pantalla"
                speaker.Speak(reproducir)
                menu = input()# Entrada de datos para realizar
                menu = menu.upper()
                
            
        
                if menu == "H":# Salir del programa
                    print("\n\n\t El blog de Mia !!! HASTA PRONTO !!!\n\n","\n    Te invito a ver la WEB el Blog de Mia")
                    reproducir = " El blog de Mia  HASTA PRONTO    Te invito a ver la WEB el Blog de Mia"
                    speaker.Speak(reproducir)
                    time.sleep(6)# Pusa en programa
                    webbrowser.open("https://elblogdemia.es/")# Llamada a la pagina WEB
                    webbrowser.open("https://danielcaraballo.es/")# Llamada a la pagina WEB
                    system ("cls")
                    break # Salida y limpieza de pantalla de la consola de comandos

                elif menu == "L":
                    
                    num10 = input ("\nIntroduce numero binario ")
                    binario = BinarioDecimal(num10)
                    binario.operacion_binario()
                    
                # color de la pantalla
                
                elif menu=="N":
                    menu_color= Calculador (1,1)
                    menu_color.menu_color()
                    
                    
                    colores = Color(color)
                    colores.operacion_color()
                    
                    tada = Calculador(1,1)
                    portada.menu_portada()
                

                elif menu =="M":
                    num10 = input ("\nIntroduce numero hexadecimal ")
                    
                    hexadecimal = BinarioDecimal(num10)
                    hexadecimal.operacion_hexa()
                    
                
                elif menu == "F":
                    la_fecha_es = time.asctime()
                    print ("\n\n\t Hora y fecha actual ",la_fecha_es,"\n\n")
                    
                elif menu =="K":
                    numb =int(input("\nIntroduce numero decimal "))
                    binario = bin (numb)
                    
        
                    print ("\n\t\t\tEl binario de ",numb," es ",binario,"\n")
                
                  
                elif menu =="I":# Creacion de codigo de tablas de multiplicar
                    print (" Estas creando tablas de multiplicar ".center(100))

                    num1 =int(input("\nIntroduce numero de tabla "))
                    num2 =int(input("\nIntroduce hasta cuanto "))
                    num2 +=1

                    for fin in range(num2):# bucle contador final de tabla hasta llegar al valor de contador + 1 
                    
                        print ("\t\t\t\t\t\t\t\t",num1, " * ",fin," = ",num1 * fin )# imprimir tabla por pantalla
                        
       
                                
                elif menu == "A":
                   
                    
                    print (" Estas en la suma ".center(100))
                    
                    ope1 =float(input("\nIntroduce sumando 1 "))
                    ope2 =float(input("\nIntroduce sumando 2 "))
                    sumar = Calculador(ope1,ope2)
                    sumar.operacion_sumar()

                elif menu == "E":# Llamada al perimetro del rectangulo y el area 
                    print (" Estas creando area y perimetro rectangulo  ".center(100))

                    ope1 =float(input("\nIntroduce altura    "))
                    ope2 =float(input("\nIntroduce base      "))
                    while ope1 <=0 or ope2:# Bucle para comprobar que los valores introducidos no sean negativos
                        try:
                            if ope1<=0:

                                print ("\n\t Altura introducida no es valida ")
                                time.sleep(2)# Pusa en programa
                                ope1 =float(input("\nIntroduce altura correcta    "))

                            elif ope2<=0:

                                print ("\n\t La base introducida no es valida ")
                                time.sleep(2)# Pusa en programa
                                ope2 =float(input("\nIntroduce base correcta      "))
                            else:
                        
                                area = Calculador(ope1,ope2)
                                area.operracion_area_perimetro()
                                break
                        except (ValueError,EOFError,):# Podemos poner varios errores como en una Tupla entre parentesis.
                            print(" Valor no valido")
                            reproducir = " Valor no valido "
                            speaker.Speak(reproducir)
                            time.sleep(2)# Pusa en programa
                            area = Calculador(ope1,ope2,0)
                            area.operracion_area_perimetro()
                            system ("cls")
                            
                        

           
                elif menu == "D":
                    print (" Estas en la resta ".center(100))
                    ope1 =float(input("\nIntroduce minuendo   "))
                    ope2 =float(input("\nIntroduce sustraendo "))
                    sumar = Calculador(ope1,ope2)
                    sumar.operacion_restar()

           
                elif menu == "G":
                    print (" Estas en la multiplicacion ".center(100))
                    ope1 = int(input("\nIntroduce  multiplicando "))
                    ope2 = int(input("\nIntroduce  multiplicador "))
                    multiplicar = Calculador(ope1,ope2)
                    multiplicar.operacion_multiplicar()

            
                elif menu == "B":
                    print (" Estas en la division ".center(100))
                    
                    ope1 =float(input("\nIntroduce dividendo "))
                    ope2 =float(input("\nIntroduce divisor   "))
                    sumar = Calculador(ope1,ope2)
                    sumar.operacion_dividir()
                   
                    
                elif menu =="C":
                    print ("\n\n\t !!! LIMPIANDO !!!")
                    time.sleep(2)# Pusa en programa
                    system ("cls")
                    portada = Calculador(1,1)
                    portada.menu_portada()

                elif menu == "J":
                    print (" Estas en la raiz cuadrada ".center(100))
                    reproducir = " estas en la rrait "
                    speaker.Speak(reproducir)
                    ope2 =float(input("\nIntroduce numero para raiz "))
                    ope1 = ope2
                    raiz = Calculador(ope1,ope2)
                    raiz.operacion_raiz()

                elif menu == "PY":
                    webbrowser.open("https://danielcaraballo.es/")# Llamada a la pagina WEB
                    reproducir = "  WEB el Blog de Mia"
                    speaker.Speak(reproducir)

                elif menu == "PDF":
                    webbrowser.open("https://danielcaraballo.es/programacion-en-poo-y-modulos-importables-python/")# Llamada a la pagina WEB
                    reproducir = "  WEB el Blog de Mia"
                    speaker.Speak(reproducir)

                elif menu == "O":
                    system ("cls")
                    calculadora = BucleCirculo
                    calculadora.principal()

                elif menu =="P":
                    base = int(input ("\nIntroduce la base "))
                    exponente = int (input(" Introduce el exponente ^ "))
        
                    operacion_potencia = PotenciaNumero (base,exponente)
                    operacion_potencia.operacion()

                elif menu == "Q":
                    estadistica = Estadistica()
                    estadistica.medias()
                    

  

                else :
                    print(" Valor no valido")
                    reproducir = " Valor no valido "
                    speaker.Speak(reproducir)
                    time.sleep(2)# Pausa en programa
                    system ("cls")
                    portada = Calculador(1,1)
                    portada.menu_portada()

            except (ValueError,KeyboardInterrupt,EOFError,RuntimeWarning,ZeroDivisionError):
                print(" Valor no valido")
                reproducir = " Valor no valido "
                speaker.Speak(reproducir)
                time.sleep(2)# Pausa en programa
                system ("cls")
                portada = Calculador(1,1)
                portada.menu_portada()


# Aqui esta el final del modulo 2

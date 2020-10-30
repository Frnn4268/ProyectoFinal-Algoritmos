from datetime import datetime
import re
import os
print("==================================================================================")
print("|                           Bienvenidos al Banco FIU S.A                         |")
print("|                                 Cuidamos tu futuro                             |")
print("==================================================================================")
print(" ")
print(" ")
print("==================================================================================")
print("|                                GENERADOR DE TICKETS                            |")
print("|Ejecutar:                                                                       |")
print("|[1] Generar nuevo Ticket                                                        |")
print("==================================================================================")

seleccion = int(input())

while (seleccion!=3):
        if seleccion == 1: 
            print("==================================================================================")
            print("|                                SELECCIÓN DE TICKETS                            |")
            print("|Escoja una de las opciones:                                                     |")
            print("|[1] CAJA                                                                        |")
            print("|[2] SAC                                                                         |")
            print("==================================================================================")
            seleccion1 = int(input())

            if seleccion1 == 1:
                ubicacion = open("ubicacion.txt", "a")
                codigo_numerico= open("codigo_numerico.txt", "a")
                codigo= open("codigo.txt", "a")
                impresion = open("impresiones.txt", "a")
                digitos3= "000"
                digitos2= "00"

                fecha=datetime.now()

                año = str(fecha.year)
                mes = str(fecha.month)
                dia = str(fecha.day)
                tot = int((año + mes + dia))
                total = str(tot)

                nuevo = open("codigo.txt", "r+")
                #se escribe  los datos a utilizar
                #se agrega datos al fichero
                valor=(nuevo.readlines())
                #se cierra el fichero
                nuevo.close()

                valores = str(valor)
                cortar = re.split("\s",valores)
                contador = len(cortar)
                personas= str(contador)


                lugar = "CAJA"
                estacion = "CAJA "
                ubicacion.write(estacion)

                if (contador < 10):
                    valores= lugar+"-"+total+digitos3+personas+" "
                    numero=total+digitos3+personas+" "
                
                if (contador >= 10):
                    valores= lugar+"-"+total+digitos2+personas+" "
                    numero=total+digitos2+personas+" "

                codigo_numerico.write(numero)
                codigo.write(valores)
                impresion.write(valores)

                ubicacion.close()
                codigo_numerico.close()
                codigo.close()
                impresion.close()

                print("==================================================================================")
                print("|Ticket ingresado correctamente                                                  |")
                print("|Ticket: "+ valores +"                                                      |")
                print("|                                                                                |")
                print("==================================================================================")
                input("presione enter para continuar")
                os.system('cls')

            if seleccion1 == 2:
                    ubicacion = open("ubicacion.txt", "a")
                    codigo_numerico= open("codigo_numerico.txt", "a")
                    codigo= open("codigo.txt", "a")
                    impresion = open("impresiones.txt", "a")
                    digitos3= "000"
                    digitos2= "00"

                    fecha=datetime.now()

                    año = str(fecha.year)
                    mes = str(fecha.month)
                    dia = str(fecha.day)
                    tot = int((año + mes + dia))
                    total = str(tot)

                    nuevo = open("codigo.txt", "r+")
                    #se escribe  los datos a utilizar
                    #se agrega datos al fichero
                    valor=(nuevo.readlines())
                    #se cierra el fichero
                    nuevo.close()

                    valores = str(valor)
                    cortar = re.split("\s",valores)
                    contador = len(cortar)
                    personas= str(contador)


                    lugar = "SAC"
                    estacion = "SAC "
                    ubicacion.write(estacion)

                    if (contador < 10):
                        valores= lugar+"-"+total+digitos3+personas+" "
                        numero=total+digitos3+personas+" "
                    
                    if (contador >= 10):
                        valores= lugar+"-"+total+digitos2+personas+" "
                        numero=total+digitos2+personas+" "

                    codigo_numerico.write(numero)
                    codigo.write(valores)
                    impresion.write(valores)

                    ubicacion.close()
                    codigo_numerico.close()
                    codigo.close()
                    impresion.close()

                    print("==================================================================================")
                    print("|Ticket ingresado correctamente                                                  |")
                    print("|Ticket: "+ valores +"                                                       |")
                    print("|                                                                                |")
                    print("==================================================================================")
                    input("presione enter para continuar")
                    os.system('cls')
        else:
            print("vuelva a esojer")


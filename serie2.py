import time
import re
import os


while True:
    nuevo = open("impresiones.txt", "r+")
    valor=(nuevo.readlines())
    nuevo.close()

    valores = str(valor)
    cortar = re.split("\s",valores)
    contador = len(cortar)


    while True:
        if (contador>1):
            
            primero=cortar.pop(0)
            cortar.pop()
            numero1 = re.split("'",primero)
            print("==================================================================================")
            print("|                                IMPRESIÓN DE TICKETS                            ")
            numero1.pop(0)
            numero=str(numero1)

            print("|" +numero[2:-2])
            for cantidad in cortar:
                print("|"+cantidad)

            print("==================================================================================")
            print("Actualizando")
            time.sleep(2)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            os.system('cls')
            break


        elif(contador<=1):
            print("==================================================================================")
            print("|Esperando tickets                                                               |")
            time.sleep(2)
            print("|.                                                                               |")
            time.sleep(1)
            print("|.                                                                               |")
            time.sleep(1)
            print("|.                                                                               |")
            time.sleep(1)
            os.system('cls')

            break

import time
import re
import os

while True:
    nuevo = open("verificacion.txt", "r+")
    #se escribe  los datos a utilizar
    #se agrega datos al fichero
    valor=(nuevo.read())
            #se cierra el fichero
    nuevo.close()

    valores = str(valor)
    cortar = re.split("\s",valores)
    contador = len(cortar)
    verificar=int(contador)


    while True:

        if (verificar>1):
            print("==================================================================================")
            print("|"+valores)
            print("==================================================================================")
            print("PROCESANDO")
            time.sleep(2)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            variables = open("verificacion.txt", "wt")
            datos_nuevoss = ""
            variables.write(datos_nuevoss)
            variables.close()
            os.system('cls')
            break
            

        elif (verificar<=1):
            print("==================================================================================")
            print("|Esperando confirmación                                                          |")
            time.sleep(1)
            print("|...                                                                             |")
            print("==================================================================================")
            time.sleep(1)

            os.system('cls')
            break
                    
        else:
            print("malo")
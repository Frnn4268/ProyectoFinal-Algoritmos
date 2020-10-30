import time
import re
import os

print("==================================================================================")
print("|                                   Banco FIU S.A                                |")
print("|                                 Cuidamos tu futuro                             |")
print("==================================================================================")
while True:
    nuevo = open("ubicacion.txt", "r+")
    #se escribe  los datos a utilizar
    #se agrega datos al fichero
    valor=(nuevo.readlines())
    #se cierra el fichero
    nuevo.close()

    valores = str(valor)
    cortar = re.split("\s",valores)
    total = list(cortar)
    contador = len(cortar)
    total.pop()


    codigo_nuevo = open("codigo.txt", "r+")
    #se escribe  los datos a utilizar
    #se agrega datos al fichero
    codgio_verificado=(codigo_nuevo.readlines())
    #se cierra el fichero
    codigo_nuevo.close()

    valores_especificos = str(codgio_verificado)
    valores_cortados = re.split("\s",valores_especificos)
    totales_a_eliminar = list(valores_cortados)

    totales_a_eliminar.pop()



    codigo_nuevos = open("codigo_numerico.txt", "r+")
    #se escribe  los datos a utilizar
    #se agrega datos al fichero
    codgio_verificados=(codigo_nuevos.readlines())
    #se cierra el fichero
    codigo_nuevos.close()

    valores_especificoss = str(codgio_verificados)
    valores_cortadoss = re.split("\s",valores_especificoss)
    totales_a_eliminars = list(valores_cortadoss)

    totales_a_eliminars.pop()


    escojer= 0
    while (escojer!= 2):
        print("==================================================================================")
        print("|                              ELIMINACIÓN DE TICKETS                            |")
        print("|Escoja una de las opciones:                                                     |")
        print("|[1] Atender al cliente                                                          |")
        print("|[2] Salir                                                                       |")
        print("==================================================================================")
                    
        escojer=int(input())
        if(escojer == 1):
            ventanilla ="1"
            print(" ")
            print("==================================================================================")
            print("|porfavor acceda a la ventanila: " + ventanilla)  
            valor2 =total.pop(0)
            corregido = valor2
            print("|operacion: " + corregido)
            print("==================================================================================")
            print(" ")
            print(" ")

            nuevo = open("ubicacion.txt", "wt")
            datos_del_nuevo = str(total)
            nuevo.write(datos_del_nuevo)
            nuevo.close()

            totales_a_eliminar.pop(0)
            variable = open("codigo.txt", "wt")
            datos_nuevos = str(totales_a_eliminar)
            variable.write(datos_nuevos)
            variable.close()


            variablees = open("impresiones.txt", "wt")
            datos_nuevoses = str(datos_nuevos)
            variablees.write(datos_nuevoses)
            variablees.close()



            valor=str(totales_a_eliminars.pop(0))
            variables = open("codigo_numerico.txt", "wt")
            datos_nuevoss = str(totales_a_eliminars)
            variables.write(datos_nuevoss)
            variables.close()


            ubicacion = open("verificacion.txt", "a")
            estacion = " El_ticket_" + valor + "_se_le_solicita_la_ventanilla_1"
            ubicacion.write(estacion)
            ubicacion.close()
            print("PROCESANDO")
            time.sleep(2)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)

            while True:
                print("==================================================================================")
                print("|Desea finalizar atencion?                                                       |")
                print("[1]  Si                                                                          |")
                print("==================================================================================")
                var1=input()
                if(var1 != 1):
                    print("==================================================================================")
                    print("|Gracias por su preferencia                                                      |")
                    print("|Vuelva pronto                                                                   |")
                    print("==================================================================================")
                    input("Presione enter para continuar")
                    os.system('cls')
                    break
                                
        if(escojer == 2):
            print("adios")
            break








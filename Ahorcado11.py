#Juego de ahorcado para Desarrollo de Aplicaciones Web
#Autor: luis jesus villarruel martinez
#Actualizado 24/02/2020
import os, time
from random import choice

print("Juego de ahorcado 1.1 - 24/febrero/2020")
print("Instruccion: Introduce letras una a una hasta revelar la palabra")

palabra = ""
contadorErrores = 0
contadorLetras = ""
totalLetras = ""
bandera = 1 == 1
mensaje = ""
base = """
 ______
 |    |
 |   
 |  
 |  
 |  
----------"""
error1 = """
 ______
 |    |
 |    O
 |  
 |  
 |  
----------"""
error2 = """
 ______
 |    |
 |    O
 |    |
 |  
 |  
----------"""
error3 = """
 ______
 |    |
 |    O
 |   -|
 |  
 |  
----------"""
error4 = """
 ______
 |    |
 |    O
 |   -|-
 |  
 |  
----------"""
error5 = """
 ______
 |    |
 |    O
 |   -|-   ultima oportunidad
 |   /
 |  
----------"""
error6 = """
 ______
 |    |
 |    O    FIN DEL JUEGO
 |   -|-
 |   //
 |     
----------"""

def seleccionPalabra():
    global palabra
    with open("lemario.txt", "r", encoding="utf8") as file:
        listaPalabras = file.readlines()
        
    palabra=choice(listaPalabras)
    palabra=palabra.rstrip()
    

#funcion que imprime en pantalla el avance
def horca(v):
    global palabra
    global contadorLetras
    
    if v == 0:
        print(base)
    elif v == 1:
        print(error1)
    elif v == 2:
        print(error2)
    elif v == 3:
        print(error3)
    elif v == 4:
        print(error4)
    elif v == 5:
        print(error5)
    elif v == 6:
        print(error6)
    print("")
    
    if contadorLetras=="":
        for i in range(len(palabra)):
            print("_ ",end="")
    else:
        for i in range(len(palabra)):
            guion = 1 == 1
            for j in range(len(contadorLetras)):
                if contadorLetras[j] in palabra[i]:
                    print(contadorLetras[j], end=" ")
                    guion = 0 == 1
            if guion:
                print("_ ",end="")
    print(" ")
    
#funcion que comprueba si la letra esta repetida o si es parte de la palabra
def comprobar(letra):
    global mensaje
    global totalLetras
    global contadorErrores
    global contadorLetras

    if len(letra) != 1:
        mensaje="elige solo una letra"
    elif letra.isalpha():
        
        if letra in totalLetras:
            mensaje= "la letra " + letra + " ya ha sido elegida"
        else:
            totalLetras += letra
            if letra in palabra:
                mensaje="bien"
                contadorLetras += letra
            else:
                contadorErrores += 1
                mensaje=("X"*contadorErrores)
                
    else:
        mensaje=" "+letra+" no es una letra"
            
#funcion que revisa si se ha ganado o perdido.
def ahorcado(letras):
    global mensaje
    
    victoria=0
    for i in range(len(palabra)):
        for j in range(len(letras)):
            if letras[j] in palabra[i]:
                victoria+=1
                
    if contadorErrores == 6:
        print("HAS PERDIDO")
        print("la palabra era ", palabra)
        return 1==2
    elif victoria >= len(palabra):
        print("HAS GANADO")
        return 1==2
    else:
        return 1==1

   
#condiciones de cierre
def preguntaFinal():
    respuesta = input("quieres jugar otra vez? (presiona 1 para si) ")
    if respuesta == "1":
        resetear()
        nuevoJuego()
    else:
        print("Cerrando...")
        time.sleep(1)

#Para que preguntaFinal no tenga problemas:
def resetear():
    global palabra
    global contadorErrores
    global contadorLetras
    global totalLetras
    global bandera
    global mensaje
    palabra = ""
    contadorErrores = 0
    contadorLetras = ""
    totalLetras = ""
    bandera = 1 == 1
    mensaje = ""
    
#JUEGO
def nuevoJuego():
    global bandera
    global mensaje
    
    seleccionPalabra()
    os.system("cls")
    print("==========AHORCADO===========")
    print("letras ya elegidas: ", totalLetras)
    horca(contadorErrores)
    
    while bandera:
        entrada = input("Introduce una letra: ")
        os.system("cls")
        entrada = entrada.lower()
        comprobar(entrada)
    
        print("==========AHORCADO===========")
        print("letras ya elegidas: ", totalLetras)
        horca(contadorErrores)
        print("")
        print("Comentario: ",mensaje)
        print("")
        mensaje=""
        bandera = ahorcado(contadorLetras)
        
    preguntaFinal()

#Llamada a funcion principal
print("Iniciando...")
time.sleep(1)
if __name__ == "__main__":
    nuevoJuego()

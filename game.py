#Libreria
import os
import time
from playsound import playsound

clear = lambda: os.system('cls')

#Funcion
def print_x(x):
    print (x)
    time.sleep(1.5)

def gameover():
        playsound('audio.mp3')
        print_x(31*"*")
        print_x(10*"*"+" GAME OVER "+10*"*")
        print_x(31*"*")
        ciclo = int(input("¿Quieres jugar? \n 1. SI \n 2. NO\n"))
        if ciclo == 1:
            clear()
            game()
        elif ciclo == 2:
            exit("JUEGO TERMINADO...")

def game():
    print(70*"*")
    print(10*"*"+" Bienvenidos a la aventura del Pirata Barba Negra "+10*"*")
    print(70*"*")
    print_x("Historia: Tu mision aqui será encontrar el tesoro y ser el primero en escapar con vida ")
    print_x("Historia: Ingresas a la isla y encuentras dos caminos cubiertos de hojas y con un letrero en un idioma que no entiendes... ")
    print_x("Historia: Pero hay rastros de pasos mas frescos en el de la Derecha ¿Que camino tomas? ")
    opcion = int(input("Elige: \n1. Derecha \n2. Izquierda \n"))
    clear()
    if opcion == 1:
        print_x("Oh no! Caiste en un agujero")
        gameover()
    elif opcion == 2:
        print_x("Historia: Super! Has llegado al patio de una mansion abandonada, pero hay un problema...")
        print_x("Hay un lago lleno de cocodrilos con una isla en centro y un cofre, ¿Nadas hacia el o esperas que se vayan?")
        opcion = int(input("Elige: \n1. Nadar \n2. Esperar \n"))
        clear()
        if opcion == 1:
            print_x("Oh no! Hay una tribu y te empieza a atacar con flechas")
            gameover()
        elif opcion == 2:
            print_x("Historia: Wow! Has visto a un nativo salir de la mansion y dejar la puerta abierta, ¡vamos a entrar!")
            print_x("Llegas a la sala principal y hay 3 puertas con diferentes colores, ¿Cual abres?")
            opcion = int(input("Elige: \n1. Rojo \n2. Azul \n3. Amarillo \n4. Otra \n"))
            clear()
            if opcion == 1:
                print_x("Que mala suerte! Miembros de la tribu tenian una trampa y te han quemado vivo.")
                gameover()
            elif opcion == 2:
                print_x("Que mala suerte! Ahora eres el alimento de un par de tigres.")
                gameover()
            elif opcion == 3:
                print_x("Historia: Te has encontrado con un tablero y una mezcla de figuras, estas crean nombres, son dioses de la Mitologia Griega...")
                print_x("Historia: Hace falta una pieza en el arbol que conforman estos dioses, que pasará si pones al dios de dioses?")
                dios = input("¿Como se llama el dios de todos los dioses en la mitologia griega?\n").upper()
                clear()
                if dios == "ODIN":
                    print_x("Historia: Se ha abierto una puerta a tu espalda, es hora de explorar...")
                    print_x("Historia: Llegaste a una habitacion donde hay varios nativos armados pero en el fondo alcanzas a ver una montaña de oro...")
                    print_x("Historia: Tienes dos opciones, huir como un cobarte o luchar y tener posibilidades de irte con los bolsillos llenos!")
                    opcion = int(input("Es momento de decir: \n1. Atacar \n2. Huir \n"))
                    clear()
                    if opcion == 1:
                        print_x("Historia: Vas corriendo y atacas al primer nativo, lo asesinas brutalmente frente a los demas, los cuales huyen sospechosamente...")
                        print_x("Historia: Tomas el tesoro y mientras sales te das cuenta que hay nativos esperando fuera de la mansion...")
                        print_x("Historia: Cuando sales te das cuenta que te estan esperando con arcos y lanzas, crees que es el final...")
                        print_x("Historia: En ese momento, todos los nativos se arrodillan frente a ti, y te proclaman rey, pero... ¿Por que?")
                        print_x(35*"*")
                        print_x(10*"*"+" CONTINUARA... "+10*"*")
                        print_x(35*"*")
                        exit("HAS COMPLETADO LA BETA")
                    elif opcion == 2:   
                        print_x("Historia: Te regresas y corres como nunca, mientras tres nativos corren detras tuyo con lanzas y unas ganas gigantes de volverte parte de su decoracion...")
                        print_x("Historia: Cuando vas saliendo del tunel inicial, te das cuenta que hay un nativo mas grande que los demas y con pinturas en su rostro... ¿Quien será?")
                        print_x("Historia: Tratas de escapar de el pero no lo logras... Para finalmente asesinarte y demostrar la razón de ser el Rey de la tribu.")
                        print_x("Has muerto como un cobarde!")
                        gameover()      
                    else:
                        print("Esa opcion no existe!")
                else:
                    print_x("Historia: Fallaste, se abrio una trampilla en el piso y ahora vives con pirañas, Game Over ;)")
            elif opcion == 4:
                print_x("Que mala suerte! Esa puerta no era la correcta y ahora eres parte de la decoracion de los nativos.")
                gameover()
        else:
            print("Opcion Incorrecta")
            gameover()
    else:
        print("Opcion Incorrecta")
        gameover()
    
    

#Inicio

game()

import time
def main():
    print("Bienvenid@ al Ejercicio 2 del Lab 1 de Sistemas de Codificación de Audio y Video \U0001F47E.")
    print("A continuación procederemos a convertir 3 valores [Y,U,V] a 3 valores [R,G,B].")
    print("Por favor, introduce un valor(entre 0 y 255) para el canal Y:")
    y = input()
    while float(y)>255 or float(y)<0:
        print(f"El valor de Y introducido no es correcto. Por favor, vuelva a introducir un valor(entre 0 y 255) para el canal Y:")
        y = input()
    print("Genial. Ahora introduce un valor(entre 0 y 255) para el canal U:")
    u = input()
    while float(u)>255 or float(u)<0:
        print(f"El valor de U introducido no es correcto. Por favor, vuelva a introducir un valor(entre 0 y 255) para el canal U:")
        u = input()
    print("Genial. Por último, introduce un valor(entre 0 y 255) para el canal V:")
    v = input()
    while float(v)>255 or float(v)<0:
        print(f"El valor de V introducido no es correcto. Por favor, vuelva a introducir un valor(entre 0 y 255) para el canal V:")
        v = input()
    print("Convirtiendo los valores [Y,U,V]=["+str(y)+", "+str(u)+", "+str(v)+"]")
    i = 0
    while i < 36:
        print(".", end="")
        i = i + 1
        time.sleep(0.1)
    print(f"\n¡Conversión completada correctamente!")
    Y = float(y)
    U = float(u)
    V = float(v)

    R = round((Y + 1.402*(V-128)), 2)
    G = round((Y - 0.34414*(U-128) - 0.71414*(V-128)), 2)
    B = round((Y + 1.772*(U-128)),2)
    print("Tus valores RGB son ["+str(R)+", "+str(G)+" ,"+str(B)+"]!!")
    time.sleep(1)
    print(f"Volviendo al menú principal...")
    time.sleep(3)

main()
import main
main.lab1_main()
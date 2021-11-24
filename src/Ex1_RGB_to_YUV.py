import time
def main():
    print("Bienvenid@ al Ejercicio 1 del Lab 1 de Sistemas de Codificación de Audio y Video \U0001F47E.")
    print("A continuación procederemos a convertir 3 valores [R,G,B]  a 3 valores [Y,U,V].")
    print("Por favor, introduce un valor(entre 0 y 255) para el canal R:")
    r = input()
    while float(r)>255:
        print(f"El valor de R introducido no es correcto. Por favor, vuelva a introducir un valor(entre 0 y 255) para el canal R:")
        r = input()
    print("Genial. Ahora introduce un valor(entre 0 y 255) para el canal G:")
    g = input()
    while float(g)>255:
        print(f"El valor de G introducido no es correcto. Por favor, vuelva a introducir un valor(entre 0 y 255) para el canal G:")
        g = input()
    print("Genial. Por último, introduce un valor(entre 0 y 255) para el canal B:")
    b = input()
    while float(b) > 255:
        print(
            f"El valor de B introducido no es correcto. Por favor, vuelva a introducir un valor(entre 0 y 255) para el canal B:")
        b = input()

    print("Convirtiendo los valores [R,G,B]=["+str(r)+", "+str(g)+", "+str(b)+"]")
    i = 0
    while i < 36:
        print(".", end="")
        i = i + 1
        time.sleep(0.1)
    print(f"¡Convertido correctamente!")
    R = float(r)
    G = float(g)
    B = float(b)

    Y = round((0.299*R + 0.587*G + 0.114*B), 2)
    U = round((0.493*(B-Y)), 2)
    V = round((0.877*(R-Y)), 2)
    print("Tus valores YUV son ["+str(Y)+", "+str(U)+" ,"+str(V)+"]!!")
    print("")
    time.sleep(1)
    print(f"Volviendo al menú principal...")
    time.sleep(3)

main()
import main
main.lab1_main()
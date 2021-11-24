
import time

def run_length_encoding(seq):
    compressed = []
    count = 1
    char = seq[0]
    for i in range(1 ,len(seq)):
        if seq[i] == char:
            count = count + 1
        else :
            compressed.append([char ,count])
            char = seq[i]
            count = 1
    compressed.append([char ,count])
    return compressed

def main():
    print(f"Bienvenid@ al Ejercicio 4 del Lab 1 de Sistemas de Codificación de Audio y Video \U0001F47E."
          f"\nAhora procederemos a comprimir una secuencia de caracteres, en otra codificada:")
    print(f"Por favor, introduce una secuencia de letras en mayúscula:")
    seq = input()
    print(f"La secuencia que has introducido es: "+str(seq)+".")
    print(f"Codificando:")
    i = 0
    while i < 36:
        print(".", end="")
        i = i + 1
        time.sleep(0.1)
    list1 = run_length_encoding(seq)
    compressed_seq = ''
    for i in range(0, len(list1)):
        for j in list1[i]:
            compressed_seq += str(j)
    print(f"\n¡Secuencia codificada con éxito!")
    print(f"La secuencia codificada es: "+str(compressed_seq)+".\n")
    time.sleep(2)
    print(f"Volviendo al menú principal...")
    time.sleep(3)

main()
time.sleep(1)
import main
main.lab1_main()

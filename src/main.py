import sys
import os.path
import time
def lab1_main():
    print(f"\nBienvenido al LAB 1 de Sistemas de Codificación de Video.")
    print("A continuación te mostraremos el listado de ejercicios disponibles en este lab:")
    print(f"....................................")
    print(f". 1. RGB to YUV:                   .")
    print(f". 2. YUV to RGB:                   .")
    print(f". 3. Resize 2pac.jpeg image:       .")
    print(f". 4. Compress Lenna image:         .")
    print(f". 5. Run-length encoding:          .")
    print(f". 6. DCT:                          .")
    print(f".                                  .")
    print(f". 7. Salir del programa:           .")
    print(f"....................................")
    ex = input("¿Que ejercicio quieres ejecutar...?")
    if ex == '7':
        option = input(f"Estas seguro que desea salir del programa? [y/n]")
        if option == 'y':
            sys.exit()
        else:
            return lab1_main()
    else:
        aux = 0
        while aux == 0:
            if ex == '1':
                import Ex1_RGB_to_YUV as ex1
                ex1.main()
            elif ex == '2':
                import Ex2_YUV_to_RGB as ex2
                ex2.main()
            elif ex == '3':
                import Ex3_Resize_Image as ex3
                ex3.main()
            elif ex == '4':
                import Ex4_Compression_BW as ex4
                ex4.main()
            elif ex == '5':
                import Ex5_Run_Length as ex5
                ex5.main()
            elif ex == '6':
                import Ex6_DCT_Coding as ex6
                ex6.main()
            else:
                time.sleep(1)
                print("\nNúmero de ejercicio incorrecto. Introduce uno de los 6 ejercicios disponibles atontao :')\n")
                return lab1_main()


lab1_main()
sys.exit()

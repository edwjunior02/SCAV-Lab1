import time
from scipy.fftpack import dct, idct
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt

# Definimos la función dct2 que nos calcula la transformada discreta del coseno de una imagen.
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# Definimos la función idct2 que nos reconstruye la transformada discreta del coseno en una imagen.
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

def main():
    print(f"Bienvenid@ al Ejercicio 6 del Lab 1 de Sistemas de Codificación de Audio y Video \U0001F47E.")
    print(f"En este ejercicio, aplicaremos los métodos DCT en imágenes. Nuestra imágen de muestra será Lenna.jpeg.")
    print(f"Primero vamos a cargar la imagen de Lenna.jpeg y la almacenaremos en una variable para poder manipularla.")
    print(f"\nCargando foto: Lenna.jpeg")
    i = 0
    while i < 10:
        print(f".", end="")
        i = i + 1
        time.sleep(0.1)
    print(f"¡Carga completada!")
    print(f"Transformando a imagen en blanco y negro:")
    i = 0
    while i < 10:
        print(f".", end="")
        i = i + 1
        time.sleep(0.1)
    # Leemos la imagen de Lenna.jpeg y la pasamos a escala de grises mediante el método rgb2gray de la libreria scikit-image.
    im = rgb2gray(imread('/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D\'ÀUDIO I '
                'VIDEO/LABS/pythonProject/images/Lenna.jpeg', 0))
    im1 = im.astype('float')
    time.sleep(2)
    print(f"¡Imagen convertida correctamente.")
    aux = 0
    while aux == 0:
        print(f"Ahora... ¿Qué desea hacer?")
        print(f"1. Aplicar DCT y ver resultado:")
        print(f"2. Aplicar DCT e IDCT y ver resultado:")
        print(f"3. Pirarme sin hacer nada \U0001F923:")
        resp = input()
        if resp == '1':
            option1(im1)
            print(f"¿Desea cerrar el programa? [y/n]")
            r1 = input()
            while r1 == 'y' or r1 == 'n':
                if r1 == 'y':
                    aux = 1
                    print(f"Volviendo al menú principal...")
                    time.sleep(3)
                    break
                elif r1 == 'n':
                    aux = 0
                    break
        elif resp == '2':
            option2(im1)
            print(f"¿Desea cerrar el programa? [y/n]")
            r2 = input()
            while r2 == 'y' or r2 == 'n':
                if r2 == 'y':
                    print(f"Volviendo al menú principal...")
                    time.sleep(3)
                    break
                elif r2 == 'n':
                    aux = 0
                    break
        elif resp == '3':
            print(f"Me has hecho convertir cosas para nada....\U0001F621")
            print(f"Mandando virus en:")
            i = 1
            while i < 6:
                print("\r"f""+str(6-i)+"", end="")
                i = i + 1
                time.sleep(1)
            break

def option1(image):
    # Realizamos un plot conjunto donde podemos ver las dos imágenes.
    # La imagen de la izquierda es la imagen original (Lenna.jpeg)
    # Y la imágen de la derecha, muestra la DCT de la imagen.
    imF = dct2(image)  # Calculamos la DCT mediante el método dct2 (que calcula la DCT en 2 diensiones al ser una imagen)
    imF = np.log(abs(imF))
    plt.subplot(121), plt.imshow(image, 'gray'), plt.axis('off'), plt.title('Imagen original', size=10)
    plt.subplot(122), plt.imshow(imF), plt.axis('off'), plt.title('DCT de la imagen', size=10)
    plt.show()

def option2(image):
    # Realizamos un plot conjunto donde podemos ver las 3 imágenes.
    # La imagen de la izquierda es la imagen original (Lenna.jpeg)
    # La imágen del centro es la DCT de la imagen original.
    # Y la imagen del centro es la reconstrucción (DCT+IDCT) de las dos imágenes.

    imF = dct2(image)  # Calculamos la DCT mediante el método dct2 (que calcula la DCT en 2 diensiones al ser una imagen)
    im1 = idct2(imF)  # Reconvertimos el array producido por dct2 en una imagen.
    imF = np.log(abs(imF))
    plt.subplot(131), plt.imshow(image, 'gray'), plt.axis('off'), plt.title('Imagen original', size=5)
    plt.subplot(132), plt.imshow(imF), plt.axis('off'), plt.title('DCT de la imagen', size=5)
    plt.subplot(133), plt.imshow(im1, 'gray'), plt.axis('off'), plt.title('Imágen reconstruida (DCT+IDCT)', size=5)
    plt.show()


main()
import main
main.lab1_main()
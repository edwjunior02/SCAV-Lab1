# SCAV-Lab1 de Sistemas de Codificación de Audio y Video.

En la carpeta ```src``` encontraremos todos los scripts ```.py``` que realizan diferentes tareas en este Lab.
Estas tareas son:
```
1. Convertir 3 valores [R,G,B] en 3 valores [Y,U,V].
2. Convertir 3 valores [Y,U,V] en 3 valores [R,G,B].
3. Redimensionar una imagen a una calidad inferior.
4. Comprimir una imagen (por defecto Lenna.jpeg).
5. Implementación de la codificación Run-Length.
6. Aplicación de la DCT e IDCT.
```
Es importante destacar, que en la mayoria de scripts, hemos utilizado un menú de tipo arbol de decisión (como en el ```main.py```)

### EJERCICIO 1: Convertir 3 valores [R,G,B] en 3 valores [Y,U,V]
Para el primer ejercicio ```1. Convertir 3 valores [R,G,B] en 3 valores [Y,U,V].```, hemos implementado un script llamado ```Ex1_RGB_to_YUV.py```.
Este script, al ser un script muy sencillo, no se desarrolla ningún tipo de arbol de decisión o menú recursivo. Simplemente se le pide al usuario que introduzca los valores y comprobando que estene en el rango correcto:
```ruby
print("Por favor, introduce un valor(entre 0 y 255) para el canal R:")
    r = input()
    while float(r)>255:
        print(f"El valor de R introducido no es correcto. Por favor, vuelva a introducir un valor(entre 0 y 255) para el canal R:")
        r = input()
```
El bloque de código anterior, muestra la solicitud de dato al usuario y la correspondiente comprobación de rango.
Podemos destacar también la fórmula utilizada para pasar de espacio de color [RGB] al espacio de color [YUV]:
```
Y = 0.299*R + 0.587*G + 0.114*B
U = 0.493*(B-Y)
V = 0.877*(R-Y)
```

Este seria el resultado de una instancia de este script:

![Captura de pantalla-outputEx1](https://user-images.githubusercontent.com/91899380/143328368-76c1c432-b633-4444-bdd9-a7f073f7da67.png)

### EJERCICIO 2: Convertir 3 valores [Y,U,V] en 3 valores [R,G,B]
En este ejercicio no hay nada mas que añadir. Realizamos lo mismo que en el script anterior pero en un nuevo script llamado ```Ex2_YUV_to_RGB.py```.
Las fórmulas necesarias para estos cálculos son:
```
R = Y + 1.402*(V-128)
G = Y - 0.34414*(U-128)
B = Y + 1.772*(U-128)
```

Resultado de una instancia de este script:

![Captura de pantalla-outputEx2](https://user-images.githubusercontent.com/91899380/143328482-236d7275-f6b7-4c94-b045-d3f4445a58fb.png)

Podemos observar como todas las variables que entren por el usuario, estan sometidas a un control de rangos y coherencia con el script :nerd_face:

## EJERCICIO 3: Redimensionar una imagen.
En este script llamado ```Ex3_Resize_Image.py```, utilizaremos como imagen modelo ```images/2pac.jpeg```.
Lo que vamos a realizar en este script es cambiar las proporciones del archivo para tener una imagen mas pequeña en dimensiones.
En este ejercicio si que hemos usado la herramienta ```ffmpeg``` y el comando utilizado ha sido el siguiente:
```ruby
os.system("ffmpeg -i 2pac.jpeg -vf scale=320:240 2pac_resized.png")
```
```
-i: Le pasamos a ffmpeg el directorio donde tiene que buscar la imagen '2pac.jpeg'. 
-vf scale=320:240: Comando que cambia la resolución y el tamaño de la imagen.
2pac_resized.png: Output de la operación en el mismo directorio que la imagen de entrada.
```
Tenemos que destacar que la imagen pesa mas (aunque las diensiones sean mas pequeñas) debido a que se ha exportado a un formato sin compresión ```.png```.

Output del script:

![Captura de pantalla-outputEx3](https://user-images.githubusercontent.com/91899380/143329116-8ceba4cd-1d21-435b-bd84-a136fb6e34bc.png)
![2pac](https://user-images.githubusercontent.com/91899380/143329260-784870bd-248a-43c0-a2a2-55e6d836441d.jpeg)
![2pac_resized](https://user-images.githubusercontent.com/91899380/143329240-c9c0c471-81e3-463e-94b4-a56cd5399196.png)

### EJERCICIO 4: Comprimir una imagen (por defecto Lenna.jpeg)
Ahora si que vamos a comprimir una imagen para que ocupe  menos espacio.
En este script llamado ```Ex4_Compression_BW.py```, se le pide al usuario un nivel de compresión al que será sometido la imagen ```Lenna.jpeg``` mediante ```ffmpeg```.
Este script tiene unas comprobaciones y unas tareas previas que le facilitan el trabajo a ```ffmpeg``` ya que es vulnerable a cambios de directorios.
Por eso el siguiente bloque de código copia las imágenes necesarias de la carpeta ```images/``` y las copia en el directorio ```src/```, que es desde donde se ejecuta ```ffmpeg```:
```ruby
pathCarpeta = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO/LABS/pythonProject/images")
pathCarpeta2 = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO/LABS/pythonProject/src")

if not os.path.isdir(pathCarpeta):
    print('la primera carpeta no existe')
elif not os.path.isdir(pathCarpeta2):
    print('la segunda carpeta no existe')

contenidos = os.listdir(pathCarpeta)
for elemento in contenidos:
    try:
          if elemento == 'Lenna.jpeg':
                print(f"Copiando {elemento} --> {pathCarpeta2} ... ", end="")
                src = os.path.join(pathCarpeta, elemento)  # origen
                dst = os.path.join(pathCarpeta2, elemento)  # destino
                shutil.copy(src, dst)
                time.sleep(2)
                print("Correcto")
          else:
                continue
    except:
          print("Falló")
          print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")
```
Ahora es donde se llamará a ```ffmpeg``` para que:
```
1. Cambie a escala de grises la imagen.
2. Comprima la imagen con el ratio de compresión pedido al usuario.
```
```ruby
os.system("ffmpeg -i Lenna.jpeg -vf hue=s=0 Lenna_bw.jpeg")
...
os.system("ffmpeg -i Lenna_bw.jpeg -compression_level "+str(c_level)+" Lenna_"+str(float(c_level)/100)+"compress.jpeg")
```
Donde ```c_level``` es la variable que almacena el ratio de compresión introducido por el usuario.
Finalmente, moverá la/s imagen/es creada/s a la carpeta ```images/``` de nuevo.

Resultado de la ejecución de este script:

![Captura de pantalla-Ex4](https://user-images.githubusercontent.com/91899380/143327791-36b335db-4a61-47f2-bbc9-6c2775760734.png)

![Lenna_0 75compress](https://user-images.githubusercontent.com/91899380/143327814-78fa237d-daa7-4158-a709-142ff9aff6de.jpeg) 
![Lenna](https://user-images.githubusercontent.com/91899380/143327815-e72a7772-0d69-4730-b9da-c29279dd2654.jpeg)


### EJERCICIO 5: Implementación de la codificación Run-Length.
En este script llamado ```Ex5_Run_Length.py```, se le pide al usuario una cadena de carácteres (en mauyúscula), para poder extraer la cadena codificada a partir del algoritmo ```run_length```.
En el script se declara una función que calcula la codificación de la secuencia de entrada:
```ruby
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
```
Y posteriormente se printa por pantalla concatenando el carácter y el número de veces que aparece de manera consecutiva, en forma de string.

Resultado de una ejecución de este script:

![Captura de pantalla-Ex5](https://user-images.githubusercontent.com/91899380/143328081-247af913-100c-464a-a171-6ff2789db754.png)


### EJERCICIO 6: Aplicación de la DCT e IDCT
En el ejercicio 6, hemos creado un script llamado ```Ex6_DCT_Coding.py```, que nos ayuda a implementar la ```Discrete Cosine Transfrm (DCT)```
y su inversa ```Inverse Discrete Cousine Transform (IDCT)```.

Para ello, hemos guardado una imagen en escala de grises (```Lenna.jpeg```) en una variable mediante la libreria ```skimage.color -> rgb2gray```
Una vez en escala de grises, ya hemos podido aplicar las transformadas correspondientes.

En este ejercicio se le pide al usuario mediante un menú recursivo, que desea hacer:

![Captura de pantalla - Ex6](https://user-images.githubusercontent.com/91899380/143328141-fb74a097-7dad-4d08-a43a-fa64e6fdbba1.png)

Y el script va calculando, mediante estas dos funciones, lo que el usuario introduzca en el menú:

```ruby
# Calculamos DCT de una imagen(2D).
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# Calculamos la IDCT de una imagen(2D)
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')
```

Este seria el resultado de la implementación de la DCT, por ejemplo:

![Captura de pantalla-Ex6_2](https://user-images.githubusercontent.com/91899380/143328188-af9d6613-0370-457b-88c6-d1b7c0141bcf.png)

### MENÚ PRINCIPAL
Aún no ser obligatorio en este Lab, hemos decidido implementar un menú interactivo para que la experiencia sea mas dinámica y se pueda observar el comportamiento de todos los scripts sin tener que ejecutarlos uno por uno.
El diseño del menú es el siguiente:

![Captura de pantalla- MainMenu](https://user-images.githubusercontent.com/91899380/143328247-e2718a45-01b2-475b-a47d-af5142d55b34.png)

Según la opción a escoger, se ejecutarán unos scripts u otros.
Es importante remarcar, que tanto el menú como todos los scripts tienen "puerta de escape", es decir, se puede salir de la ejecución del programa en cualquier momento.



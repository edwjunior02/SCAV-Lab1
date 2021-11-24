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
El bloque de código anterior, ejemplifica la solicitud de dato al usuario y la correspondiente comprobación de rango.
Podemos destacar también la fórmula utilizada para pasar de espacio de color [RGB] al espacio de color [YUV]:
<img src="https://latex.codecogs.com/gif.latex?Y=0.299*R + 0.587*G + 0.114*B\" />
<img src="https://latex.codecogs.com/gif.latex?U=0.493*(B-Y)\" />
<img src="https://latex.codecogs.com/gif.latex?V=0.877*(R-Y)\" />

### EJERCICIO 2: Convertir 3 valores [Y,U,V] en 3 valores [R,G,B]
En este ejercicio no hay nada mas que añadir. Realizamos lo mismo que en el script anterior pero en un nuevo script llamado ```Ex2_YUV_to_RGB.py```.
Las fórmulas necesarias para estos cálculos son:

<img src="https://latex.codecogs.com/gif.latex?R=Y + 1.402*(V-128)\" />
<img src="https://latex.codecogs.com/gif.latex?G=Y - 0.34414*(U-128) - 0.71414*(V-128)\" />
<img src="https://latex.codecogs.com/gif.latex?B=Y + 1.772*(U-128)\" />

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

### EJERCICIO 4: Comprimir una imagen (por defecto Lenna.jpeg)
Ahora si que vamos a comprimir una imagen para que ocupe  menos espacio.
En este script llamado ```Ex4_Compression_BW.py```, se le pide al usuario un nivel de compresión al que será sometido la imagen ```Lenna.jpeg``` mediante ```ffmpeg```.
Este script tiene unas comprobaciones y unas tareas previas que le facilitan el trabajo a ```ffmpeg``` ya que es vulnerable a cambios de directorios.
Por eso el siguiente bloque de código copia las imágenes necesarias de la carpeta ```images/``` y las copia en el directorio ```src/```, que es desde donde se ejecuta ```ffmpeg````:
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
Y finalmente, moverá la/s imágen/es creada/s a la carpeta ```images/``` de nuevo.

### EJERCICIO 5: Implementación de la codificación Run-Length.

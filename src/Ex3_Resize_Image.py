import os.path
import time
import shutil
def main():

    # Nuestra línea de comando de FFMPEG solo lee imágenes que esten en el mismo directorio que el script en el que se lanze la petición.
    #Para ello, haremos una copia de images/2pac_jpeg y la pasaremos al directorio src/.
    pathCarpeta = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO/LABS/pythonProject/images")
    pathCarpeta2 = ("/Users/edwjunior/Documents/UNIVERSIDAD/4o CURSO/1r TRIMESTRE/SISTEMES DE CODIFICACIÓ D'ÀUDIO I VIDEO/LABS/pythonProject/src")

    if not os.path.isdir(pathCarpeta):
        print('la primera carpeta no existe')
    elif not os.path.isdir(pathCarpeta2):
        print('la segunda carpeta no existe')

    contenidos = os.listdir(pathCarpeta)
    for elemento in contenidos:
        try:
            if elemento == '2pac.jpeg':
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

    print(f"Se han importado los archivos correctamente.")
    time.sleep(2)

    print("Bienvenid@ al Ejercicio 3 del Lab 1 de Sistemas de Codificación de Audio y Video \U0001F47E."
          "\nDe manera muy sencilla vamos a comprimir en una imagen mas pequeña,"
          "una imagen de muestra mas grande.\nEsta imagen de muestra es de nuestro queridísimo 2pac \U0001F918."
          "\nVamos a ello:")
    print(f"\nCargando foto: 2pac.jpeg")
    i = 0
    while i < 10:
        print(f".", end="")
        i = i+1
        time.sleep(0.1)
    print(f"¡Carga completada!")
    print(f"Convirtiendo:")
    i = 0
    while i < 10:
        print(f".", end="")
        i = i+1
        time.sleep(0.1)
    os.system("ffmpeg -i 2pac.jpeg -vf scale=320:240 2pac_resized.png")     #Con este comando, cambiamos el tamaño de la imagen 2pac.jpeg a 320x240 y la guardamos en 2pac_resized.png
    print(f"Imagen transformada correctamente. Ya tenemos a nuestro 2pac en una imagen mas pequeña.")

    # Aqui vamos a pasar los archivos que hemos generado a la carpeta images/
    contenidos = os.listdir(pathCarpeta2)
    for elemento in contenidos:
        try:
            if elemento.endswith(".jpeg") or elemento.endswith(".png"):
                print(f"Moviendo {elemento} --> {pathCarpeta} ... ", end="")
                src = os.path.join(pathCarpeta2, elemento)  # origen
                dst = os.path.join(pathCarpeta, elemento)  # destino
                shutil.move(src, dst)       #Ahora utilizamos move en vez de copy, ya que lo queremos mover de aquí.
                time.sleep(2)
                print("Correcto")
            else:
                continue
        except:
            print("Falló")
            print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")

    time.sleep(2)
    print(f"Se han movido los archivos correctamente.")
    time.sleep(2)
    print(f"Volviendo al menú principal...")
    time.sleep(3)

main()
import main
main.lab1_main()


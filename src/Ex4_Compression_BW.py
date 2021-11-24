
import time
import os.path
import shutil

def main():
      # Nuestra línea de comando de FFMPEG solo lee imágenes que esten en el mismo directorio que el script en el que se lanze la petición.
      # Para ello, haremos una copia de images/2pac_jpeg y la pasaremos al directorio src/.
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

      print(f"Se han importado los archivos correctamente.")
      time.sleep(2)
      print("Bienvenid@ al Ejercicio 4 del Lab 1 de Sistemas de Codificación de Audio y Video \U0001F47E."
            "\n Vamos a comprimir una imagen en blanco y negro manipulando el grado de compresión. "
            "Buscaremos el grado máximo de compresión para ver que resultado obtenemos. Para ello utilzaremos una"
            "imagen jpeg básica de la famosa Lenna :')")

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
      os.system("ffmpeg -i Lenna.jpeg -vf hue=s=0 Lenna_bw.jpeg")
      time.sleep(2)
      print(f"¡Imagen convertida correctamente.")
      print(f"Ahora dinos que ratio de compresión quieres aplicar:")
      c_level = input()
      while float(c_level) > 100 or float(c_level) < 0:
            print("El ratio de compresión introducido no es correcto. Por favor, dinos de nuevo que ratio de compresión quieres aplicar: ")
            c_level =input()
      print("Comprimiendo al "+str(c_level)+" %:")
      i = 0
      while i < 10:
            print(f".", end="")
            i = i + 1
            time.sleep(0.3)
      os.system("ffmpeg -i Lenna_bw.jpeg -compression_level "+str(c_level)+" Lenna_"+str(float(c_level)/100)+"compress.jpeg")
      print(f"¡Imagen comprimida correctamente!")

      # Aqui vamos a pasar los archivos que hemos generado a la carpeta images/
      contenidos = os.listdir(pathCarpeta2)
      for elemento in contenidos:
            try:
                  if elemento.endswith(".jpeg") or elemento.endswith(".png"):
                        print(f"Moviendo {elemento} --> {pathCarpeta} ... ", end="")
                        src = os.path.join(pathCarpeta2, elemento)  # origen
                        dst = os.path.join(pathCarpeta, elemento)  # destino
                        shutil.move(src, dst)  # Ahora utilizamos move en vez de copy, ya que lo queremos mover de aquí.
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










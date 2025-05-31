# Ejercicio de manejo de archivos en Python
with open("archivo.csv","w") as f:
  f.write("Primer Archivo Creado.........")
print("Archivo creado correctamente....")



import os
# Eliminar un archivo si existe
if os.path.exists("archivo.txt"):
  os.remove("archivo.txt")
  print("Archivo elimando")
else:
  print("El archivo no existe")
  


# Creación de un archivo de texto con 1500 líneas
with open("archivo.txt","w") as f:
  for i in  range(1,1500):
    f.write(f"Linea numero : {i} \n")
print("Datos creados correctamente")



# Lectura del archivo de texto
with open("archivo.txt","r") as f:
  linea_num = 1
  for linea in f:
    print(f"linea: {linea_num} : {linea.strip()}")
    linea_num += 1



# Lectura del archivo de texto y guardado en una lista
palabra = "Linea numero : 26 "
with open("archivo.txt","r") as f:
  for linea in f:
    if palabra in linea:
      print(f"encontrado: {linea}")
      
      
#Copiar el contenido de un archivo a otro archivo
with open("archivo.txt","r") as original, open("archivo_copia.txt","w") as copia:
  copia.write("Copia del archivo original \n")
  for linea in original:
    copia.write(linea)
print("Archivo copiado correctamente..............")


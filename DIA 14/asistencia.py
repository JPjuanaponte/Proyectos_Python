import cv2
import face_recognition as fr
import os
import numpy 
from datetime import datetime


# Crear base de datos 


ruta_base = os.path.dirname(__file__)
ruta = os.path.join(ruta_base, 'empleados')
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])
print(nombres_empleados)

# Códificar imagenes

def codificar(imagenes):
    # crear una lista nueva
    lista_codificada = []
    # Pasar todas la imagnes a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    
    # Codificar 
        codificado = fr.face_encodings(imagen)[0]

    # Agregar a lista 
        lista_codificada.append(codificado)

# Devolover lista codificada
    return lista_codificada

# Registrar ingresos de empleados
def registar_ingresos(persona):
    f = open('registro.csv','r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')


lista_empleados_codificada = codificar(mis_imagenes)

# Tomar una imagen de camara web
captura = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# leer imagen de la cámara
exito, imagen = captura.read()

if not exito:
    print('No se podido tomar la captura')
else:
    # reconocer cara en captura
    """
    imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    cara_captura = fr.face_locations(imagen_rgb)
    """
    cara_captura = fr.face_locations(imagen)
    # codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)
    # buscar coincidencias 
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif) # hubo ocincidencia o no 
        distancias = fr.face_distance(lista_empleados_codificada, caracodif) # cuanta distancioa hay enre la coincidencia
        
        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        # Mostrar coincidencias 
        if distancias[indice_coincidencia] > 0.6: 
            print('No coincide con ninguno de nuestros empleados')
        else:
            # Buscar el nombre del empleado encontrado 
            nombre = nombres_empleados[indice_coincidencia]

            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2,y2), (0,255,0), 2)
            cv2.rectangle(imagen, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255),2)

            # Registro de ingreso en el csv
            registar_ingresos(nombre)


            # Mostrar la imagen coincidida
            cv2.imshow('Imagen web', imagen)
            # mantener ventana abierta 
            cv2.waitKey(0)

        



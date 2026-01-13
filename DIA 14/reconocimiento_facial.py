import cv2
import face_recognition as fr

# Cargar imagenes
foto_control = fr.load_image_file('C:/Users/juanp/Desktop/DATA/fotoa.jpg')
foto_prueba = fr.load_image_file('C:/Users/juanp/Desktop/DATA/fotob.jpeg')

# Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB) 
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_A= fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# busca las coordenadas de ubicación del rostro
"""
print(lugar_cara_A)
"""

# Mostrar rectangulo 
cv2.rectangle(foto_control,
            (lugar_cara_A[3],lugar_cara_A[0]),
            (lugar_cara_A[1], lugar_cara_A[2]),
            (0,255,0),
            2)
# mostrarrectangulo foto de prueba

# Localizar cara control
lugar_cara_B= fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# Mostrar rectangulo 
cv2.rectangle(foto_prueba,
            (lugar_cara_B[3],lugar_cara_B[0]),
            (lugar_cara_B[1], lugar_cara_B[2]),
            (236, 152, 170),
            2)

# realizar comparación
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B, 0.7 )   # ceste método compara una lista , tolerancia la final para comparar aqui se modifica a 0.3

print(resultado)

# Medida de la distancia
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
"""print(distancia)"""

# Mostrar resulatdos 
cv2.putText(foto_prueba,
            f'{resultado}{distancia.round(2)}',
            (50,50), # Distancia para que aparezca información en la foto
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (251, 0, 93),
            2)

# Mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# Mantener programa abierto
cv2.waitKey(0) # herramiento de cv2 que necesita quese teclee una tecla especiifca pára cerrar el programa en este caso es 0
from PIL import Image


rutaimagen = input("Ingresa la ruta de la imagen: ")
angulorotacion = int(input("Ingresa el ángulo de rotación (en grados): "))

imagen = Image.open(rutaimagen)

imagenrotada = imagen.rotate(angulorotacion, expand=True)

imagenrotada.show()

nombrearchivo = rutaimagen.split('/')[-1]
nombresinextension, extension = nombrearchivo.split('.')

nuevonombre = f"{nombresinextension}Rot{angulorotacion}.{extension}"

imagenrotada.save(nuevonombre)

print(f"Imagen rotada guardada como {nuevonombre}")
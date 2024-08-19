from PIL import Image

rutaimagen = "img/descarga.webp"
imagen = Image.open(rutaimagen)
imagen.show()

imagen.save("img/copia/imagencopia cristiano.webp")
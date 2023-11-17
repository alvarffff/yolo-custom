import os
from PIL import Image

def obtener_dimensiones_imagenes(directorio):
    # Lista para almacenar los resultados
    resultados = []

    # Recorre los archivos en el directorio
    for i in range(900):
        # Construye el nombre del archivo con el formato especificado
        nombre_archivo = f"{i:05}.ppm"
        ruta_completa = os.path.join(directorio, nombre_archivo)

        # Verifica si el archivo existe
        if os.path.isfile(ruta_completa):
            try:
                # Abre la imagen y obtiene sus dimensiones
                with Image.open(ruta_completa) as img:
                    ancho, alto = img.size
                    # Añade los resultados a la lista
                    resultados.append((nombre_archivo, ancho, alto))
            except IOError:
                print(f"No se pudo abrir la imagen: {nombre_archivo}")

    return resultados




# Ejemplo de uso
# Remplaza 'ruta_a_la_carpeta' con la ruta real a tu carpeta
dimensiones = obtener_dimensiones_imagenes('./FullIJCNN2013')

def normalizar_coordenadas(x_min, y_min, x_max, y_max, ancho_imagen, alto_imagen):
    # Calcula el centro y el tamaño de la ROI
    x_centro = (x_min + x_max) / 2
    y_centro = (y_min + y_max) / 2
    ancho = x_max - x_min
    alto = y_max - y_min

    # Normaliza las coordenadas y el tamaño
    x_centro_normalizado = x_centro / ancho_imagen
    y_centro_normalizado = y_centro / alto_imagen
    ancho_normalizado = ancho / ancho_imagen
    alto_normalizado = alto / alto_imagen

    return x_centro_normalizado, y_centro_normalizado, ancho_normalizado, alto_normalizado

def procesar_anotaciones_para_crear_archivos(archivo_anotaciones, lista_dimensiones):
    # Crear un diccionario para almacenar las anotaciones por imagen
    anotaciones_por_imagen = {}

    # Leer las anotaciones del archivo
    with open(archivo_anotaciones, 'r') as file:
        anotaciones = file.readlines()

    # Agrupar anotaciones por imagen
    for anotacion in anotaciones:
        partes = anotacion.strip().split(';')
        nombre_imagen, x_min, y_min, x_max, y_max, clase_objeto = partes
        nombre_imagen = nombre_imagen.replace('.ppm', '.txt')

        # Buscar las dimensiones de la imagen en la lista
        dimensiones = next((item for item in lista_dimensiones if item[0] == nombre_imagen.replace('.txt', '.ppm')), None)
        if dimensiones:
            # Extrae las dimensiones de la imagen
            _, ancho_imagen, alto_imagen = dimensiones

            # Normaliza las coordenadas y el tamaño del objeto
            x_centro_norm, y_centro_norm, ancho_norm, alto_norm = normalizar_coordenadas(
                int(x_min), int(y_min), int(x_max), int(y_max), ancho_imagen, alto_imagen
            )

            # Agrega la anotación al diccionario
            if nombre_imagen not in anotaciones_por_imagen:
                anotaciones_por_imagen[nombre_imagen] = []
            anotaciones_por_imagen[nombre_imagen].append(f"{clase_objeto} {x_centro_norm} {y_centro_norm} {ancho_norm} {alto_norm}")

    # Crear un archivo .txt por cada imagen con sus anotaciones
    for imagen, anots in anotaciones_por_imagen.items():
        with open(imagen, 'w') as archivo_salida:
            for anot in anots:
                archivo_salida.write(anot + '\n')


# Ejemplo de uso
procesar_anotaciones_para_crear_archivos('./FullIJCNN2013/gt.txt', dimensiones)
# Asegúrate de reemplazar 'ruta/al/archivo/anotaciones.txt' con la ruta real al archivo de anotaciones y 'lista_dimensiones' con la lista obtenida previamente.

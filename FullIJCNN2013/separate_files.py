import os
import shutil

def crear_estructura_carpetas(base_path):
    # Crear las carpetas principales 'images' y 'labels'
    for carpeta_principal in ['images', 'labels']:
        for sub_carpeta in ['test', 'train', 'val']:
            # Crear la ruta de la subcarpeta
            ruta_carpeta = os.path.join(base_path, carpeta_principal, sub_carpeta)
            # Crear la carpeta si no existe
            os.makedirs(ruta_carpeta, exist_ok=True)

def mover_archivos(carpeta_origen, base_path):
    for i in range(900):
        # Construir el nombre del archivo
        nombre_archivo = f"{i:05}"

        # Determinar la subcarpeta de destino
        if i < 560:
            sub_carpeta = 'train'
        elif i < 800:
            sub_carpeta = 'test'
        else:
            sub_carpeta = 'val'

        # Mover los archivos .ppm y .txt a las carpetas correspondientes
        for extension in ['ppm', 'txt']:
            archivo_origen = os.path.join(carpeta_origen, f"{nombre_archivo}.{extension}")
            if os.path.exists(archivo_origen):
                archivo_destino = os.path.join(base_path, 'images' if extension == 'ppm' else 'labels', sub_carpeta, f"{nombre_archivo}.{extension}")
                shutil.move(archivo_origen, archivo_destino)

# Ejemplo de uso:
base_path = ''
carpeta_origen = ''
crear_estructura_carpetas(base_path)
mover_archivos(carpeta_origen, base_path)

# Nota: Asegúrate de reemplazar 'ruta/a/la/carpeta/base' con la ruta de la carpeta donde quieres crear la estructura de carpetas y 'ruta/a/la/carpeta/con/los/archivos' con la carpeta donde están los archivos .ppm y .txt originales.

import os

# Definir los directorios base para imágenes y etiquetas
base_image_dir = 'images'
base_label_dir = 'labels'

# Definir las subcarpetas
subfolders = ['test', 'train', 'val']

# Función para obtener el nombre del archivo sin la extensión
def get_filename_without_extension(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

# Recorrer cada subcarpeta
for folder in subfolders:
    image_folder_path = os.path.join(base_image_dir, folder)
    label_folder_path = os.path.join(base_label_dir, folder)

    # Obtener la lista de nombres de archivos de imágenes y etiquetas
    image_files = os.listdir(image_folder_path)
    label_files = os.listdir(label_folder_path)

    # Convertir los nombres de los archivos de etiquetas a nombres base (sin extensión)
    label_names = {get_filename_without_extension(file) for file in label_files}

    # Recorrer los archivos de imágenes y verificar si existe una etiqueta correspondiente
    for image_file in image_files:
        image_name = get_filename_without_extension(image_file)
        
        # Si no existe un archivo de etiqueta correspondiente, eliminar la imagen
        if image_name not in label_names:
            image_path = os.path.join(image_folder_path, image_file)
            print(f"Eliminando imagen sin etiqueta: {image_path}")
            os.remove(image_path)

print("Limpieza completada.")
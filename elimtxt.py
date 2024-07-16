import os
#Script so it is easier to try the script
#Executing this script will delete all the .txt files in the current folder

current_directory = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(current_directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(current_directory, filename)
        try:
            os.remove(file_path)
            print(f'Archivo eliminado: {file_path}')
        except Exception as e:
            print(f'Error al eliminar el archivo {file_path}: {e}')

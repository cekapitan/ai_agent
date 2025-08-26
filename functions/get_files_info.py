# get_files_info.py

import os


def get_files_info(working_directory, directory="."):


    if isinstance(directory, str) == False:
        raise ValueError(f'Error: "{directory}" is not a directory')
    
    path =os.path.join(working_directory, directory)
    if not os.path.exists(path):
        raise ValueError(f'Error: "{path}" does not exist')
    
    if not os.path.isdir(path):
        raise ValueError(f'Error: "{path}" is not a directory')
    
    files = os.listdir(path)

    file_info = []
    for file in files:
        file_path = os.path.join(path, file)
        file_size = os.path.getsize(file_path)
        is_dir = os.path.isdir(file_path)
        file_info.append(f"{file}: file_size={file_size} bytes, is_dir={is_dir}")

    return file_info

# Result for current directory:
#  - main.py: file_size=576 bytes, is_dir=False
#  - tests.py: file_size=1343 bytes, is_dir=False
#  - pkg: file_size=92 bytes, is_dir=True

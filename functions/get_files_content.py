

error = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
more_err = f'Error: File not found or is not a regular file: "{file_path}"'

large = [...File "{file_path}" truncated at 10000 characters]




def get_file_content(working_directory, file_path):
MAX_CHARS = 10000

with open(file_path, "r") as f:
    file_content_string = f.read(MAX_CHARS)

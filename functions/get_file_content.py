import os

def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory, file_path))
    full_path = os.path.abspath(target_dir)
    MAX_CHARS = 10000
        # Ensure full_path is inside working_directory
    if not os.path.commonpath([working_directory, full_path]) == working_directory:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # Is it even a file?
    if not os.path.isfile(full_path):
        return f'Error: "{file_path}" is not a file'

    try:
        with open(full_path, "r") as f:
            content = f.read(MAX_CHARS)

    # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except  Exception as e:
        return f"Error: {e}"

    return content
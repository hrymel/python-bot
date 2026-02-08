import os

def write_file(working_directory, file_path, content):
    working_directory = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(working_directory, file_path))
    full_path = os.path.abspath(target_path)

    # Ensure full_path is inside working_directory
    if os.path.commonpath([working_directory, full_path]) != working_directory:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # If the path points to a directory, error
    if os.path.isdir(full_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    try:
        parent_dir = os.path.dirname(full_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        with open(full_path, "w") as f:
            f.write(content)

    except Exception as e:
        return f"Error: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
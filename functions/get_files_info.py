import os

def get_files_info(working_directory, directory="."):
    working_directory = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory, directory))
    full_path = os.path.abspath(target_dir)

    # Ensure full_path is inside working_directory
    if not os.path.commonpath([working_directory, full_path]) == working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Is it even a directory?
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    lines = []
    for entry in os.listdir(full_path):
        entry_path = os.path.join(full_path, entry)
        try:
            size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
        except Exception as e:
            return f"Error: {e}"

        line = f"- {entry}: file_size={size} bytes, is_dir={is_dir}"
        lines.append(line)

    return "\n".join(lines)
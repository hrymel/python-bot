import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=(
        "Writes text content to a file relative to the working directory, creating "
        "any missing parent directories if needed. Overwrites the file if it already exists."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
                    'Path to the file to write to, relative to the working directory '
                    '(e.g., "notes.txt" or "pkg/output/result.txt").'
                ),
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

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
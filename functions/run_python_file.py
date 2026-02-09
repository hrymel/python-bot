import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=(
        "Executes a Python file relative to the working directory in a subprocess, "
        "optionally passing command-line arguments, and returns captured stdout/stderr "
        "or error information."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=(
                    'Path to the Python file to execute, relative to the working directory '
                    '(e.g., "script.py" or "tools/run_task.py").'
                ),
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description=(
                    "Optional list of command-line arguments to pass to the Python file "
                    '(e.g., ["--verbose", "input.txt"]).'
                ),
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_directory, file_path))
        full_path = os.path.abspath(target_path)

        # Ensure full_path is inside working_directory
        if os.path.commonpath([working_directory, full_path]) != working_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", full_path]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30,
        )

        parts = []

        if result.returncode != 0:
            parts.append(f"Process exited with code {result.returncode}")

        stdout = (result.stdout or "").strip()
        stderr = (result.stderr or "").strip()

        if not stdout and not stderr:
            parts.append("No output produced")
        else:
            if stdout:
                parts.append(f"STDOUT: {stdout}")
            if stderr:
                parts.append(f"STDERR: {stderr}")

        return "\n".join(parts)

    except Exception as e:
    	return f"Error: executing Python file: {e}"
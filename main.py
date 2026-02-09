import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
MAX_ITEMS = 20


def main():
    if len(sys.argv) < 2:
        print("Error: No prompt provided. Usage: uv run main.py 'your prompt here'")
        sys.exit(1)

    verbose = "--verbose" in sys.argv

    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    for _ in range(MAX_ITEMS):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
            ),
        )

        for candidate in response.candidates:
            messages.append(candidate.content)

        function_results_parts = []

        func_calls = response.function_calls or []

        if not func_calls:
            final_text = response.text
            break

        function_results_parts = []

        # === PHASE 1: CALL FUNCTIONS ===
        for func_call in func_calls:
            function_call_result = call_function(func_call)

            if not function_call_result.parts:
                raise Exception("Error: function_call_result.parts is empty")

            first_part = function_call_result.parts[0]

            if first_part.function_response is None:
                raise Exception("Error: function_response is None")

            if first_part.function_response.response is None:
                raise Exception("Error: function_response.response is None")

            function_results_parts.append(first_part)
            messages.append(types.Content(role="user", parts=function_results_parts))

    # === PHASE 2: PRINT OUTPUT ===
    if verbose:
        print("User prompt:", prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if function_results_parts:
        for part in function_results_parts:
            if verbose:
                print("Function response:")
            print(part.function_response.response)
    else:
        print("Response:")
        print(response.text)


    
    

if __name__ == "__main__":
    main()

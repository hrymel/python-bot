import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



def main():
    if len(sys.argv) < 2:
        print("Error: No prompt provided. Usage: uv run main.py 'your prompt here'")
        sys.exit(1)


    # Join all arguments (so multi-word prompts work without extra quotes)
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )


    if "--verbose" in sys.argv:
        print("User prompt:", prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    
    print("Response:")
    print(response.text)



    
    

if __name__ == "__main__":
    main()

import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set")
        sys.exit(1)
    
    client = genai.Client(api_key=api_key)
    
    # Get prompt from command line arguments
    if len(sys.argv) < 2:
        print("Usage: python main.py <your_prompt> [--verbose]")
        print("Example: python main.py 'Why is Boot.dev such a great place to learn backend development?' --verbose")
        sys.exit(1)
    
    # Check if --verbose flag is present
    verbose = False
    args = sys.argv[1:]
    
    if "--verbose" in args:
        verbose = True
        # Remove --verbose from arguments
        args.remove("--verbose")
    
    # Join remaining arguments to form the prompt
    prompt = " ".join(args)
    
    # Show verbose output if flag is set
    if verbose:
        print(f"User prompt: {prompt}")
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    
    try:
        model = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
        )
        
        print(model.text)
        
        # Show token information only in verbose mode
        if verbose:
            print(f"Prompt tokens: {model.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {model.usage_metadata.candidates_token_count}")
        
    except Exception as e:
        print(f"Error generating content: {e}")
        sys.exit(1)
        

if __name__ == "__main__":
    main()

"""
Library with Gemini solutions as functions
"""

from google import genai
from google.genai import types

# Initialize the Gemini client
client = genai.Client()

# Build a function to generate a solution for a given question using the Gemini API
def generate_solution(question: str) -> str:
    """
    Generate a solution for a given question using the Gemini API.

    Args:
        question (str): The question to generate a solution for.

    Returns:
        str: The generated solution.
    """
    # Create a chat request
    chat = client.chats.create(model='gemini-3.6-flash')

    # Generate the solution
    response = chat.send_message(question)

    # Return the generated solution
    return response.text

# Build a function to generate code from a given prompt using the Gemini API
def generate_code(prompt: str) -> str:
    """
    Generate code from a given prompt using the Gemini API.

    Args:
        prompt (str): The prompt to generate code from.

    Returns:
        str: The generated code.
    """
    # Define a system instruction for the Gemini model to generate code
    system_instruction = (
        "Eres un Ingeniero de Software Senior experto en Python. "
        "Tu única tarea es generar código de Python limpio, optimizado y que siga las normas PEP 8. "
        "No incluyas explicaciones textuales, introducciones ni conclusiones. "
        "Devuelve exclusivamente el bloque de código dentro de marcas de formato triple acento grave (```python)."
    )

    # 2. Configure the content generation parameters
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.2 
    )

    # Create a chat request
    chat = client.chats.create(model='gemini-3.6-flash', config=config)

    # Generate the code
    response = chat.send_message(prompt)

    # Return the generated code
    return response.text
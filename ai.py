"""
This module provides functions to interact with the 
Gemini AI model using the google.generativeai library.
It includes functions to retrieve the API key, configure
the model, start a chat session, and send prompts to the AI model.

Functions:
    get_gemini_api_key(): Retrieves the Gemini API key from the environment variables.
    get_ai_response(prompt): Sends a prompt to the AI model and retrieves the response.
    ai_startup(): Reads the initial prompt from a file and sends it to the AI model.
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

def get_gemini_api_key():
    """
    Retrieves the Gemini API key from the environment variables.

    Raises:
        ValueError: If the GEMINI_API_KEY environment variable is not set.

    Returns:
        str: The Gemini API key.
    """
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("No Gemini API key found. Please set the GEMINI_API_KEY variable.")
    return api_key

genai.configure(api_key=get_gemini_api_key())
with open("optimal_prompt.txt", "r", encoding="utf-8") as pprompt:
    model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest', system_instruction=pprompt.read())
chat = model.start_chat(history=[])

def get_ai_response(prompt):
    """
    Sends a prompt to the AI model and retrieves the response.

    Args:
        prompt (str): The prompt to send to the AI model.

    Returns:
        str: The response from the AI model, or an error message if an exception occurs.
    """
    try:
        response = chat.send_message(prompt)
        return response
    except Exception as e:
        print(f"Error getting response from Gemini: {e}")
        return "Sorry, I encountered an error processing your request."

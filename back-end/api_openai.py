from openai import OpenAI
import os
from prep_data import prep_data_f

def chat_with_llm(query, messages, system):
    """
    query: nouvelle question de l'utilisateur
    messages: historique des messages avec l'utilisateur
    system: prompt système du llm
    """

    KEY = os.getenv("API_KEY_OPENAI")
    client = OpenAI(api_key=KEY)

    # prep_data_f est une fonction qui permet de préparer vos données à envoyer à l'API
    # Vous allez devoir coder ici l'appel de l'API de OpenAI
    # Utilisez le modèle "gpt-3.5-turbo"

    for chunk in response:
        if chunk.choices[0].delta.content != None:
            yield chunk.choices[0].delta.content
        else:
            return "/s"
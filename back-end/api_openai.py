from openai import OpenAI
import os

def chat_with_llm(query, messages, system):
    """
    query: nouvelle question de l'utilisateur
    messages: historique des messages avec l'utilisateur
    system: prompt système du llm
    """

    KEY = os.getenv("API_KEY_OPENAI")
    client = OpenAI(api_key=KEY)
    new_list_messages = []
    i = 0
    for content in messages:
        role = "assistant"
        if i % 2 == 0:
            role = "user"
        obj = {"role": role, "content": content}
        new_list_messages.append(obj)
        i += 1
    query_obj = {"role": "user", "content": query}
    system_obj = {"role": "system", "content": system}
    new_list_messages.insert(0, system_obj)
    new_list_messages.append(query_obj)

    response = client.chat.completions.create(
        stream=True,
        model="gpt-3.5-turbo",
        temperature=0,
        messages=new_list_messages
    )

    for chunk in response:
        if chunk.choices[0].delta.content != None:
            yield chunk.choices[0].delta.content
        else:
            return "/s"
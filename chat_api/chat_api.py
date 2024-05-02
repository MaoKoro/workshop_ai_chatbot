import requests
import os
import time

PROMPT_SYSTEM="..."

def main():
    while True:
        query = input("> ")
        
        historiqueDeLaConversation = ["hello", "hey"]
        promptSystem = PROMPT_SYSTEM  
        print(promptSystem)
        
        body = {'query': query, 'messages': historiqueDeLaConversation, 'system': promptSystem}
        historiqueDeLaConversation.append(query)
        
        url = 'http://0.0.0.0:8000/conversation'
        resp = bytes()
        response = requests.post(url, json=body, stream=True)
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                print(chunk.decode('utf-8'), end="")
                resp += chunk
        historiqueDeLaConversation.append(resp)

if __name__ == "__main__":
    main()

import requests
import json


HOSTURL = "http://localhost:1234"

COMPLETIONURL = "/v1/chat/completions"

CHATBODY = {
    "model": "qwen2.5-coder-3b-instruct",
    "messages": [],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": False,
}


def callChatbot(message):
    CHATBODY["messages"] = message
    response = requests.post(HOSTURL + COMPLETIONURL, json=CHATBODY)
    respJsonData = response.json()
    chatResponses = []
    for choice in respJsonData["choices"]:
        chatResponses.append(choice["message"])
    return chatResponses

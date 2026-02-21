# README: Local LLM Integration with Python

This documentation explains the implementation of a local Large Language Model (LLM) interface using the `requests` library to interact with an OpenAI-compatible API (such as LM Studio)

---

## Core Learning Objectives

The provided script demonstrates three fundamental concepts in modern AI development:

### 1. Interacting with OpenAI-Compatible APIs

Most local LLM runners mimic the OpenAI API structure. This allows developers to swap a cloud provider (like OpenAI) for a local provider by simply changing the `base_url`.

* **Endpoint:** `/v1/chat/completions` is the standard route for chat-based interactions.
* **Method:** `POST` requests are used to send the payload (JSON) to the model.

### 2. Anatomy of a Chat Request

The `CHATBODY` dictionary defines how the model behaves:

* **Model:** `qwen2.5-coder-3b-instruct` specifies the specific weights being queried.
* **Messages:** An array that stores the conversation history.
* **Temperature:** Controls randomness. **0.7** provides a balance between creative and deterministic outputs.
* **Max Tokens:** Set to **-1** to allow the model to generate until it naturally stops or hits the hardware limit.

### 3. Response Parsing

The script demonstrates how to navigate the nested JSON response returned by the server:

1. Access the `choices` list.
2. Extract the `message` object (containing `role` and `content`).
3. Store these in a list for the application to use.

---

## Implementation Details

### Function: `callChatbot(message)`

This function acts as the bridge between the user and the model.

1. **Input:** Accepts a list of message objects: `[{"role": "user", "content": "..."}]`.
2. **Processing:** Updates the global `CHATBODY` and sends it via `requests.post`.
3. **Extraction:** Iterates through the API response to retrieve the generated text.

```python
def callChatbot(message):
    CHATBODY["messages"] = message
    response = requests.post(HOSTURL + COMPLETIONURL, json=CHATBODY)
    respJsonData = response.json()
    chatResponses = []
    for choice in respJsonData["choices"]:
        chatResponses.append(choice["message"])
    return chatResponses

```

---

## Technical Requirements

* **Python 3.x**
* **Library:** `requests` (`pip install requests`)
* **Local Server:** A running instance ( LM Studio) at `http://localhost:1234`.

---
 
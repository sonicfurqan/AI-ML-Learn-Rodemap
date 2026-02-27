from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import streamlit as st
from langchain.tools import tool
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


# from phoenix.otel import register

# # loging service
# tracer_provider = register(project_name="rag-pdf-chat", auto_instrument=True)

if "messages" not in st.session_state:
    st.session_state.messages = []


# load embading model
embeddings = OpenAIEmbeddings(
    base_url="http://127.0.0.1:1234/v1/",  # Replace with your LM Studio server URL/port
    api_key="lm-studio",
    check_embedding_ctx_length=False,
)

# load vector database
vector_store = Chroma(
    collection_name="pdfStore",
    embedding_function=embeddings,
    persist_directory="./DB/chroma_langchain_db",
)


# load gpt model
model = init_chat_model(
    model="qwen2.5-coder-3b-instruct",  # e.g. "gpt-3.5-turbo" or "lmstudio-llama2"
    model_provider="openai",  # because LM Studio mimics OpenAI's API
    base_url="http://127.0.0.1:1234/v1/",
    api_key="lm-studio",  # LM Studio accepts any string here
)


# Cretaing tool with decorator @tool and adding Doc string bellow method declaration. this is important info that defines what funtion does
@tool(response_format="content_and_artifact")
def retrieve_context(query):
    """Searches the internal knowledge base to retrieve salesforce technical documents
    and context. Use this tool when the user asks questions that require
    specific information not present in the chat history, such as facts,
    stored procedures, or company-specific data."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


tools = [retrieve_context]
# If desired, specify custom instructions
prompt = (
    "You are a helpful assistant equipped with a specialized search tool. "
    "Your primary goal is to provide accurate answers by following these steps:\n"
    "1. Analyze the user's request. and check if tools can retive the required information.\n"
    "2. If the tool returns information, synthesize it to answer the user clearly.\n"
    "3. Always cite your sources based on the 'Source' metadata provided by the tool.\n"
    "4. If the retrieved context doesn't contain the answer, state that you don't have enough information."
)
agent = create_agent(model, tools, system_prompt=prompt)


def askAgent(userQuery):
    response = agent.invoke({"messages": [{"role": "user", "content": userQuery}]})
    response
    for msg in response["messages"]:
        st.session_state["messages"].append(
            {"role": "assistant", "content": msg.content}
        )
        with st.chat_message("assistant"):
            st.markdown(msg.content)


userQuery = st.chat_input("Enter your message")
if prompt:
    st.session_state["messages"].append({"role": "user", "content": userQuery})
    with st.chat_message("user"):
        st.markdown(userQuery)
        askAgent(userQuery)

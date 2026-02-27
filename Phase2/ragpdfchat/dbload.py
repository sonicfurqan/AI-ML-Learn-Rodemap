# load data in vector database from pdf files

from pypdf import PdfReader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4
# load db

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

# load file
folderPath = Path("./Files")
documents = []
for fileslink in folderPath.iterdir():
    if fileslink.is_file() and fileslink.suffix == ".pdf":
        reader = PdfReader(fileslink)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                documents.append(
                    Document(
                        page_content=text,
                        metadata={"page": i + 1, "source": str(fileslink)},
                    )
                )


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=200,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)
all_splits = text_splitter.split_documents(documents)

print(f"Split pdf  into {len(all_splits)} sub-documents.")
uuids = [str(uuid4()) for _ in range(len(documents))]
vector_store.add_documents(documents=all_splits)


# Check insert
results = vector_store.similarity_search(
    "Apex Limits",
    k=2,
)
for res in results:
    print(f"* {res.page_content} [{res.metadata}]")

import streamlit as st
import fitz
import chromadb
import re

# load/initiate client
client = chromadb.PersistentClient(path="./DB")


col1, col2 = st.columns([4, 1], vertical_alignment="center")
container = st.container(border=True)


if "filename" not in st.session_state:
    st.session_state["filename"] = ""

if "messages" not in st.session_state:
    st.session_state.messages = []


def createFileDatabase(fileName, textlist):
    collectionName = fileName.replace(" ", "_").replace(".pdf", "")
    collection = client.get_or_create_collection(name=collectionName)
    st.session_state["filename"] = collectionName
    print("collection name", collectionName)

    # Create the fixed container
    with container:
        st.markdown("**Ingestion Status**")
        # Create a placeholder for continuous updates
        status_text = st.empty()
        progress_bar = st.progress(0)

    for i, data in enumerate(textlist):
        collection.add(
            documents=[data["text"]],
            metadatas=[{"page": data["page"], "paragraph": data["paragraph"]}],
            ids=[f"id_{data['page']}_{data['paragraph']}"],
        )
        # Update the SAME line of text continuously
        status_text.text(
            f"Processing: Page {data['page']}, Paragraph {data['paragraph']}"
        )

        # Update progress bar
        progress_bar.progress((i + 1) / len(textlist))


def searchQuery():
    if st.session_state["filename"] != "":
        with st.status("Checking"):
            collection = client.get_or_create_collection(
                name=st.session_state["filename"]
            )
            results = collection.query(
                query_texts=[prompt],  # Chroma will embed this for you
                n_results=2,  # how many results to return
            )

            msg = []
            for metadata, res in zip(results["metadatas"], results["documents"]):
                for meta, text in zip(metadata, res):
                    msg.append(
                        {
                            "role": "assistant",
                            "content": f"{text} - Found on page {meta['page']} paragraph {meta['paragraph']}",
                        }
                    )
            for m in msg:
                with st.chat_message(m["role"]):
                    st.markdown(m["content"])
            st.session_state["messages"].extend(msg)


def onFileUpload():
    data = st.session_state["file_upload_widget"]
    if data is None:
        print("file cleared")
        return
    fileName = data.name
    print(fileName)

    fileData = data.read()
    doc = fitz.open(stream=fileData, filetype="pdf")

    documents = []
    for index, page in enumerate(doc):  # iterate through the doc:
        # Split text into sentences using regex (handles . ! ?)
        page_sentences = re.split(
            r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s", page.get_text("text")
        )
        for i, sentence in enumerate(page_sentences):
            documents.append({"text": sentence, "page": index + 1, "paragraph": i + 1})

    createFileDatabase(fileName, documents)


def refreshChat():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


# build UI

with col1:
    colList = client.list_collections()

    names = [col.name for col in colList]

    st.selectbox(
        "Select exsisting PDF Database?",
        (names),
        key="existingDB",
    )
    collectionStatusText = st.empty()

with col2:
    loadTable = st.button("Load", type="primary")
    if st.session_state["existingDB"] is not None and loadTable:
        collection = client.get_or_create_collection(
            name=st.session_state["existingDB"]
        )
        collectionStatusText.write(f" Lines in collection {collection.count()}")
        st.session_state["filename"] = st.session_state["existingDB"]

with container:
    st.file_uploader(
        "Load New PDF",
        on_change=onFileUpload,
        key="file_upload_widget",
        type=["pdf"],
        accept_multiple_files=False,
        label_visibility="visible",
        width="stretch",
    )


with container:
    st.title("Search text in PDF")
    prompt = st.chat_input("Enter your message")
    if prompt:
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        searchQuery()

if __name__ == "__main__":
    pass

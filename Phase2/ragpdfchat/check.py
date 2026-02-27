import chromadb

client = chromadb.PersistentClient(path="./DB/chroma_langchain_db")

collection = client.get_or_create_collection(name="pdfStore")
print(f" Lines in collection {collection.count()}")


client.delete_collection(name="pdfStore")
# delete and check again
collection = client.get_or_create_collection(name="pdfStore")
print(f" Lines in collection {collection.count()}")

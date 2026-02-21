 

 

### 1. Embedding (Dense Vector) 🧠

An **Embedding** model turns a piece of text into a long list of numbers called a **Dense Vector**.

* **How it works:** It captures the **semantic meaning** (the "vibe") of the text. Instead of looking for exact words, it looks for concepts. For example, the embeddings for "king" and "queen" will be mathematically close to each other in vector space.
* **How to use it:** You pass your documents through an embedding model (like `text-embedding-3`) and store those numbers in a **Vector Database**. When a user asks a question, you embed the question and ask the database to find the "nearest neighbors."

### 2. Sparse Encoder 🕸️

A **Sparse Encoder** (like **BM25** or **SPLADE**) focuses on specific **keywords** and their importance.

* **How it works:** Unlike dense embeddings, most values in a sparse vector are zero. It excels at finding exact matches, technical terms, or rare words (like "iPhone 15 Pro Max" or a specific serial number) that a dense embedding might generalize too much.
* **How to use it:** It is often used alongside dense embeddings in a **Hybrid Search** setup. You search your index using both methods to ensure you get both the conceptual meaning and the specific keyword accuracy.

### 3. Reranker ⚖️

A **Reranker** is a high-precision model used at the very end of the search process.

* **How it works:** While Embeddings are fast but sometimes "blurry," a Reranker (Cross-Encoder) looks at the user's query and a specific document side-by-side to give a relevancy score. It is too slow to search millions of documents, so it only looks at the top 20–50 results found by the first two methods.
* **How to use it:** After you get your initial results from your Vector/Sparse search, you send those top results to the Reranker. It re-orders them so the absolute best answer moves to the #1 spot.

---
 
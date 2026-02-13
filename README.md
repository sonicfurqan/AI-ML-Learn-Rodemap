# Local AI Development Roadmap: From Data to Agents

## 📖 Summary
This repository contains a comprehensive, step-by-step roadmap for building Local AI applications. The curriculum is designed to take you from a basic environment setup to deploying complex, autonomous agents.

The project is divided into four distinct phases:
1.  **Data & UI:** Mastering Streamlit for data visualization and basic logic.
2.  **RAG (Retrieval-Augmented Generation):** Building local chatbots that can "read" your documents using Vector Databases.
3.  **Agents:** Creating AI agents that can use tools and query databases via the Model Context Protocol (MCP).
4.  **Ops:** Evaluating model faithfulness and monitoring performance metrics.

---

## 🛠️ Tech Stack
* **UI/Frontend:** Streamlit, Chainlit
* **Data Manipulation:** Pandas, NumPy
* **AI/LLM:** LM Studio (Local Inference), OpenAI (API format), Sentence-Transformers
* **Vector DB:** ChromaDB
* **Orchestration:** LangChain
* **Evaluation:** Ragas

---

## 🗺️ Phase 1: Data Engineering & UI Setup
**Goal:** Establish a development environment and build interactive data applications using Streamlit.

| ID | Task Name | Detailed Steps (The "How") | Definition of Done | Reference |
| :--- | :--- | :--- | :--- | :--- |
| **1.1** | **Env & UI Setup** | Install `streamlit`, `pandas`, `openai`. Create `app.py`. Set `openai.api_base = "http://localhost:1234/v1"` in your code. | App runs and prints "Connected to Local LLM" on the screen. | [Link](https://lmstudio.ai/docs/welcome) |
| **1.2** | **Logic UI: Calculator** | Build a Streamlit app with 2 inputs and a "Calculate" button. Handle logic in Python, show result in UI. | You can add/subtract numbers in the browser without errors. | [Link](https://docs.streamlit.io/library/api-reference/widgets) |
| **1.3** | **State: To-Do List** | Use `st.session_state` to store tasks. Save to `todos.json` on every change so data persists on reload. | Closing the browser and reopening it shows your old tasks. | [Link](https://docs.streamlit.io/library/api-reference/session-state) |
| **1.4** | **Pandas: Load CSV and Cleaning** | Create juypter book to load and then clean data. | Plot graphs using clean data. | [Link](https://www.kaggle.com/learn/data-cleaning) |
| **1.5** | **Capstone: Price UI** | Train Linear Regression on "Area" vs "Price". Create UI input for "Area". Predict Price. | You type "5000 sqft" -> App shows "Predicted: $850k". | [Link](https://medium.com/data-science/linear-regression-on-housing-csv-data-kaggle-10b0edc550ed) |

### Bonus 
- Complete tasks in Bonus ML Projects for better undersanding of ML Learning types and  Models
---

## 🧠 Phase 2: RAG (Retrieval Augmented Generation)
**Goal:** Connect your local LLM to private data sources (PDFs) using vector embeddings.

| ID | Task Name | Detailed Steps (The "How") | Definition of Done | Reference |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | **Local Chatbot UI** | Connect `st.chat_input` to LM Studio. Send user text to `http://localhost:1234/v1`. Stream response. | You say "Hi", Local Llama replies "Hello!" in the UI. | [Link](https://blog.streamlit.io/how-to-build-an-llm-powered-app-from-scratch/) |
| **2.2** | **Embedding Test** | Install `sentence-transformers` (runs locally). Turn user text into a vector list `[0.1, 0.4...]`. | You type a word, and the app shows a list of numbers (the vector). | [Link](https://sbert.net/) |
| **2.3** | **Vector DB Setup** | Install `chromadb`. Create a persistent client. Create a collection named "my_docs". | Code runs without error and creates a `chroma` folder locally. | [Link](https://docs.trychroma.com/getting-started) |
| **2.4** | **PDF Ingestion** | Upload PDF in UI. Extract text. Chunk it (500 chars). Store in ChromaDB. | Upload PDF -> Success Message "Stored 50 chunks". | [Link](https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf) |
| **2.5** | **Capstone: PDF Chat** | 1. User asks Q.<br>2. Search ChromaDB.<br>3. Send Top 3 chunks + Q to LM Studio.<br>4. Show Answer. | Asking "What is the 1st amendment?" gives the exact text from the PDF. | [Link](https://python.langchain.com/docs/use_cases/question_answering/local_retrieval_qa) |

---

## 🤖 Phase 3: Agents & Tool Use
**Goal:** Build autonomous agents capable of using tools and executing SQL queries via MCP.

| ID | Task Name | Detailed Steps (The "How") | Definition of Done | Reference |
| :--- | :--- | :--- | :--- | :--- |
| **3.1** | **Tool Definition** | Define `get_weather(city)` in Python. Create a JSON schema for it (OpenAI format). | You have a Python dictionary describing the tool parameters. | [Link](https://platform.openai.com/docs/guides/function-calling) |
| **3.2** | **Chainlit Setup** | Install `chainlit`. Create `app.py`. Run `chainlit run app.py`. | A ChatGPT-like UI opens in your browser (Dark mode!). | [Link](https://docs.chainlit.io/get-started/pure-python) |
| **3.3** | **Local Tool Call** | Send "What's the weather?" to LM Studio. Catch the `tool_calls` response. Execute Python function. | Agent says: "Calling Tool..." -> "It is 25°C". | [Link](https://github.com/ollama/ollama/blob/main/docs/api.md#tool-calls) |
| **3.4** | **MCP Server** | Use `fastmcp` to build a server. Create tool `read_query(sql)`. Connect to SQLite. | Running the server command shows "MCP Server Listening". | [Link](https://github.com/jlowin/fastmcp) |
| **3.5** | **Capstone: SQL Agent** | Connect Chainlit UI to MCP Server. User asks "Top selling tracks?". Agent writes SQL and runs it. | You ask plain English Qs about music sales and get real data back. | [Link](https://python.langchain.com/docs/use_cases/sql/quickstart) |

---

## 📊 Phase 4: LLMOps & Evaluation
**Goal:** Ensure your application is reliable, accurate, and efficient.

| ID | Task Name | Detailed Steps (The "How") | Definition of Done | Reference |
| :--- | :--- | :--- | :--- | :--- |
| **4.1** | **Eval: Faithfulness** | Use `ragas`. Generate 10 Q&A pairs from your PDF. Score your Local RAG pipeline. | You get a score (e.g., 0.85) for how accurate your RAG is. | [Link](https://docs.ragas.io/en/stable/) |
| **4.2** | **Ops: Cost/Speed** | Measure time (start - end) for every query. Count tokens (approx 0.75 words = 1 token). | UI shows: "Latency: 2.4s \| Tokens: 150" after every message. | [Link](https://github.com/openai/tiktoken) |
# STREAMLIT TODO APPLICATION ARCHITECTURE

---

## PERSISTENCE LAYER

The application utilizes the `json` library to manage the data lifecycle between volatile memory and disk storage.

### ToDoStorage Class

* **`storeData`**: Serializes the Python list to `todolist.json` using `json.dump`.
* **`loadData`**: Deserializes the JSON file back into a Python list. Implements `try-except` to prevent crashes if the file does not exist on the first run.

---

## STATE MANAGEMENT (`st.session_state`)

Streamlit operates on a top-down execution model where the script reruns on every interaction. `st.session_state` is the mechanism used to preserve data across these cycles.

* **Input Handling**: The `key="task_input_ele"` parameter binds the text input directly to the session state.
* **List Retention**: The `todolist` is stored in the session state to ensure tasks remain visible while buttons are clicked.

---

## CALLBACK LOGIC

Event-driven programming is handled via the `on_click` parameter. These functions execute logic before the UI is redrawn.

| Function | Logic |
| --- | --- |
| **`ontaskAdd`** | Appends a dictionary (task value + ID) to the list, clears the input buffer, and updates the JSON file. |
| **`ontaskDelete`** | Filters the session list to exclude a specific `taskId` using list comprehension and updates the JSON file. |

---

## SYSTEM FLOW

1. **Initialization**: The `main()` function triggers on startup, loading existing tasks from `todolist.json` into the session state.
2. **UI Generation**: `st.columns` partitions the screen for inputs and task displays.
3. **Mutation**: User interaction (Add/Delete) triggers a callback function.
4. **Synchronization**: The callback modifies the session state and calls `ToDoStorage.storeData` to sync the physical file.
5. **Rerender**: Streamlit automatically reruns the script, reflecting the updated state in the browser.

---

## SETUP AND EXECUTION

### Requirements

* **Python 3.x**
* **Streamlit Library**: `pip install streamlit`

### Execution

Run the following command in your terminal:

```bash
streamlit run your_script_name.py

```
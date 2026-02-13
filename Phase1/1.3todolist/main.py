import streamlit as st
import json

userTask = ""


class ToDoStorage:
    def __init__(self):
        self.todolist = []

    def storeData(todolist):
        with open("todolist.json", "w", encoding="utf-8") as f:
            json.dump(todolist, f, ensure_ascii=False, indent=4)

    def loadData():
        try:
            with open("todolist.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: The file todolist.json was not found.")


def ontaskAdd():
    st.session_state["todolist"].append(
        {
            "value": st.session_state["task_input_ele"],
            "id": len(st.session_state["todolist"]),
        }
    )
    st.session_state["task_input_ele"] = ""

    ToDoStorage.storeData(st.session_state["todolist"])


def ontaskDelete(taskId):
    fullList = st.session_state["todolist"]

    st.session_state["todolist"] = [
        item for item in fullList if item.get("id") != taskId
    ]

    ToDoStorage.storeData(st.session_state["todolist"])


def main():
    toDoList = ToDoStorage.loadData()

    if toDoList:
        st.session_state["todolist"] = toDoList


if __name__ == "__main__":
    main()

if "todolist" not in st.session_state:
    st.session_state["todolist"] = []

st.title("Todo App")
col1, col2 = st.columns([4, 1], vertical_alignment="bottom")
with col1:
    st.text_input(
        " Task",
        max_chars=255,
        label_visibility="visible",
        icon=None,
        width="stretch",
        key="task_input_ele",
    )
with col2:
    st.button("Add", type="primary", on_click=ontaskAdd)

st.subheader("Todo List")
with st.container(border=True):
    for taskItem in st.session_state["todolist"]:
        subcol1, subcol2 = st.columns([4, 1], vertical_alignment="center")
        with subcol1:
            st.write(taskItem.get("value"))
        with subcol2:
            st.button(
                "Delete",
                type="secondary",
                key=taskItem.get("id"),
                on_click=ontaskDelete,
                args=(taskItem.get("id"),),
            )

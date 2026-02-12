import re
import streamlit as st


class Calculate:
    def __init__(self, userInput):
        self.userInput = userInput
        self.normalize()
        pass

    def normalize(self):
        inputValues = "".join(self.userInput).split(" ")
        normalizedValues = []

        for i in inputValues:
            expression = i
            parts = re.split(r"(\+|\-|\*)", expression)
            normalizedValues.extend(parts)

        self.input = normalizedValues

    def calucate(self):
        operatorStack = []
        outputQue = []
        result = []
        for i in self.input:
            if i in ["+", "-", "*"]:
                operatorStack.append(i)
            else:
                outputQue.append(i)
        rpnList = outputQue + operatorStack

        for i in rpnList:
            if i in ["+", "-", "*"]:
                if i == "+":
                    pop1 = result.pop()
                    pop2 = result.pop()

                    result.append(int(pop1) + int(pop2))
                elif i == "-":
                    pop1 = result.pop()
                    pop2 = result.pop()

                    result.append(int(pop1) - int(pop2))
                else:
                    pop1 = result.pop()
                    pop2 = result.pop()

                    result.append(int(pop1) * int(pop2))
            elif i not in [" "]:
                result.append(int(i))
        return result


def eval_function():
    result = Calculate(finalMessage).calucate()
    flex = st.container(border=True)
    for i in result:
        flex.text("Result:")
        flex.badge(str(i), color="blue")


def setup():
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            for number in [" ", "0", "1", "2"]:
                if st.button(number, type="primary"):
                    st.session_state.operation.append(number)
    with col2:
        with st.container(border=True):
            for number in ["3", "4", "5"]:
                if st.button(number, type="primary"):
                    st.session_state.operation.append(number)
    with col3:
        with st.container(border=True):
            for number in ["6", "7", "8", "9"]:
                if st.button(number, type="primary"):
                    st.session_state.operation.append(number)

    with st.container(border=True, horizontal=True):
        if st.button("Add", type="primary"):
            st.session_state.operation.append("+")
        if st.button("Sub", type="primary"):
            st.session_state.operation.append("-")
        if st.button("Multi", type="primary"):
            st.session_state.operation.append("*")

    st.button("=", type="secondary", on_click=eval_function)


st.title("Very Simple Calcuater ", width="stretch", text_alignment="left")
st.header(
    "This only does one math operation at a time (like $5 + 5$). It can't handle long equations with different operators mixed together",
    width="stretch",
    text_alignment="left",
)


if "operation" not in st.session_state:
    st.session_state.operation = []

setup()
# Display every message stored in the list

finalMessage = []
for message in st.session_state.operation:
    finalMessage.append(message)

st.text("".join(finalMessage), width="content")

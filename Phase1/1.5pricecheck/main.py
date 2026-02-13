import joblib
import streamlit as st


model = None
try:
    model = joblib.load("housing_model.pkl")
except FileNotFoundError:
    print("Model not found. Run train_model.py first.")


def main():
    print()


if __name__ == "__main__":
    main()


st.title("Housing Price Predictor")
container = st.container(border=True)
with container:
    houseArea = st.text_input("Enter Avg Area Income", "0")
    predictPrice = st.button("Predict Price")
    print("model", model)
    print("houseArea", houseArea)
    value = model.predict([[int(houseArea)]])
    st.text(f"house value for given area is {value[0]}")

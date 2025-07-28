import streamlit as st

st.title("Simple BMI Calculator")

# Sidebar inputs
st.sidebar.header("Enter your details")
weight = st.sidebar.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
height = st.sidebar.number_input("Height (cm)", min_value=30.0, max_value=250.0, value=170.0)

# BMI calculation
if height > 0:
    bmi = weight / ((height / 100) ** 2)
    bmi = round(bmi, 2)

    st.write(f"Your BMI is: **{bmi}**")

    # BMI categories
    if bmi < 18.5:
        st.write("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        st.write("Category: Overweight")
    else:
        st.write("Category: Obese")
else:
    st.write("Please enter a valid height")

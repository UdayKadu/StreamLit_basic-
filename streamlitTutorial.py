import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")
st.text("Let's get started!")

#conditional logic with widgets
name = st.text_input("What's your name?")
if st.button("Great!"):
    st.success(f"Hello, {name}!")


#Display data and charts
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
st.line_chart(df)
st.bar_chart(df)

#File uploader
uploaded_file = st.file_uploader("Choose a file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)

st.title("Text and Markdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is some text.")
st.markdown("**Bold**,**Italic*, and `Code`,[link](https://streamlit.io).")
st.code("for i in range(5):\n    print(i)", language="python")

st.text_input("Enter some text:")
st.text_area("Enter a longer text:")
st.number_input("Pick a number:", min_value=0, max_value=100, value=50)
st.slider("Select a range:", 0,100)
st.selectbox("Choose an fruit:", ["Apple", "Banana", "Cherry"])
st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.chat_input("I agree to the terms and conditions.")
st.multiselect("Select multiple options:", ["Option A", "Option B", "Option C"])

if st.checkbox("Check me out!"):
    st.write("Checkbox is checked!")
option = st.radio(
    "Choose an option:",
    ["Option $", "Option %", "Option &"]
)
if option == "Option 1":
    st.write("You selected Option 1")
else:
    st.write(f"You selected {option}")  

with st.form("Login Form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")
    if submitted:
        st.write(f"Username: {username}, Password: {password}")

st.image("https://www.magnific.com/free-photos-vectors/jpg",caption="Sample Image", use_column_width=True)
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", format="video/mp4", start_time=0)       
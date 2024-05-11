import streamlit as st

import os
import google.generativeai as genai



st.markdown("""
    <style>
    .title {
        font-size: 40px;
        color: #ff6347;  # This is a tomato color
        font-family: 'Helvetica', sans-serif;  # Font style
        text-align: center;
        margin-bottom: 20px;
    }
    .textbox {
        font-family: 'Verdana', sans-serif;
        font-size: 18px;
        color: #333;
    }
    .btn {
        font-size: 20px;
        color: white;
        background-color: #0078D4;  # This is a blue color
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# Use HTML for the title with custom class for styling
st.markdown("<div class='title'>MathMatrixMovies</div>", unsafe_allow_html=True)


GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)



# Text input for the prompt
prompt = st.text_input("Enter the topic you wanna generate video on")

# Create columns for the dropdowns and the button
col1, col2, col3 = st.columns(3)

# Dropdown 1 in the first column
with col1:
    option1 = st.selectbox(
        'Age',
        ['3', '4', '5','6','7','8','9','10','11','12','13','14','15','16','17','18', 'Undergraduate', 'Graduate'], key="1")

# Dropdown 2 in the second column
with col2:
    option2 = st.selectbox(
        'Language',
        ['English', 'Hindi','Spanish', 'Mandarin', 'Turkish', 'Tamil'], key="2")

# Button in the third column, spanning the third and fourth columns
with col3:
    if st.button("Generate", key="3"):
        # This block will execute when the button is pressed
        # Display the entered prompt and selections
        st.write(f"You entered: {prompt}")
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        response = model.generate_content(f"{prompt} Can you create manim script for that explanation.")
        print(response.text)
        st.write(f"Option 1 selected: {option1}")
        st.write(f"Option 2 selected: {option2}")

# # Empty space in the fourth column (optional, adjust as needed)
# with col4:
#     st.write("")

    
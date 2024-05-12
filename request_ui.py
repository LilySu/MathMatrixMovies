import streamlit as st
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
st.markdown("<div class='title'>MathMatrixMovies</div>",
            unsafe_allow_html=True)
st.video('https://youtu.be/-4-M8YwAlhU')
iframe = '<iframe class="airtable-embed" src="https://airtable.com/embed/appJHjHaquTmMQ82e/pagAMECsTYqX6unw9/form" frameborder="0" onmousewheel="" width="100%" height="1066" style="background: transparent;"></iframe>'
st.markdown(iframe, unsafe_allow_html=True)
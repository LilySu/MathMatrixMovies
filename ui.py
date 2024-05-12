from google_auth_oauthlib.flow import Flow
import os
import streamlit as st
from create_movie import create_math_matrix_movie
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

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

# Text input for the prompt
prompt = st.text_input("Enter the topic you wanna generate video on", key="video_prompt")

# Create columns for the dropdowns and the button
col1, col2, col3 = st.columns(3)

# Dropdown 1 in the first column
with col1:
    option1 = st.selectbox(
        'Age',
        ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', 'Undergraduate', 'Graduate'], key="1")

# Dropdown 2 in the second column
with col2:
    option2 = st.selectbox(
        'Language',
        ['English', 'Hindi', 'Spanish', 'Mandarin', 'Turkish', 'Tamil'], key="2")

# Button in the third column, spanning the third and fourth columns
with col3:
    if st.button("Generate", key="3"):
        # This block will execute when the button is pressed
        # Display the entered prompt and selections
        st.write(f"You entered: {prompt}")
        st.write(f"Option 1 selected: {option1}")
        st.write(f"Option 2 selected: {option2}")
        video_result = create_math_matrix_movie(prompt, option1, option2)
        st.video(video_result["video_url"])

# Setup environment variable for Google credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_secrets.json'

# Define the OAuth flow function
def authenticate_user():
    scopes = ['https://www.googleapis.com/auth/youtube']
    flow = Flow.from_client_secrets_file(
        'client_secrets.json',
        scopes=scopes,
        redirect_uri='https://math.auto.movie')  # Ensure this is correctly registered in Google Cloud Console
    auth_url, state = flow.authorization_url(prompt='consent', include_granted_scopes='true')
    return flow, auth_url, state

# Sidebar for connecting to YouTube OAuth
with st.sidebar:
    st.write("Connect to Services")
    if st.button('Connect to YouTube'):
        flow, auth_url, state = authenticate_user()
        st.session_state['auth_state'] = state  # Save the state token in session state
        st.session_state['auth_url'] = auth_url
        st.write('Please go to this URL: ', auth_url)

    # Text input for authorization code
    code = st.text_input('Enter the authorization code here', key="auth_code")
    if st.button('Authenticate', key="authenticate"):
        if 'auth_state' in st.session_state and code:
            try:
                # Rebuild the flow object using saved state
                flow = Flow.from_client_secrets_file(
                    'client_secrets.json',
                    scopes=['https://www.googleapis.com/auth/youtube'],
                    state=st.session_state['auth_state'],
                    redirect_uri='https://math.auto.movie')
                flow.fetch_token(code=code)
                credentials = flow.credentials

                # Saving the credentials for later use
                credentials_json = credentials.to_json()
                with open('credentials.json', 'w') as cred_file:
                    cred_file.write(credentials_json)

                st.success('You are now authenticated!')
            except Exception as e:
                st.error(f"Failed to authenticate: {str(e)}")
        else:
            st.error("Please reconnect and provide a valid authorization code.")



# Now 'credentials' is ready to be used with Google API client libraries
def upload_video_to_youtube(credentials, file_path, title, description, category_id, tags):
    """
    Uploads a video to YouTube.

    Args:
    credentials (google.oauth2.credentials.Credentials): The authenticated Google OAuth credentials
    file_path (str): Path to the video file
    title (str): Title of the video
    description (str): Description of the video
    category_id (str): YouTube category ID
    tags (list): List of tags for the video

    Returns:
    dict: Response from the YouTube API
    """
    # Load credentials from file
    with open('credentials.json', 'r') as cred_file:
        credentials_json = cred_file.read()
        credentials = Credentials.from_authorized_user_info(json.loads(credentials_json))
    youtube = build('youtube', 'v3', credentials=credentials)

    # Define the body of the request
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': 'public'  # or 'private' or 'unlisted'
        }
    }

    # Define the media file to upload
    media = MediaFileUpload(file_path, mimetype='video/*', resumable=True)

    # Create the YouTube video insert request
    request = youtube.videos().insert(
        part='snippet,status',
        body=body,
        media_body=media
    )

    # Execute the upload
    response = request.execute()

    return response

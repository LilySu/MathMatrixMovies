from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
import json
from google.oauth2.credentials import Credentials
import os
from groq import Groq
from dotenv import load_dotenv
import re
load_dotenv()


def remove_code_snippet(prompt):
    # Regular expression pattern to match the code snippet between ``` ```
    pattern = r'```.*?```'

    # Replace the code snippet with an empty string
    cleaned_prompt = re.sub(pattern, '', prompt, flags=re.DOTALL)

    return cleaned_prompt.strip()


def format_prompt(prompt, variables):
    # Format the prompt string with the extracted variables
    formatted_prompt = prompt.format(**{var: var for var in variables})

    return formatted_prompt


def remove_symbols(text):
    text = text.replace('"', '')
    text = text.replace('*', '')
    text = text.replace('<', '')
    text = text.replace('>', '')
    return text


def trim_string(text):
    # Check if the text is at least 6 characters long
    if len(text) < 6:
        return "Error: The string is too short to remove six characters."
    # Remove the first 3 and last 3 characters
    return text[3:-3]


def remove_text_within_stars(text):
    # Regex pattern to find content between double stars including the stars
    pattern = r'\*\*[^*]+\*\*'
    # Replace the found patterns with an empty string
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

# math_problem, audience_type, language, voice_label = parse_arguments()


def llama3_call(math_problem, audience_type, language, voice_label):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    TITLE_PROMPT = f'''Provide a concise and trendy YouTube tutorial \
                    video title in less than 100 characters for \
                    the following topic of {math_problem} \
                    use the target audience of {audience_type} years old in the language of {language} \
                    voice_label to influence the title. Do not include the word 'manim' \
                    since every single video is using manim so it's redundant. Do not \
                    output the title with special characters. \
                    repeat the content. Do not print out manim code. Make the title \
                    less than 100 characters. Do not return the title formatted in bold.\
                    Do not output any special characters in the title such as *  \
                    Do not return any additional explanations other than the title.\
                    Make sure the math_problem {math_problem} is part of the title \
                    Do not bold the title, do not put the title with two asterisks. \
                    Don't make the title too generic. Do not explain yourself. Just \ 
                    output the title and nothing else.'''

    DESCRIPTION_PROMPT = f'''Provide a good YouTube video description for a video that has \
                    been generated via the following prompt: {math_problem} \
                    use the target audience math_problem, audience_type, language, \
                    voice_label to influence the description. Do not include the word 'manim' \
                    since every single video is using manim so it's redundant. Output the \
                    title in double stars and just output the description and no further comments \
                    Do not repeat the content. Do not print out manim code. Make the title \
                    less than 100 characters. Do not return Python code \
                    Do not return any additional explanations other than the description.\
                    Generate a description between 1000 to 5000 characters. \
                    Make sure the math_problem {math_problem} is part of the description.
                    Make the tone and sophistication of the text appropriate for students \
                    at {audience_type} age. Just output the description and nothing else.'''

    TAG_PROMPT = f'''Provide tags related to the topic of {math_problem} \
                    that are fitting to the \
                    YouTube Data API that would help with SEO optimization. \
                    Make sure the math_problem {math_problem} is one of the tags. \
                    Output a python list of strings. Do not include any other text \
                    outside a python list of strings.'''

    title_generated = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": TITLE_PROMPT
            }
        ],
        model="llama3-8b-8192",
    )

    description_generated = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": DESCRIPTION_PROMPT
            }
        ],
        model="llama3-8b-8192",
    )

    tags_generated = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": TAG_PROMPT
            }
        ],
        model="llama3-8b-8192",
    )

    yt_title_not_cleaned = title_generated.choices[0].message.content
    yt_title = remove_symbols(yt_title_not_cleaned)
    yt_title = yt_title.replace("**", "")
    print(yt_title)

    print("\n")

    yt_description = description_generated.choices[0].message.content
    yt_description = remove_code_snippet(yt_description)
    yt_description = remove_text_within_stars(yt_description)
    print(yt_description)

    print("\n")

    yt_category_id = 28

    yt_tags = tags_generated.choices[0].message.content
    yt_tags = remove_code_snippet(yt_tags)
    print(yt_tags)
    return {"title": yt_title, "description": yt_description, "category_id": yt_category_id, "tags": yt_tags}


# Now 'credentials' is ready to be used with Google API client libraries


def upload_video_to_youtube(file_path, title, description, category_id, tags):
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
        credentials = Credentials.from_authorized_user_info(
            json.loads(credentials_json))
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
    print(response)

    return response

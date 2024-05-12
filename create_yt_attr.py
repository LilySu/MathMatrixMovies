import os
from groq import Groq
from dotenv import load_dotenv
import argparse
import re
from create_movie import MOVIE_PROMPT, parse_arguments
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

math_problem, audience_type, language, voice_label = parse_arguments()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

movie_prompt_no_code = remove_code_snippet(MOVIE_PROMPT)

TITLE_PROMPT = f'''Provide a concise and trendy YouTube tutorial video title for \
                the following prompt that generated a tutorial video: {movie_prompt_no_code}\
                use the target audience math_problem, audience_type, language, \
                voice_label to influence the title. Do not include the word 'manim' \
                since every single video is using manim so it's redundant. output the \
                title in double stars and just output the title and nothing else, do not \
                repeat the content. Do not print out manim code. Make the title \
                less than 100 characters. Do not return the title formatted in bold.\
                Do not output any special characters in the title such as *  \
                Do not return any additional explanations other than the title.\
                Make sure the math_problem {math_problem} is part of the title''' 

DESCRIPTION_PROMPT = f'''Provide a good YouTube video description for a video that has \
                been generated via the following prompt: {movie_prompt_no_code} \
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
                at {audience_type} age.'''

TAG_PROMPT = f'''Provide tags related to the topic of {math_problem} \
                with {movie_prompt_no_code} that are fitting to the \
                YouTube Data API that would help with SEO optimization. \
                Make sure the math_problem {math_problem} is one of the tags. \
                Output a list of strings. '''

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
print(yt_title)

print("\n\n\n")

yt_description = description_generated.choices[0].message.content
yt_description = remove_code_snippet(yt_description)
print(yt_description)

yt_category_id = 28

yt_tags = tags_generated.choices[0].message.content
print(yt_description)
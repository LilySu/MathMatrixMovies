import random
import requests
from bs4 import BeautifulSoup
import time
import json
import glob
import subprocess
import uuid
import argparse
import re
import os
import cv2
import shutil
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()


def extract_code_blocks(text):
    # Regular expression pattern to find code blocks surrounded by triple backticks
    pattern = r"```python(.*?)```"

    # Using re.DOTALL to make the dot match newlines as well
    matches = re.findall(pattern, text, re.DOTALL)

    # 'matches' will be a list of all the code blocks found in the text
    return matches


GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate a math movie based on the given problem, audience age, and language."
    )
    parser.add_argument("--math_problem", type=str, default="Explain the pythagorean theorem",
                        help="The math problem to be visualized in the movie.")
    parser.add_argument("--audience_type", type=int, default=10,
                        help="The target audience age for the math movie.")
    parser.add_argument("--language", type=str, default="English",
                        help="The language for the movie narration (default is English).")
    parser.add_argument("--voice_label", type=str, default="en-US-AriaNeural",
                        help="The voice label for the narration (default is en-US-AriaNeural).")
    args = parser.parse_args()
    return args.math_problem, args.audience_type, args.language, args.voice_label


def main():
    pass


MOVIE_PROMPT = """

Can you explain the following to an audience of {audience_type}? 

Request: '{math_problem}'

Please be visual and interesting in your explanation. Consider using a meme if the audience is younger.

Please create python code for a manim video for the same. 

Do not create any sound effects. The only images you have access to are svgs you can download with the download_svg_from_query fn. Scale svgs appropriately for use please.

Always add a title and an outro. Always narrate the title and outro.

Please try to visually center or attractively lay out all content. Please also keep the margins in consideration. If a sentence is long please wrap it by splitting it into multiple lines. 

Please add actual numbers and formulae wherever appropriate as we want our {audience_type} to learn math & reason visually and conceptually as well.

Do use voiceovers to narrate the video. The following is an example of how to do that, and also how to import the download_svg_from_query function:

```
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from create_movie import download_svg_from_query

class AzureExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

        # Download SVGs
        brain_svg = download_svg_from_query("brain")
        cnn_svg = download_svg_from_query("computer")
        rnn_svg = download_svg_from_query("flow chart")
        transformer_svg = download_svg_from_query("robot")
        robot_svg = download_svg_from_query("robot")

        # Draw shapes
        circle = Circle()
        square = Square().shift(2 * RIGHT)

        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)

        with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
            self.play(circle.animate.shift(2 * LEFT),
                      run_time=tracker.duration)

        with self.voiceover(text="Now, let's transform it into a square.") as tracker:
            self.play(Transform(circle, square), run_time=tracker.duration)

        with self.voiceover(
            text="You can also change the pitch of my voice like this.",
            prosody={{"pitch": "+40Hz"}},
        ) as tracker:
            pass

        with self.voiceover(text="Thank you for watching."):
            self.play(Uncreate(circle))

        self.wait()
```

The voice for the "{language}" is "{voice_label}". Please use this voice for the narration.  

First write the script explicitly and refine the contents and then write the code.

Please draw and animate things, using the whole canvas. Use color.

Please add actual numbers and formulae wherever appropriate as we want our audience of {audience_type} to learn math. Please do not leave large blank gaps in the video. Make it visual and interesting. PLEASE ENSURE ELEMENTS FADE OUT AT THE APPROPRIATE TIME. DO NOT LEAVE ARTIFACTS ACROSS SCENES AS THEY OVERLAP AND ARE JARRING. WRAP TEXT IF IT IS LONG. FORMAT TABLES CORRECTLY. ENSURE LABELS, FORMULAE, TEXT AND OBJECTS DO NOT OVERLAP OR OCCLUDE EACH OTHER. TEXT SHOULD NOT OVERLAP EVER!!! ALL ELEMENTS SHOULD BE WELL LAID OUT!!!. Be an elegant video designer. Scale charts and numbers TO FIT THE SCREEN. And don't let labels run into each other or overlap, or take up poor positions. For example, do not label a triangle side length at the corners, but the middle. Do not write equations that spill across the Y axis bar or X axis bar, etc.

If the input is math that is obviously wrong, do not generate any code.

You can search for svgs for objects like 'tree' and 'satellite' and then download them and get the download path using the download_svg_from_query('satellite') fn. DO NOT MAKE UP PATHS, USE THE download_svg_from_query(query) fn

You can also search_google for concepts and then ingest the results into this context via fetch_html to create your video. Include "manim" in the search query if you need syntactical help. Do any research BEFORE writing code.

Please use only manim for the video. Please write ALL the code needed in one block in your final response since it will be extracted directly and run from your response. 

Make it visual and interesting please. The goal is to demonstrate concepts through cool visuals and animations, not present a powerpoint. Flex the power of Manim to create beautiful visuals and animations. Feel free to look up syntax and examples from the internet. 

Consider all the requirements carefully, but have fun and be creative. Use tools to download images or do research, or both, then in your final answer write all the code. ALL THE CODE IN THE FINAL BLOCK PLEASE. NO SKIPPING LINES, THE ENTIRE MANIM FILE.


"""


TRANSLATION_PROMPT = """
Ok. now translate the text to {language}, and replace the voice_label for azureservice with {voice_label}. Please write ALL the code in one go so that it can be extracted and run directly.
"""

#       hindi_text = Text('नमस्ते', font='Lohit Devanagari')  # Replace 'Lohit Devanagari' with any available Hindi font
#        tamil_text = Text('வணக்கம்', font='Lohit Tamil')  # Replace 'Lohit Tamil' with any available Tamil font
# Create or cleanup existing extracted image frames directory.


def create_frame_output_dir(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


FRAME_PREFIX = "_frame"


def extract_frame_from_video(video_file_path, frame_extraction_directory):
    print(
        f"Extracting {video_file_path} at 1 frame per second. This might take a bit...")
    create_frame_output_dir(frame_extraction_directory)
    vidcap = cv2.VideoCapture(video_file_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    # Calculate the ideal number of frames to extract
    max_frames = 60  # Maximum number of frames to extract
    if duration <= 60:
        frame_extraction_rate = 1  # 1 fps for videos under 60 seconds
    else:
        frame_extraction_rate = max(1, int(total_frames / max_frames))

    output_file_prefix = os.path.basename(video_file_path).replace('.', '_')
    frame_count = 0
    count = 0
    while vidcap.isOpened():
        success, frame = vidcap.read()
        if not success:  # End of video
            break
        if count % frame_extraction_rate == 0:  # Extract a frame at the calculated rate
            # Calculate the actual time for the frame
            time_in_seconds = count / fps
            min = int(time_in_seconds // 60)
            sec = int(time_in_seconds % 60)
            time_string = f"{min:02d}:{sec:02d}"
            image_name = f"{output_file_prefix}{FRAME_PREFIX}{time_string}.jpg"
            output_filename = os.path.join(
                frame_extraction_directory, image_name)
            cv2.imwrite(output_filename, frame)
            frame_count += 1
        count += 1
    vidcap.release()
    print(
        f"Completed video frame extraction!\n\nExtracted: {frame_count} frames at a rate of {frame_extraction_rate} frames per second.")
    return {"video_duration": duration, "frame_count": frame_count, "frame_extraction_rate": frame_extraction_rate}


class File:
    def __init__(self, file_path: str, display_name: str = None):
        self.file_path = file_path
        if display_name:
            self.display_name = display_name
        self.timestamp = get_timestamp(file_path)

    def set_file_response(self, response):
        self.response = response


def get_timestamp(filename):
    """Extracts the frame count (as an integer) from a filename with the format
       'output_file_prefix_frame00:00.jpg'.
    """
    parts = filename.split(FRAME_PREFIX)
    if len(parts) != 2:
        return None  # Indicates the filename might be incorrectly formatted
    return parts[1].split('.')[0]


def create_python_file(response):
    code_blocks = extract_code_blocks(response.text)

    if not code_blocks:
        return ""

    # Find the biggest code block
    biggest_code_block = max(code_blocks, key=len)

    print("Found the biggest code block:")
    print(biggest_code_block.strip())
    code = biggest_code_block.strip()

    filename = f"MathMovie_{uuid.uuid4().hex[:8]}"

    # Open the file in write mode ('w') which will overwrite the file if it already exists
    with open(f"{filename}.py", 'w') as file:
        file.write(code)

    return filename


def make_request(prompt, files):
    request = [prompt]
    for file in files:
        request.append(file.timestamp)
        request.append(file.response)
    return request


def send_message_with_retries(chat, request, max_retries=3):
    retry_wait = 60  # upped to 60 seconds cos of 504s grr
    for attempt in range(max_retries):
        try:
            response = chat.send_message(request)
            return response
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(retry_wait)
            retry_wait *= 2  # exponential backoff
    raise Exception("Max retries exceeded")


def fetch_html(url: str) -> str:
    """
    Fetch the HTML content of a given URL and return it as is.

    Args:
        url: The URL to fetch the HTML content from.
    Returns:
        The raw HTML content.
    """
    print(f"fetching html from url: {url}")
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.text


def search_google(query: str) -> list:
    """
    Search Google and return a list of URLs from the search results.

    Args:
        query: The search query string.
    Returns:
        A list of URLs from the search results.
    """
    print(f"searching google for: {query}")
    page = requests.get(
        f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(page.content, "html5lib")
    links = soup.findAll("a")

    urls = []
    for link in links:
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            url = link.get('href').split("?q=")[1].split("&sa=U")[0]
            if url.startswith("http") and "google.com" not in url and "youtube.com" not in url:
                urls.append(url)

    print(f"google search results for {query}:")
    print(urls)

    return urls


def search_svg_repo(query: str) -> list:
    """
    Search for SVGs on svgrepo.com based on the given query.

    Args:
        query: The search query string.
    Returns:
        A list of dictionaries containing SVG titles and URLs or a message indicating no results.
    """
    # Strip leading/trailing whitespace and replace multiple spaces with a single hyphen
    slugified_query = re.sub(r'\s+', '-', query.strip().lower())
    url = f"https://www.svgrepo.com/vectors/{slugified_query}/multicolor/"

    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    soup = BeautifulSoup(response.content, "html.parser")

    # Check for "No Results in Vectors" message
    no_results = soup.find("h2", text="No Results in Vectors")
    if no_results:
        return f"No results found for the given query: {query}."

    # Find all nodes in the result table
    nodes = soup.find_all('div', class_='style_Node__GkK82')

    results = []
    for node in nodes:
        img_url = node.find('img')['src']
        results.append(img_url)
    print(f"svg repo results for {query}:")
    print(results)
    return results


def download_svg_from_url(url: str) -> str:
    """
    Download an SVG from the given URL and save it to the media/images/svgs/ directory.

    Args:
        url: The URL of the SVG to download.
    Returns:
        The path to the saved SVG file.
    """
    print(f"downloading svg from url: {url}")
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.join(current_script_dir, "media/images/svgs/")

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Extract the filename from the URL
    filename = os.path.basename(url)
    save_path = os.path.join(save_dir, filename)

    print(f"saving svg to path: {save_path}")

    with open(save_path, 'wb') as file:
        file.write(response.content)

    return save_path


def download_svg_from_query(query: str) -> str:
    """
    Search for SVGs based on the given query and download a random result from the top 3 or the first one if fewer than 3 results.

    Args:
        query: The search query string.
    Returns:
        The path to the saved SVG file.
    """
    results = search_svg_repo(query)

    if isinstance(results, str):
        # If the result is a string, it means no results were found
        raise ValueError(results)

    if not results:
        raise ValueError(f"No SVGs found for the given query '{query}'.")

    # Select a random result from the top 3 or the first one if fewer than 3 results
    selected_url = random.choice(results[:3])

    return download_svg_from_url(selected_url)


def create_math_matrix_movie(math_problem, audience_type, language="English", voice_label="en-US-AriaNeural"):
    # Check if audience_type is a digit and format it as "x years old", otherwise leave as is
    if str(audience_type).isdigit():
        audience_type = f"{audience_type} year olds"
    else:
        audience_type = f"{audience_type} audience"

    # Fill up the MOVIE_PROMPT with the provided arguments
    filled_prompt = MOVIE_PROMPT.format(
        math_problem=math_problem, audience_type=audience_type, language=language, voice_label=voice_label)

    tools = [search_google, fetch_html, download_svg_from_query]
    model = genai.GenerativeModel('gemini-1.5-pro-latest', tools=tools)
    print(model._tools.to_proto())
    chat = model.start_chat(enable_automatic_function_calling=True)

    attempt_count = 0
    success = False

    next_prompt = filled_prompt

    while attempt_count < 8 and not success:
        print(f"attempt #{attempt_count+1} next_prompt: {next_prompt}")
        response = send_message_with_retries(chat, next_prompt)
        print(response.text)
        filename = create_python_file(response)
        command = f"{os.getenv('MANIM_BIN')} -ql {filename}.py --disable_caching"
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)
        print(f"result: {result.returncode}")

        if result.returncode == 0:
            success = True
        else:
            attempt_count += 1
            error_prompt = f"Your last code iteration created an error, this is the text of the error: {result.stderr}\nRemember to download ALL images using the download_svg_from_query function.\nYou can also search_google for concepts and then ingest the results into this context via fetch_html to create your video. Include 'manim' in the search query if you need syntactical help. Do any research BEFORE writing code.\n Please write ALL the code in one go so that it can be extracted and run directly.  ALL THE CODE IN THE FINAL BLOCK PLEASE. NO SKIPPING LINES, THE ENTIRE MANIM FILE."
            next_prompt = error_prompt

    if not success:
        print("Failed to generate a successful output after 8 attempts.")
        raise Exception(
            "Failed to generate a successful output after 8 attempts.")

    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    path_pattern = os.path.join(
        current_script_dir, f"media/videos/{filename}/480p15/*.mp4")
    mp4_files = glob.glob(path_pattern)

    video_file_path = mp4_files[0]
    with open(f"{filename}.py", 'r') as file:
        initial_code = file.read()
    video_url = os.getenv('BASE_URL') + video_file_path.split("media")[1]

    yield {
        "stage": "initial",
        "video_path": video_file_path,
        "video_id": filename,
        "video_url": video_url,
        "original_prompt": filled_prompt,
        "initial_code": initial_code
    }

    NUM_ITERATIONS = 4
    # Generate 4 videos
    for i in range(NUM_ITERATIONS):
        print(f"iteration #{i+1}")
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        path_pattern = os.path.join(
            current_script_dir, f"media/videos/{filename}/480p15/*.mp4")
        mp4_files = glob.glob(path_pattern)

        video_file_path = mp4_files[0]
        with open(f"{filename}.py", 'r') as file:
            initial_code = file.read()
        video_url = os.getenv('BASE_URL') + video_file_path.split("media")[1]

        video_file = genai.upload_file(path=video_file_path)

        # Check whether the file is ready to be used.
        while video_file.state.name == "PROCESSING":
            print('.', end='')
            time.sleep(10)
            video_file = genai.get_file(video_file.name)

        if video_file.state.name == "FAILED":
            raise ValueError(video_file.state.name)

        prompt = f"""
            Watch the video, study the code you generated previously and make tweaks to make the video more appealing, if needed. Ask yourself: is there anything wrong with the attached images? How are the text colors, spacing and so on. How are the animations? How is their placement? be terse and focus on actionable insights with references to what code needs to be changed and how and why. This is for an AI video editor. This is your f{i+1}th attempt out of {NUM_ITERATIONS}. Each one should be an improvement, check the history and be sure this is the case.
            
            Remember to:
            - make sure there are voiceovers throughout
            - that visuals match audio
            - THAT VISUALS MAKE SENSE
            - that the whole thing isn't boring like a powerpoint
            - center titles
            - make sure title text fits on screen, or make it wrap. THIS IS VERY IMPORTANT AS TITLES GOING OFF SCREEN MAKES VIDEOS LOOK SUPER UNPROFESSIONAL.
            - make sure outro text fits on screen, or make it wrap. THIS IS VERY IMPORTANT AS TITLES GOING OFF SCREEN MAKES VIDEOS LOOK SUPER UNPROFESSIONAL.
            - use the whole canvas and do not let text or diagrams OVERLAP. VERY IMPORTANT. NO OVERLAPPING
            - no text should roll off screen. NO ROLLING OFF SCREEN!
            - no text should be too small. WELL SIZED!
            - no text should be too big. WELL SIZED!
            - there should not be looong stretches of blank screen. NO BLANK STRETCHES!
            - diagrams should be labelled correctly. WELL LABELLED!
            - diagrams should be placed correctly. WELL PLACED!
            - diagrams should be animated correctly. WELL ANIMATED!
            - there should not be any artifacts. OVERLAPPING OBJECTS TURN VIEWERS OFF. THINGS HAVE TO BE SIZED RIGHT AND FADE IN AND OUT CORRECTLY AND NOT CROSS EACH OTHER.
            - ARE IMAGES AND TEXT OVERLAPPING? THEY SHOULD NEVER OVERLAP. IF THEY ARE OVERLAPPING, MAKE THEM NOT OVERLAP. BLEEDS VIEWERS.
            - animations should be awesome & educational!
            - there should not be significant stretches of blank screen. BLANK SECTIONS WITH NO VISUALS ARE VERY BORING, BLEED VIEWERS.
            - leave some padding at the bottom to allow for where subtitles would appear
            - you can use svgs using the functions provided
            - you can use google search results to help with code stuff
            - you can use google search results to help with concepts
            - please make it fun and creative.
                    
            Previous code:
            ```
            {initial_code}
            ```
            
            Enumerate actionable insights, and reference the timestamp and the precise code segment that needs modification, and note how it needs modification. For example, a title may need to be centered, text may need to wrap, and the font may need to be smaller. 
            
            Once you're done with listing all helpful suggestions, please write a FINAL block with ALL Manim code that includes ALL the code needed since that final block will be extracted directly and run from your response.  ALL THE CODE IN THE FINAL BLOCK PLEASE. NO SKIPPING LINES, THE ENTIRE MANIM FILE.
                    
            Remember, your goal is to explain the following to {audience_type}: '{math_problem}'. 
            
            Please stick to explaining the right thing in an interesting way appropriate to the audience. 
            
            The goal is to make a production grade math explainer video that will help viewers quickly and thoroughly learn the concept. You are a great AI video editor and educator. Looking forward to your feedback!
        """

        # Make the LLM request.
        request = [prompt, video_file]
        response = send_message_with_retries(chat, request)
        print(response.text)

        filename = create_python_file(response)
        # Assuming filename is already defined as shown previously
        command = f"{os.getenv('MANIM_BIN')} -ql {filename}.py --disable_caching"
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)

        if result.returncode != 0:
            attempt_count = 0
            success = False
            error_prompt = f"Your last code iteration created an error, this is the text of the error: {result.stderr}\nRemember to download ALL images using the download_svg_from_query function.\nYou can also search_google for concepts and then ingest the results into this context via fetch_html to create your video. Include 'manim' in the search query if you need syntactical help. Do any research BEFORE writing code.\n Please write ALL the code in one go so that it can be extracted and run directly.\n ALL THE CODE IN THE FINAL BLOCK PLEASE. NO SKIPPING LINES, THE ENTIRE MANIM FILE."
            next_prompt = error_prompt

            NUM_ATTEMPTS = 8
            while attempt_count < NUM_ATTEMPTS and not success:
                print(f"attempt #{attempt_count+1} next_prompt: {next_prompt}")
                response = send_message_with_retries(chat, next_prompt)
                print(response.text)
                filename = create_python_file(response)
                command = f"{os.getenv('MANIM_BIN')} -ql {filename}.py --disable_caching"
                result = subprocess.run(command, shell=True,
                                        capture_output=True, text=True)
                print(f"result: {result.returncode}")

                if result.returncode == 0:
                    success = True
                else:
                    attempt_count += 1
                    error_prompt = f"Your last code iteration created an error, this is the text of the error: {result.stderr}\nThis is attempt #{attempt_count+1} out of {NUM_ATTEMPTS}.\nIf it's the {NUM_ATTEMPTS/2} attempt or greater, please start being conservative and make your atempted code output simpler or the code won't compile and generation will fail.\nRemember to download ALL images using the download_svg_from_query function.\nYou can also search_google for concepts and then ingest the results into this context via fetch_html to create your video. Include 'manim' in the search query if you need syntactical help. Do any research BEFORE writing code.\n Please write ALL the code in one go so that it can be extracted and run directly.\n ALL THE CODE IN THE FINAL BLOCK PLEASE. NO SKIPPING LINES, THE ENTIRE MANIM FILE."
                    next_prompt = error_prompt

        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        path_pattern = os.path.join(
            current_script_dir, f"media/videos/{filename}/480p15/*.mp4")
        mp4_files = glob.glob(path_pattern)

        video_file_path = mp4_files[0]

        with open(f"{filename}.py", 'r') as file:
            final_code = file.read()

        video_url = os.getenv('BASE_URL') + video_file_path.split("media")[1]

        yield {
            "stage": "final",
            "iteration": i+1,
            "video_path": video_file_path,
            "video_id": filename,
            "video_url": video_url,
            "original_prompt": filled_prompt,
            "final_code": final_code,
        }

    # Write subprocess
if __name__ == "__main__":
    main()

import glob
import subprocess
import uuid
import argparse
import re
import os
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


def main():
    parser = argparse.ArgumentParser(
        description="Generate a math movie based on the given problem, audience age, and language.")
    parser.add_argument("math_problem", type=str,
                        help="The math problem to be visualized in the movie.")
    parser.add_argument("audience_type", type=int,
                        help="The target audience age for the math movie.")
    parser.add_argument("--language", type=str, default="English",
                        help="The language for the movie narration (default is English).")
    parser.add_argument("--voice_label", type=str, default="en-US-AriaNeural",
                        help="The voice label for the narration (default is en-US-AriaNeural).")

    args = parser.parse_args()

    # Placeholder for the function that creates the math movie
    create_math_matrix_movie(
        args.math_problem, args.audience_type, args.language, args.voice_label)


MOVIE_PROMPT = """

Can you explain {math_problem} to a {audience_type}? Be visual and creative please. Please create python code for a manim video for the same. 

Please do not use any external dependencies like mp3s or svgs or graphics. If you need to draw something, do so using exclusively manim. 

Do use voiceovers to narrate the video. The following is an example of how to do that:

```
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class AzureExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

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

The voice for the "{language}" is "{voice_label}". Please use this voice for the narration. Always keep the global speed as 1.15, like the example provided.

Please do not use any external dependencies like svgs since they are not available. Please use only manim for the video. Please write ALL the code needed since it will be extracted directly and run from your response. 


"""


TRANSLATION_PROMPT = """
Ok. now translate the text to {language}, and replace the voice_label for azureservice with {voice_label}. Please write ALL the code in one go so that it can be extracted and run directly.
"""

#       hindi_text = Text('नमस्ते', font='Lohit Devanagari')  # Replace 'Lohit Devanagari' with any available Hindi font
#        tamil_text = Text('வணக்கம்', font='Lohit Tamil')  # Replace 'Lohit Tamil' with any available Tamil font


def create_math_matrix_movie(math_problem, audience_type, language="English", voice_label="en-US-AriaNeural"):
    # Check if audience_type is a digit and format it as "x years old", otherwise leave as is
    if str(audience_type).isdigit():
        audience_type = f"{audience_type} year old"

    # Fill up the MOVIE_PROMPT with the provided arguments
    filled_prompt = MOVIE_PROMPT.format(
        math_problem=math_problem, audience_type=audience_type, language=language, voice_label=voice_label)

    # Print the filled prompt to the console
    print(filled_prompt)
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(filled_prompt)
    code_blocks = extract_code_blocks(response.text)
    for block in code_blocks:
        print("Found code block:")
        print(block.strip())
        code = block.strip()
    # exec(code)
    filename = f"MathMovie_{uuid.uuid4().hex[:8]}"

    # Open the file in write mode ('w') which will overwrite the file if it already exists
    with open(f"{filename}.py", 'w') as file:
        file.write(code)
    # Assuming filename is already defined as shown previously
    command = f"{os.getenv('MANIM_BIN')} -ql {filename}.py --disable_caching"
    subprocess.run(command, shell=True)
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    path_pattern = os.path.join(
        current_script_dir, f"media/videos/{filename}/480p15/*.mp4")
    mp4_files = glob.glob(path_pattern)
    return {"video_url": mp4_files[0], "video_id": filename}

    # Write subprocess
if __name__ == "__main__":
    main()

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class QuadraticExpressions(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

        # Introduction
        intro_text = Tex("Let's learn about Quadratic Expressions!").scale(1.5)
        with self.voiceover(text="Let's learn about Quadratic Expressions!") as tracker:
            self.play(Write(intro_text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(intro_text))

        # ... (rest of your scene code) ...

    def tear_down(self):
        super().tear_down() 
        
        # Now delete and/or adjust files (after the scene is rendered)
        for filename in os.listdir("media/voiceovers/"):
            if filename.endswith(".mp3"):
                filepath = os.path.join("media/voiceovers/", filename)

                # Option 1: Delete the file
                # os.remove(filepath)

                # Option 2: Adjust speed, etc. (Code from previous responses can be used here)
                # For example:
                from manim_voiceover.modify_audio import adjust_speed
                adjust_speed(filepath, filepath, speed=1.2)
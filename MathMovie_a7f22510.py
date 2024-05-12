from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import uuid

class QuadraticExpressions(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

        # Unique ID to avoid file overwriting
        unique_id = uuid.uuid4()

        # Introduction
        with self.voiceover(text="Hey there! Today, we're going to explore quadratic expressions.",
                           file_name=f"intro_{unique_id}") as tracker:
            text = Tex("Quadratic Expressions").scale(1.5)
            self.play(Write(text), run_time=tracker.duration)
        self.play(FadeOut(text))

        # What are Quadratic Expressions?
        with self.voiceover(text="A quadratic expression is a special type of mathematical expression that involves a variable squared.",
                           file_name=f"what_are_quadratics_{unique_id}") as tracker:
            text = Tex("What are Quadratic Expressions?").scale(1.2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(text))

        with self.voiceover(text="You'll recognize them because they have the general form ax squared plus bx plus c.",
                           file_name=f"general_form_{unique_id}") as tracker:
            formula = MathTex("ax^2 + bx + c").scale(1.2)
            self.play(Write(formula), run_time=tracker.duration)
        self.wait(0.5)

        # CORRECTED INDEXING 
        with self.voiceover(text="Where 'a', 'b', and 'c' are constants - just regular numbers.",
                           file_name=f"constants_{unique_id}") as tracker:
            a = formula[0:2]  # Select "a" from the formula
            b = formula[3:5] # Select "b" from the formula
            c = formula[6:7]  # Select "c" from the formula
            self.play(FadeToColor(a, YELLOW),
                      FadeToColor(b, BLUE),
                      FadeToColor(c, RED), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="And 'x' is our variable, the one that can change.",
                           file_name=f"variable_{unique_id}") as tracker:
            x = formula[2] # Select the first "x" from the formula (the other one is visually identical)
            self.play(FadeToColor(x, GREEN), run_time=tracker.duration)
        self.wait(1)

        # Example: x^2 + 2x + 1 (rest of the code remains unchanged)

       # ... (rest of the code remains the same)
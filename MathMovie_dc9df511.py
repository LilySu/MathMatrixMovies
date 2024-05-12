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

        # Delete existing voiceover files to prevent overwriting issues
        for filename in os.listdir("media/voiceovers/"):
            if filename.endswith(".mp3"):
                os.remove(os.path.join("media/voiceovers/", filename))

        # Introduction
        intro_text = Tex("Let's learn about Quadratic Expressions!").scale(1.5)
        with self.voiceover(text="Let's learn about Quadratic Expressions!") as tracker:
            self.play(Write(intro_text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(intro_text))

        # What are quadratic expressions?
        what_text = Tex("What are quadratic expressions?").scale(1.2)
        with self.voiceover(text="What are quadratic expressions?") as tracker:
            self.play(Write(what_text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(what_text.animate.to_edge(UP))

        # Show the standard form
        standard_form = MathTex("ax^2 + bx + c").scale(1.2)
        with self.voiceover(text="They are expressions that can be written in the form 'a x squared plus b x plus c'.") as tracker:
            self.play(Write(standard_form), run_time=tracker.duration)
        self.wait(0.5)

        # Highlight each part - CORRECTED INDEXING
        a_rect = SurroundingRectangle(standard_form[0:2], color=BLUE)
        b_rect = SurroundingRectangle(standard_form[5:7], color=GREEN) 
        c_rect = SurroundingRectangle(standard_form[10:], color=RED)  

        with self.voiceover(text="Where 'a', 'b', and 'c' are constants,") as tracker:
            self.play(Create(a_rect), run_time=tracker.duration/3)
            self.play(Create(b_rect), run_time=tracker.duration/3)
            self.play(Create(c_rect), run_time=tracker.duration/3)
        self.wait(0.5)

        with self.voiceover(text="and 'x' is the variable.") as tracker:
            self.play(FadeOut(a_rect), FadeOut(b_rect), FadeOut(c_rect), run_time=tracker.duration)
        self.wait(0.5)

        # Example
        example_text = Tex("For example:").next_to(standard_form, DOWN, buff=0.5)
        example_expression = MathTex("3x^2 + 5x - 2").next_to(example_text, DOWN, buff=0.5).scale(1.2)

        with self.voiceover(text="For example, 3 x squared plus 5 x minus 2") as tracker:
            self.play(Write(example_text), run_time=tracker.duration/2)
            self.play(Write(example_expression), run_time=tracker.duration/2)
        self.wait(0.5)

        # Explain a, b, and c values - CORRECTED INDEXING
        with self.voiceover(text="Here, 'a' is 3, 'b' is 5, and 'c' is negative 2.") as tracker:
            self.play(Indicate(example_expression[0:2]), run_time=tracker.duration/3)
            self.play(Indicate(example_expression[5:7]), run_time=tracker.duration/3)
            self.play(Indicate(example_expression[10:]), run_time=tracker.duration/3)
        self.wait(0.5)

        # Importance of a not being 0
        imp_text = Tex("Important: 'a' cannot be 0").next_to(example_expression, DOWN, buff=0.5).scale(0.9).set_color(YELLOW)
        with self.voiceover(text="Importantly, 'a' cannot be zero, otherwise, it wouldn't be a quadratic expression!") as tracker:
            self.play(Write(imp_text), run_time=tracker.duration)
        self.wait(0.5)

        # Fade out everything
        self.play(FadeOut(what_text), FadeOut(standard_form), FadeOut(example_text), FadeOut(example_expression), FadeOut(imp_text))

        # Why are they called quadratic?
        why_text = Tex("Why are they called \\textbf{quadratic}?").scale(1.2)
        with self.voiceover(text="Why are they called quadratic?") as tracker:
            self.play(Write(why_text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(why_text.animate.to_edge(UP))

        # Explain the term 'quadratic'
        square_text = Tex("'Quad' means square").scale(1.1)
        with self.voiceover(text="'Quad' means square, ") as tracker:
            self.play(Write(square_text), run_time=tracker.duration)
        self.wait(0.5)

        # Show x squared
        x_squared = MathTex("x^2").next_to(square_text, DOWN, buff=0.5).scale(1.2)
        with self.voiceover(text="and in quadratic expressions, the highest power of 'x' is 2, hence x squared.") as tracker:
            self.play(Write(x_squared), run_time=tracker.duration)
        self.wait(0.5)

        # Conclusion
        conclusion_text = Tex("So, these expressions are all about the square!").scale(1.1)
        with self.voiceover(text="So, these expressions are all about the square!") as tracker:
            self.play(Write(conclusion_text.next_to(x_squared, DOWN, buff=0.5)), run_time=tracker.duration)
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(why_text), FadeOut(square_text), FadeOut(x_squared), FadeOut(conclusion_text))
        self.wait(0.5)

        # Outro
        outro_text = Tex("That's quadratic expressions in a nutshell!").scale(1.2)
        with self.voiceover(text="That's quadratic expressions in a nutshell!") as tracker:
            self.play(Write(outro_text), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(outro_text))

        self.wait()
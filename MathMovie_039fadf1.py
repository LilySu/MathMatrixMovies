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
            self.play(FadeToColor(formula[0], YELLOW),
                      FadeToColor(formula[3], BLUE),
                      FadeToColor(formula[5], RED), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="And 'x' is our variable, the one that can change.",
                           file_name=f"variable_{unique_id}") as tracker:
            self.play(FadeToColor(formula[1], GREEN), run_time=tracker.duration)
        self.wait(1)

        # Example: x^2 + 2x + 1
        with self.voiceover(text="Let's look at an example.  How about x squared plus 2x plus 1?",
                           file_name=f"example_{unique_id}") as tracker:
            example = MathTex("x^2 + 2x + 1").scale(1.2)
            self.play(ReplacementTransform(formula, example), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="Here, our 'a' is 1, 'b' is 2, and 'c' is 1.",
                           file_name=f"example_constants_{unique_id}") as tracker:
            self.play(FadeToColor(example[0], YELLOW),
                      FadeToColor(example[2], BLUE),
                      FadeToColor(example[4], RED), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(example))

        # Why are they important?
        with self.voiceover(text="So why are these quadratic expressions so important?",
                           file_name=f"importance_{unique_id}") as tracker:
            text = Tex("Why are they important?").scale(1.2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(text))

        with self.voiceover(text="Well, they pop up everywhere! From describing the path of a thrown ball,",
                           file_name=f"applications_{unique_id}") as tracker:
            text = Tex("They pop up everywhere!").scale(1.2).to_edge(UP)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="to calculating areas,",
                           file_name=f"areas_{unique_id}") as tracker:
            rect = Rectangle(width=2, height=1).set_fill(BLUE, opacity=0.5).shift(LEFT * 3)
            area_text = Tex("Area = length x width").next_to(rect, DOWN)
            self.play(FadeIn(rect), Write(area_text), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="to even understanding how populations grow!",
                           file_name=f"populations_{unique_id}") as tracker:
            graph = FunctionGraph(lambda x: 0.1 * (x + 3) * (x - 5), x_range=[-4, 6]).scale(0.5).shift(RIGHT * 3)
            dot = Dot(graph.point_from_proportion(0.7))
            self.play(Create(graph), FadeIn(dot), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(text), FadeOut(rect), FadeOut(area_text), FadeOut(graph), FadeOut(dot))

        # Conclusion
        with self.voiceover(text="So, keep an eye out for these quadratic expressions - they're more common than you might think!",
                           file_name=f"conclusion_{unique_id}") as tracker:
            text = Tex("Keep an eye out for them!").scale(1.2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(text))

        with self.voiceover(text="That's it for today! See you next time!",
                           file_name=f"outro_{unique_id}"):
            self.wait(1)
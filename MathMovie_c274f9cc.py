from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

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
        with self.voiceover(text="Hey there! Today, we're going to explore quadratic expressions.") as tracker:
            text = Tex("Quadratic Expressions").scale(1.5)
            self.play(Write(text), run_time=tracker.duration)
        self.play(FadeOut(text))

        # What are Quadratic Expressions?
        with self.voiceover(text="A quadratic expression is a special type of mathematical expression that involves a variable squared.") as tracker:
            text = Tex("What are Quadratic Expressions?").scale(1.2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(text))

        with self.voiceover(text="You'll recognize them because they have the general form ax squared plus bx plus c.") as tracker:
            formula = MathTex("ax^2 + bx + c").scale(1.2)
            self.play(Write(formula), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="Where 'a', 'b', and 'c' are constants - just regular numbers.") as tracker:
            self.play(FadeToColor(formula[0], YELLOW),
                      FadeToColor(formula[2], BLUE),
                      FadeToColor(formula[4], RED), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="And 'x' is our variable, the one that can change.") as tracker:
            self.play(FadeToColor(formula[1], GREEN), run_time=tracker.duration)
        self.wait(1)

        # Example: x^2 + 2x + 1
        with self.voiceover(text="Let's look at an example.  How about x squared plus 2x plus 1? ") as tracker:
            example = MathTex("x^2 + 2x + 1").scale(1.2)
            self.play(ReplacementTransform(formula, example), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="Here, our 'a' is 1, 'b' is 2, and 'c' is 1.") as tracker:
            self.play(FadeToColor(example[0], YELLOW),
                      FadeToColor(example[2], BLUE),
                      FadeToColor(example[4], RED), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(example))

        # Why are they important?
        with self.voiceover(text="So why are these quadratic expressions so important?") as tracker:
            text = Tex("Why are they important?").scale(1.2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(text))

        with self.voiceover(text="Well, they pop up everywhere!  From describing the path of a thrown ball, ") as tracker:
            text = Tex("They pop up everywhere!").scale(1.2).to_edge(UP)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="to calculating areas, ") as tracker:
            rect = Rectangle(width=2, height=1).set_fill(BLUE, opacity=0.5).shift(LEFT*3)
            area_text = Tex("Area = length x width").next_to(rect, DOWN)
            self.play(FadeIn(rect), Write(area_text), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="to even understanding how populations grow!") as tracker:
            graph = FunctionGraph(lambda x: 0.1*(x+3)*(x-5), x_range=[-4,6]).scale(0.5).shift(RIGHT*3)
            dot = Dot(graph.point_from_proportion(0.7))
            self.play(Create(graph), FadeIn(dot), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(text), FadeOut(rect), FadeOut(area_text), FadeOut(graph), FadeOut(dot))

        # Conclusion
        with self.voiceover(text="So, keep an eye out for these quadratic expressions - they're more common than you might think!") as tracker:
            text = Tex("Keep an eye out for them!").scale(1.2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(text))

        with self.voiceover(text="That's it for today! See you next time!"):
            self.wait(1)
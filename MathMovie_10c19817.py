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
        with self.voiceover(text="Hey there! Today, we're diving into the world of quadratic expressions.") as tracker:
            text = Text("Quadratic Expressions", font_size=48).shift(UP*2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)

        # Basic form
        with self.voiceover(text="These guys might seem intimidating, but they're just equations with a fancy name. ") as tracker:
            self.play(FadeOut(text), run_time=tracker.duration)
        with self.voiceover(text="They follow a simple structure, something like this:") as tracker:
            eq = MathTex("ax^2 + bx + c").shift(UP*2)
            self.play(Write(eq), run_time=tracker.duration)
        self.wait(0.5)

        # Explanation of terms
        with self.voiceover(text="Here, 'a', 'b', and 'c' are just numbers, plain and simple.  'x' is our variable, the unknown we're trying to figure out.") as tracker:
            self.play(FadeToColor(eq[0][0], BLUE), run_time=tracker.duration/3)
            self.play(FadeToColor(eq[0][4], RED), run_time=tracker.duration/3)
            self.play(FadeToColor(eq[0][8], GREEN), run_time=tracker.duration/3)
        self.wait(0.5)

        with self.voiceover(text="And that little '2' above the 'x'? That's what makes it quadratic! It means we're squaring our variable.") as tracker:
            self.play(Indicate(eq[0][2]), run_time=tracker.duration)
        self.wait(0.5)

        # Example: Throwing a ball
        with self.voiceover(text="Let's imagine throwing a ball.  The path it follows, that beautiful arc, can be represented by a quadratic expression.") as tracker:
            axes = Axes(
                x_range=[0, 5, 1],
                y_range=[0, 6, 1],
                x_length=5,
                y_length=4,
                axis_config={"include_numbers": True}
            ).shift(DOWN*2)
            self.play(Create(axes), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="Imagine this parabola represents the path of our ball. Its shape is determined by our 'a', 'b', and 'c' values.") as tracker:
            graph = axes.get_graph(lambda x: -0.5*x**2 + 2.5*x, color=YELLOW)
            dot = Dot(color=RED).move_to(axes.c2p(1, 2))
            self.play(Create(graph), run_time=tracker.duration)
            self.play(Create(dot), run_time=tracker.duration)
        self.wait(0.5)

        # Conclusion
        with self.voiceover(text="So, quadratic expressions are all about these curvy parabolas.  They pop up everywhere, from physics to economics!") as tracker:
            self.play(FadeOut(eq), FadeOut(axes), FadeOut(graph), FadeOut(dot), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="That's the gist of it!  Hopefully, quadratic expressions seem a little less scary now.") as tracker:
            text = Text("The End", font_size=48).shift(UP * 2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(2)

        self.play(FadeOut(text))
        self.wait()
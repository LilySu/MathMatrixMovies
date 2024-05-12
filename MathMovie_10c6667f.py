from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class QuadraticEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

        # Introduction
        with self.voiceover(text="Hey there! Today, we're diving into the world of quadratic equations.") as tracker:
            title = Text("Quadratic Equations").scale(1.5)
            self.play(Write(title), run_time=tracker.duration)
        self.wait()
        self.play(FadeOut(title))

        # What are quadratic equations?
        with self.voiceover(text="A quadratic equation is an equation where the highest power of the variable is 2.  It has the general form ax squared plus bx plus c equals 0.") as tracker:
            eq = MathTex("ax^2 + bx + c = 0").scale(1.2)
            self.play(Write(eq), run_time=tracker.duration)
        self.wait()

        # Example
        with self.voiceover(text="Let's look at an example. Consider the equation x squared plus 3x minus 4 equals 0.") as tracker:
            example_eq = MathTex("x^2 + 3x - 4 = 0").scale(1.2)
            self.play(Transform(eq, example_eq), run_time=tracker.duration)
        self.wait()

        # Graphing
        with self.voiceover(text="When we graph quadratic equations, they create a beautiful, symmetrical curve called a parabola.") as tracker:
            axes = Axes(
                x_range=[-5, 5, 1],
                y_range=[-10, 5, 1],
                axis_config={"include_numbers": True},
            )
            graph = axes.plot(lambda x: x**2 + 3*x - 4, color=BLUE) # Corrected line 
            self.play(Create(axes), run_time=tracker.duration / 2)
            self.play(Create(graph), run_time=tracker.duration / 2)
        self.wait()

        # Solutions
        with self.voiceover(text="The solutions to a quadratic equation, also known as its roots, are the points where the parabola intersects the x-axis.") as tracker:
            dots = VGroup(
                Dot(axes.c2p(-4, 0), color=RED),
                Dot(axes.c2p(1, 0), color=RED)
            )
            self.play(Create(dots), run_time=tracker.duration)
        self.wait()

        # Solving
        with self.voiceover(text="There are different ways to solve quadratic equations, like factoring, completing the square, and using the quadratic formula.") as tracker:
            formula = MathTex(
                "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"
            ).scale(1.2)
            self.play(FadeOut(dots, graph, axes), FadeIn(formula), run_time=tracker.duration)
        self.wait()

        # Conclusion
        with self.voiceover(text="And that's a quick look at quadratic equations! They're a key concept in algebra with various applications in physics, engineering, and beyond.  Keep exploring, and you'll discover their amazing power!") as tracker:
            self.play(FadeOut(formula, example_eq), run_time=tracker.duration)
        self.wait()
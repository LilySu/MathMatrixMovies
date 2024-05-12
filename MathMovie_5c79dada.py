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
        with self.voiceover(text="Let's explore quadratic expressions!") as tracker:
            text = Tex("Quadratic Expressions").scale(1.5)
            self.play(Write(text), run_time=tracker.duration)
        self.wait()
        self.play(FadeOut(text))

        # What are they?
        with self.voiceover(text="They're like special equations that involve a variable squared. Think of 'x squared'!") as tracker:
            x_squared = MathTex("x^2").scale(1.5)
            self.play(Write(x_squared), run_time=tracker.duration)
        self.wait()

        # General Form
        with self.voiceover(text="Their general form looks like this: ax squared plus bx plus c.") as tracker:
            general_form = MathTex("ax^2 + bx + c").scale(1.5)
            self.play(Transform(x_squared, general_form), run_time=tracker.duration)
        self.wait()

        # Example
        with self.voiceover(text="Let's see an example: 2x squared plus 5x minus 3") as tracker:
            example = MathTex("2x^2 + 5x - 3").scale(1.5)
            self.play(Transform(general_form, example), run_time=tracker.duration)
        self.wait()

        # Visualizing with a parabola
        with self.voiceover(text="These expressions can be visualized as parabolas, U-shaped curves on a graph.") as tracker:
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[-5, 10, 1],
                axis_config={"include_tip": False},
            )
            graph = axes.plot(lambda x: 2*x**2 + 5*x - 3, color=BLUE)
            parabola_label = Tex("Parabola").scale(0.8).next_to(graph, RIGHT)
            self.play(FadeIn(axes), Create(graph), Write(parabola_label), run_time=tracker.duration)
        self.wait()

        # Applications
        with self.voiceover(text="They're used in tons of real-world scenarios! Think about the path of a basketball, or figuring out profits.") as tracker:
            basketball = Circle(radius=0.2, color=ORANGE).move_to(axes.c2p(-1, 5))
            path = DashedVMobject(axes.plot(lambda x: -0.5*(x + 1)**2 + 6, x_range=[-3, 1]), num_dashes=30)
            profit_text = Tex("Profit Analysis").scale(0.8).next_to(axes, DOWN, buff=0.5)

            # Create the path first
            self.play(Create(path), run_time=tracker.duration)

            # Now animate the basketball along the path
            self.play(FadeIn(basketball), Write(profit_text))
            self.play(MoveAlongPath(basketball, path), run_time=2)
        self.wait()

        # Conclusion
        with self.voiceover(text="That's quadratic expressions in a nutshell! Keep exploring, there's so much more to discover.") as tracker:
            self.play(FadeOut(axes), FadeOut(graph), FadeOut(parabola_label),
                      FadeOut(basketball), FadeOut(path), FadeOut(profit_text),
                      FadeOut(example), run_time=tracker.duration)
        self.wait()
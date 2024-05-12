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
        
        # Title
        title = Text("Quadratic Equations", font_size=48).to_edge(UP)
        with self.voiceover(text="Let's explore the world of Quadratic Equations!") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        self.wait()

        # Basic Equation
        equation = MathTex("ax^2 + bx + c = 0").scale(1.5).shift(UP)
        with self.voiceover(text="They look a bit like this.") as tracker:
            self.play(FadeIn(equation), run_time=tracker.duration)
        self.wait()

        # Explain each term
        a_label = Text("a: coefficient of x²", font_size=24).next_to(equation, DOWN).shift(2*LEFT)
        b_label = Text("b: coefficient of x", font_size=24).next_to(equation, DOWN)
        c_label = Text("c: constant term", font_size=24).next_to(equation, DOWN).shift(2*RIGHT)
        
        with self.voiceover(text="The letters a, b, and c represent numbers called coefficients. ") as tracker:
            self.play(Write(a_label), run_time=tracker.duration)
        self.wait()

        with self.voiceover(text="They tell us how much each part of the equation matters.") as tracker:
            self.play(Write(b_label), run_time=tracker.duration)
            self.play(Write(c_label), run_time=tracker.duration)
        self.wait()

        # Example Equation
        example = MathTex("2x^2 + 5x - 3 = 0").scale(1.5).shift(2*DOWN)
        with self.voiceover(text="Here's an example. Can you spot the coefficients?") as tracker:
            self.play(Write(example), run_time=tracker.duration)
        self.wait(2) # Pause to let viewers spot coefficients

        # Highlight coefficients
        a_highlight = SurroundingRectangle(example[0:1], color=YELLOW)
        b_highlight = SurroundingRectangle(example[3:4], color=YELLOW)
        c_highlight = SurroundingRectangle(example[6:8], color=YELLOW)

        with self.voiceover(text="Here's a hint: The coefficient of x² is 2") as tracker:
            self.play(Create(a_highlight), run_time=tracker.duration)
        self.wait()

        with self.voiceover(text="The coefficient of x is 5") as tracker:
            self.play(Create(b_highlight), run_time=tracker.duration)
        self.wait()

        with self.voiceover(text="and the constant term is -3") as tracker:
            self.play(Create(c_highlight), run_time=tracker.duration)
        self.wait(2)

        self.play(FadeOut(a_highlight), FadeOut(b_highlight), FadeOut(c_highlight))

        # Graphing
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-10, 10, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True},
        ).shift(DOWN)

        graph = axes.get_graph(lambda x: 2*x**2 + 5*x - 3, color=BLUE)

        with self.voiceover(text="Quadratic equations describe curves called parabolas.") as tracker:
            self.play(Create(axes), run_time=tracker.duration)
            self.play(Create(graph), run_time=2)  # Take 2 seconds to draw the graph
        self.wait()

        # Roots
        dots = VGroup(*[Dot(axes.c2p(root, 0), color=RED) for root in [-3, 0.5]])
        with self.voiceover(text="The points where the parabola crosses the x-axis are called roots or solutions.") as tracker:
            self.play(Create(dots), run_time=tracker.duration)
        self.wait(2)

        # End
        with self.voiceover(text="That's a glimpse into the world of Quadratic Equations! Keep exploring!") as tracker:
            self.play(FadeOut(title, equation, a_label, b_label, c_label, example, axes, graph, dots), run_time=tracker.duration)
        self.wait()
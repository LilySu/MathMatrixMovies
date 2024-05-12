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
            text = Text("Quadratic Expressions").scale(0.8)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(text))

        # What are quadratic expressions?
        with self.voiceover(text="A quadratic expression is like a special type of math sentence. It has a variable, usually 'x', raised to the power of 2.") as tracker:
            text = Tex("$x^2$").scale(2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="It can also have other terms with 'x' and some constant numbers.") as tracker:
            text2 = Tex("$x^2 + 3x + 2$").scale(2)
            self.play(Transform(text, text2), run_time=tracker.duration)
        self.wait(0.5)

        # Examples
        with self.voiceover(text="Think of it like building a tower with LEGO blocks. The '$x^2$' term is like a big square block.") as tracker:
            square = Square(side_length=1, color=BLUE).shift(UP*2)
            self.play(Create(square), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="The '3x' term is like three rectangular blocks, each representing 'x'.") as tracker:
            rectangles = VGroup(*[Rectangle(width=1, height=0.3, color=GREEN) for _ in range(3)]).arrange(RIGHT, buff=0.1).next_to(square, DOWN, buff=0.2)
            self.play(Create(rectangles), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="Finally, the '2' is like two small single blocks.") as tracker:
            small_squares = VGroup(*[Square(side_length=0.3, color=RED) for _ in range(2)]).arrange(RIGHT, buff=0.1).next_to(rectangles, DOWN, buff=0.2)
            self.play(Create(small_squares), run_time=tracker.duration)
        self.wait(0.5)

        # Putting it together
        with self.voiceover(text="All these blocks together represent our quadratic expression, '$x^2 + 3x + 2$'.") as tracker:
            self.play(FadeOut(text2), run_time=tracker.duration)
        self.wait(0.5)

        # Applications
        with self.voiceover(text="Quadratic expressions are super useful! They can describe the path of a ball thrown in the air.") as tracker:
            path = ParametricFunction(
                lambda t: np.array((t, -t**2 + 3*t, 0)),
                t_range=[0, 3],
                color=YELLOW,
            )
            self.play(Create(path), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="They can also help us solve problems about areas and shapes.") as tracker:
            self.play(FadeOut(square, rectangles, small_squares, path), run_time=tracker.duration)
        self.wait(0.5)

        # Conclusion
        with self.voiceover(text="So, next time you see an expression with '$x^2$', remember it's a quadratic expression, ready to help you understand the world around you.") as tracker:
            text = Text("Keep Exploring!").scale(0.8)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(1)

        self.play(FadeOut(text))
        self.wait()
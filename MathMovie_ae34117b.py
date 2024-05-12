from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class PythagoreanTheorem(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

        # Create a right triangle
        triangle = Polygon(
            [0, 3, 0],
            [4, 0, 0],
            [0, 0, 0],
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=WHITE
        )

        # Label the sides
        a = Text("a", font_size=30).next_to(triangle, LEFT)
        b = Text("b", font_size=30).next_to(triangle, DOWN)
        c = Text("c", font_size=30).next_to(triangle.get_center(), UP + RIGHT)

        with self.voiceover(text="The Pythagorean theorem is a fundamental concept in geometry that describes the relationship between the sides of a right triangle.") as tracker:
            self.play(Create(triangle), run_time=tracker.duration)

        with self.voiceover(text="A right triangle is a triangle that has one right angle, which is a 90-degree angle. Let's label the sides.") as tracker:
            self.play(Write(a), Write(b), Write(c), run_time=tracker.duration)

        with self.voiceover(text="The two shorter sides are called 'legs', often denoted as 'a' and 'b', and the longest side, opposite the right angle, is called the 'hypotenuse', denoted as 'c'.") as tracker:
            self.play(Wiggle(a), Wiggle(b), run_time=3),
            self.play(Wiggle(c), run_time=3)

        # Draw squares on each side
        a_square = Square(side_length=3, fill_color=RED, fill_opacity=0.5, stroke_color=WHITE).next_to(triangle, LEFT)
        b_square = Square(side_length=4, fill_color=GREEN, fill_opacity=0.5, stroke_color=WHITE).next_to(triangle, DOWN)
        c_square = Square(side_length=5, fill_color=YELLOW, fill_opacity=0.5, stroke_color=WHITE).rotate(triangle.get_angle()).move_to(triangle.get_center() + UP * 2)

        with self.voiceover(text="The theorem states that the sum of the squares of the two legs is equal to the square of the hypotenuse. Let's visualize this with squares.") as tracker:
            self.play(Create(a_square), run_time=tracker.duration/3)
            self.play(Create(b_square), run_time=tracker.duration/3)
            self.play(Create(c_square), run_time=tracker.duration/3)

        # Show formula
        formula = MathTex("a^2 + b^2 = c^2").scale(1.5).shift(DOWN * 2)

        with self.voiceover(text="This can be represented mathematically by the equation: a squared plus b squared equals c squared.") as tracker:
            self.play(Write(formula), run_time=tracker.duration)

        self.wait()
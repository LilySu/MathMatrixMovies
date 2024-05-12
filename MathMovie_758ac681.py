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

        # Intro
        with self.voiceover(text="The Pythagorean Theorem is a fundamental concept in geometry that describes the relationship between the sides of a right triangle.") as tracker:
            pass

        # Right triangle
        triangle = Polygon(ORIGIN, 3*RIGHT, 4*UP, color=BLUE)
        triangle.set_fill(BLUE, opacity=0.5)
        with self.voiceover(text="Let's start by looking at a right triangle.") as tracker:
            self.play(Create(triangle), run_time=tracker.duration)

        # Label sides
        a_label = Text("a").next_to(triangle, DOWN).shift(0.5*LEFT)
        b_label = Text("b").next_to(triangle, RIGHT)
        c_label = Text("c").next_to(triangle.get_center(), UP)
        with self.voiceover(text="The two shorter sides of the triangle are called the legs, and we label them 'a' and 'b'.") as tracker:
            self.play(Write(a_label), Write(b_label), run_time=tracker.duration)
        with self.voiceover(text="The longest side, opposite the right angle, is called the hypotenuse, and we label it 'c'.") as tracker:
            self.play(Write(c_label), run_time=tracker.duration)

        # Squares on sides
        a_square = Square(side_length=3).next_to(triangle, DOWN).shift(0.5*LEFT).set_fill(RED, opacity=0.5)
        b_square = Square(side_length=4).next_to(triangle, RIGHT).set_fill(GREEN, opacity=0.5)
        c_square = Square(side_length=5).move_to(triangle.get_center() + 2*UP).set_fill(YELLOW, opacity=0.5)
        with self.voiceover(text="Now, let's imagine we build squares on each side of the triangle.") as tracker:
            self.play(Create(a_square), Create(b_square), Create(c_square), run_time=tracker.duration)

        # Theorem statement
        theorem_text = MathTex("a^2 + b^2 = c^2").move_to(3*DOWN)
        with self.voiceover(text="The Pythagorean Theorem states that the sum of the areas of the squares on the legs (a² + b²) is equal to the area of the square on the hypotenuse (c²).") as tracker:
            self.play(Write(theorem_text), run_time=tracker.duration)

        # Example
        with self.voiceover(text="In our example, a = 3, b = 4, and c = 5. So, 3 squared plus 4 squared equals 5 squared, or 9 + 16 = 25.") as tracker:
            pass

        # Conclusion
        with self.voiceover(text="This theorem is incredibly useful for finding the length of an unknown side of a right triangle if you know the lengths of the other two sides.") as tracker:
            pass

        self.wait()
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
        triangle = Polygon(ORIGIN, 3*RIGHT, 4*UP, color=BLUE)
        triangle.set_fill(BLUE, opacity=0.5)

        # Label the sides
        a_label = Tex("a").next_to(triangle, LEFT)
        b_label = Tex("b").next_to(triangle, DOWN)
        c_label = Tex("c").next_to(triangle.get_center(), UP + RIGHT)

        with self.voiceover(text="The Pythagorean Theorem is a fundamental concept in geometry that describes the relationship between the sides of a right triangle.") as tracker:
            self.play(Create(triangle), run_time=tracker.duration)

        with self.voiceover(text="A right triangle is a triangle with one right angle, which is a 90-degree angle.") as tracker:
            self.play(Create(a_label), Create(b_label), Create(c_label), run_time=tracker.duration)
            self.wait(0.5)
        
        # Draw squares on each side of the triangle
        square_a = Square(side_length=3).next_to(triangle, LEFT).shift(UP * 1.5)
        square_b = Square(side_length=4).next_to(triangle, DOWN).shift(LEFT * 1.5)
        square_c = Square(side_length=5, color=YELLOW).move_to(triangle.get_center() + UP * 2.5 + RIGHT * 2.5)

        with self.voiceover(text="The theorem states that the sum of the squares of the two shorter sides, called the legs, is equal to the square of the longest side, called the hypotenuse.") as tracker:
            self.play(Create(square_a), Create(square_b), run_time=tracker.duration)
            self.wait(0.5)

        with self.voiceover(text="In mathematical terms, if 'a' and 'b' represent the lengths of the legs, and 'c' represents the length of the hypotenuse, then the Pythagorean theorem is expressed as:") as tracker:
            self.play(Create(square_c), run_time=tracker.duration)

        # Write the formula: a² + b² = c²
        formula = MathTex("a^2 + b^2 = c^2").next_to(square_c, RIGHT).scale(1.2)
        self.play(Write(formula))
        self.wait(2)

        # Show an example
        with self.voiceover(text="Let's see an example. If one leg of a right triangle is 3 units long and the other leg is 4 units long, we can use the Pythagorean theorem to find the length of the hypotenuse.") as tracker:
            self.play(FadeOut(square_c), FadeOut(formula), run_time=tracker.duration)
            self.wait(0.5)
 
        # Highlight sides a and b
        self.play(square_a.animate.set_fill(BLUE, opacity=0.8), square_b.animate.set_fill(BLUE, opacity=0.8))
        self.wait(1)

        # Substitute the values into the formula
        formula = MathTex("3^2 + 4^2 = c^2").next_to(triangle, DOWN * 3)
        self.play(Write(formula))
        self.wait(2)

        # Solve for c
        formula2 = MathTex("9 + 16 = c^2").next_to(formula, DOWN)
        formula3 = MathTex("25 = c^2").next_to(formula2, DOWN)
        formula4 = MathTex("c = 5").next_to(formula3, DOWN)
        self.play(Write(formula2))
        self.play(Write(formula3))
        self.play(Write(formula4))
        self.wait(2)

        # Fill square_c with color
        square_c = Square(side_length=5, color=YELLOW).move_to(triangle.get_center() + UP * 2.5 + RIGHT * 2.5)
        square_c.set_fill(YELLOW, opacity=0.8)
        c_label = Tex("5").next_to(square_c, UP + RIGHT)

        with self.voiceover(text="So, the length of the hypotenuse is 5 units.") as tracker:
            self.play(FadeIn(square_c), Write(c_label), run_time=tracker.duration)
            self.wait(2)

        # Emphasize the importance
        with self.voiceover(text="The Pythagorean theorem is a powerful tool with numerous applications in various fields, including mathematics, physics, engineering, and architecture.") as tracker:
            self.play(FadeOut(formula), FadeOut(formula2), FadeOut(formula3), FadeOut(formula4), run_time=tracker.duration)
            self.wait(2)

        self.play(FadeOut(triangle), FadeOut(square_a), FadeOut(square_b), FadeOut(square_c), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label))
        self.wait(1)
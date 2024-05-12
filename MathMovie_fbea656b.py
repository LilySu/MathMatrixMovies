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

        # Define colors
        side_color = BLUE
        hypotenuse_color = YELLOW

        # Create a right triangle
        triangle = Polygon(
            [0, 3, 0], [4, 0, 0], [0, 0, 0],
            fill_color=GREEN,
            fill_opacity=0.5,
            stroke_color=WHITE
        )

        # Add labels to the sides
        a_label = MathTex("a").next_to(triangle, LEFT).set_color(side_color)
        b_label = MathTex("b").next_to(triangle, DOWN).set_color(side_color)
        c_label = MathTex("c").next_to(triangle, UR).set_color(hypotenuse_color)

        # Group triangle and labels
        triangle_group = VGroup(triangle, a_label, b_label, c_label)

        # Introduce the Pythagorean theorem
        with self.voiceover(text="The Pythagorean theorem is a fundamental concept in geometry that describes the relationship between the sides of a right triangle.") as tracker:
            self.play(Create(triangle_group), run_time=tracker.duration)

        # Highlight the right angle
        right_angle = RightAngle(triangle.get_vertices()[2], triangle.get_vertices()[1], length=0.5)

        with self.voiceover(text="In a right triangle, the side opposite the right angle is called the hypotenuse, denoted by 'c'.") as tracker:
            self.play(Create(right_angle), run_time=tracker.duration)
            self.play(c_label.animate.scale(1.2).set_color(RED), run_time=tracker.duration)
            self.play(c_label.animate.scale(1/1.2).set_color(hypotenuse_color), run_time=tracker.duration)

        # Highlight the other two sides
        with self.voiceover(text="The other two sides are called legs, denoted by 'a' and 'b'.") as tracker:
            self.play(a_label.animate.scale(1.2).set_color(RED), run_time=tracker.duration)
            self.play(b_label.animate.scale(1.2).set_color(RED), run_time=tracker.duration)
            self.play(a_label.animate.scale(1/1.2).set_color(side_color), run_time=tracker.duration)
            self.play(b_label.animate.scale(1/1.2).set_color(side_color), run_time=tracker.duration)

        # State the theorem
        theorem = MathTex("a^2 + b^2 = c^2").to_edge(DOWN).set_color(ORANGE)
        with self.voiceover(text="The Pythagorean theorem states that the square of the hypotenuse is equal to the sum of the squares of the other two sides.") as tracker:
            self.play(Write(theorem), run_time=tracker.duration)

        # Create squares on each side
        a_square = Square(side_length=triangle.get_vertices()[0][1], fill_color=side_color, fill_opacity=0.5, stroke_color=side_color).next_to(triangle, LEFT, buff=0).align_to(triangle, DOWN)
        b_square = Square(side_length=triangle.get_vertices()[1][0], fill_color=side_color, fill_opacity=0.5, stroke_color=side_color).next_to(triangle, DOWN, buff=0)
        c_square = Square(side_length=triangle.get_vertices()[0][1] * np.sqrt(2), fill_color=hypotenuse_color, fill_opacity=0.5, stroke_color=hypotenuse_color).rotate(PI/4).move_to(triangle.get_center() + RIGHT*2)

        # Add labels to the squares
        a_square_label = MathTex("a^2").move_to(a_square.get_center()).set_color(WHITE)
        b_square_label = MathTex("b^2").move_to(b_square.get_center()).set_color(WHITE)
        c_square_label = MathTex("c^2").move_to(c_square.get_center()).set_color(WHITE)

        # Group squares and labels
        squares_group = VGroup(a_square, b_square, c_square, a_square_label, b_square_label, c_square_label)

        # Show squares and their relation to the theorem
        with self.voiceover(text="This means that if we draw squares on each side of the triangle, the area of the square on the hypotenuse (c²) is equal to the sum of the areas of the squares on the other two sides (a² + b²).") as tracker:
            self.play(FadeIn(squares_group), run_time=tracker.duration)

        self.wait(2)
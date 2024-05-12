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

        # Introduction
        with self.voiceover(text="Hey there! Today, we're diving into the Pythagorean theorem.") as tracker:
            text = Text("Pythagorean Theorem", font_size=48, color=BLUE).shift(UP*2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)

        # Draw a right triangle
        triangle = Polygon(
            [-2, -1, 0],
            [2, -1, 0],
            [2, 2, 0],
            color=WHITE,
            fill_opacity=0.5
        )
        with self.voiceover(text="This is a right triangle.  Notice the little square in the corner? That means it has a right angle, a 90-degree angle.") as tracker:
            self.play(Create(triangle), run_time=tracker.duration)
        self.wait(0.5)

        # Label sides
        a = Text("a", font_size=24).next_to(triangle, LEFT)
        b = Text("b", font_size=24).next_to(triangle, DOWN)
        c = Text("c", font_size=24).next_to(triangle.get_center() + RIGHT + UP, RIGHT)
        with self.voiceover(text="The sides of a right triangle have special names. The two shorter sides, forming the right angle, are called 'a' and 'b'.") as tracker:
            self.play(Write(a), Write(b), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="The longest side, opposite the right angle, is called the hypotenuse, or 'c'.") as tracker:
            self.play(Write(c), run_time=tracker.duration)
        self.wait(0.5)

        # State the theorem
        theorem = MathTex("a^2 + b^2 = c^2").shift(DOWN*2)
        with self.voiceover(text="The Pythagorean theorem states that in a right triangle, the sum of the squares of the two shorter sides is equal to the square of the hypotenuse.") as tracker:
            self.play(Write(theorem), run_time=tracker.duration)
        self.wait(0.5)

        # Example calculation
        with self.voiceover(text="For instance, if 'a' is 3 and 'b' is 4, we can find 'c'.") as tracker:
            self.play(FadeOut(a, b, c), run_time=tracker.duration)
            a = Text("3", font_size=24).next_to(triangle, LEFT)
            b = Text("4", font_size=24).next_to(triangle, DOWN)
            self.play(Write(a), Write(b), run_time=tracker.duration)
        self.wait(0.5)

        calc = MathTex("3^2 + 4^2 = c^2", "9 + 16 = c^2", "25 = c^2", "c = 5").shift(DOWN*2).arrange(DOWN, aligned_edge=LEFT)
        with self.voiceover(text="Substituting into our equation: 3 squared plus 4 squared equals c squared. That's 9 plus 16 equals c squared.  So 25 equals c squared.  Taking the square root of both sides gives us c equals 5.") as tracker:
            self.play(Write(calc), run_time=tracker.duration)
        self.wait(0.5)

        # Conclusion
        with self.voiceover(text="That's the Pythagorean theorem! It's a fundamental concept in geometry with tons of applications.") as tracker:
            self.play(FadeOut(triangle, a, b, c, theorem, calc), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="I hope you found this helpful! See you next time.") as tracker:
            self.play(Uncreate(text), run_time=tracker.duration)
        self.wait()
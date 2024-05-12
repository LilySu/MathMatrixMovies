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
        with self.voiceover(text="Hey there! Today we're diving into the world of quadratic expressions.") as tracker:
            text = Text("Quadratic Expressions", font_size=48).shift(UP*2)
            self.play(Write(text), run_time=tracker.duration)

        self.wait(0.5)
        self.play(FadeOut(text))

        # What are quadratic expressions?
        with self.voiceover(text="So, what exactly are they?") as tracker:
            pass
        
        with self.voiceover(text="Simply put, a quadratic expression is like a math sentence with a variable, usually 'x', raised to the power of two.") as tracker:
            text = MathTex("ax^2 + bx + c").scale(1.5)
            self.play(Write(text), run_time=tracker.duration)

        self.wait(1)

        # Example
        with self.voiceover(text="Let's look at an example:  3x squared, plus 5x, minus 2.  Here, 'a' is 3, 'b' is 5, and 'c' is -2.") as tracker:
            example = MathTex("3x^2 + 5x - 2").scale(1.5).shift(DOWN*2)
            a = Arrow(start=example[0].get_center() + UP*0.5, end=example[0].get_center(), color=BLUE)
            b = Arrow(start=example[3].get_center() + UP*0.5, end=example[3].get_center(), color=GREEN)
            c = Arrow(start=example[6].get_center() + UP*0.5, end=example[6].get_center(), color=RED)
            a_label = Text("a = 3", color=BLUE).next_to(a, UP)
            b_label = Text("b = 5", color=GREEN).next_to(b, UP)
            c_label = Text("c = -2", color=RED).next_to(c, UP)
            self.play(Write(example), run_time=tracker.duration/2)
            self.play(Create(a), Write(a_label), Create(b), Write(b_label), Create(c), Write(c_label), run_time=tracker.duration/2)

        self.wait(1)

        # Importance of x squared
        with self.voiceover(text="The key thing that makes it quadratic is that 'x' is squared, meaning it's multiplied by itself.") as tracker:
            x_squared = MathTex("x^2").scale(2).next_to(text, DOWN)
            self.play(Write(x_squared), run_time=tracker.duration)

        self.wait(1)

        # Applications
        with self.voiceover(text="Now, why are these expressions useful?") as tracker:
            self.play(FadeOut(x_squared), FadeOut(a), FadeOut(b), FadeOut(c), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label), run_time=tracker.duration/2)
            self.play(example.animate.shift(UP*2), run_time=tracker.duration/2)

        with self.voiceover(text="They pop up in tons of real-world situations!") as tracker:
            pass

        with self.voiceover(text="Think about the path a ball takes when you throw it, or the shape of a satellite dish.") as tracker:
            ball = Circle(radius=0.2, color=YELLOW).shift(LEFT*3 + DOWN*2)
            path = ParametricFunction(lambda t: np.array([t, -0.5*t**2 + 2*t - 1, 0]), t_min=-1, t_max=5, color=RED)
            dish = Arc(radius=1, start_angle=PI/4, angle=PI/2, color=GREY).shift(RIGHT*3 + DOWN*2)
            self.play(Create(ball), run_time=tracker.duration/3)
            self.play(MoveAlongPath(ball, path), run_time=tracker.duration/3)
            self.play(Create(dish), run_time=tracker.duration/3)

        self.wait(1)

        # Conclusion
        with self.voiceover(text="So, that's a quick look at quadratic expressions. They might seem a bit abstract at first, but trust me, they're everywhere, making our world go round.") as tracker:
            self.play(FadeOut(ball), FadeOut(path), FadeOut(dish), FadeOut(example), run_time=tracker.duration)

        self.wait(0.5)

        with self.voiceover(text="I hope you learned something new today!") as tracker:
            pass

        self.wait()
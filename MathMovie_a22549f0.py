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
        with self.voiceover(text="Hey there! Today, we're diving into the world of quadratic expressions.") as tracker:
            text = Text("Quadratic Expressions", font_size=48).shift(UP*2)
            self.play(Write(text), run_time=tracker.duration)

        self.wait(0.5)
        self.play(FadeOut(text))

        # Basic form
        with self.voiceover(text="A quadratic expression is like a math sentence with a special ingredient: a variable squared, usually represented by 'x²'.") as tracker:
            x_squared = MathTex("x^2").scale(1.5)
            self.play(Write(x_squared), run_time=tracker.duration)
        self.wait(0.5)
        
        with self.voiceover(text="It looks a bit like this. This 'x²' is what makes an expression quadratic.") as tracker:
            self.play(x_squared.animate.shift(LEFT*3), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="A full quadratic expression has the form ax² + bx + c.") as tracker:
            quadratic_form = MathTex("ax^2 + bx + c").scale(1.5).next_to(x_squared, RIGHT*3)
            self.play(Write(quadratic_form), run_time=tracker.duration)
        self.wait(0.5)

        # Coefficients
        with self.voiceover(text="Here, 'a', 'b', and 'c' are like secret codes, called coefficients. They tell us how strong each part of the expression is.") as tracker:
            a_brace = Brace(quadratic_form[0:2], UP)
            b_brace = Brace(quadratic_form[3:5], UP)
            c_brace = Brace(quadratic_form[6], UP)
            a_text = a_brace.get_text("a")
            b_text = b_brace.get_text("b")
            c_text = c_brace.get_text("c")
            self.play(
                FadeIn(a_brace), FadeIn(a_text),
                FadeIn(b_brace), FadeIn(b_text),
                FadeIn(c_brace), FadeIn(c_text),
                run_time=tracker.duration
            )
        self.wait(0.5)

        # Example
        with self.voiceover(text="For instance, in the expression 3x² + 2x + 1, our secret codes are a = 3, b = 2, and c = 1.") as tracker:
            example = MathTex("3x^2 + 2x + 1").scale(1.5).shift(DOWN*2)
            self.play(Write(example), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="These coefficients can be any number, positive, negative, or even zero.") as tracker:
            pass
        self.wait(0.5)

        # Importance
        with self.voiceover(text="Quadratic expressions are like superheroes in math. They help us understand things that go up and then come down, like a ball being thrown, or describe the shapes of parabolas.") as tracker:
            self.play(FadeOut(x_squared), FadeOut(quadratic_form), FadeOut(a_brace), FadeOut(b_brace), FadeOut(c_brace), FadeOut(a_text), FadeOut(b_text), FadeOut(c_text),FadeOut(example), run_time=tracker.duration)

        # Outro
        with self.voiceover(text="So, that's quadratic expressions in a nutshell! Remember, they are all about that x², and they are pretty awesome.") as tracker:
            text = Text("Pretty Awesome!", font_size=48).shift(UP*2)
            self.play(Write(text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(text))

        self.wait()
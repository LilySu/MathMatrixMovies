from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class OnePlusOne(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual"
            )
        )

        # Title
        title = Text("1 + 1 = Fun with Math!", font="Comic Sans", font_size=60, color=BLUE).shift(UP)
        title.set_color_by_gradient(BLUE, GREEN) # Gradient effect
        self.play(Write(title))
        with self.voiceover(text="Do you love apples? Let's have some fun with math using apples!"):
            self.wait(2)
        self.play(FadeOut(title))

        # Apples
        apple1 = Circle(radius=1, color=RED, fill_opacity=1).shift(3 * LEFT)
        apple2 = Circle(radius=1, color=RED, fill_opacity=1).shift(3 * UP)

        with self.voiceover(text="We'll start with one red apple."):
            self.play(FadeIn(apple1))
            self.wait(1)

        with self.voiceover(text="Now, imagine another apple drops in!"):
            self.play(apple2.animate.shift(3 * LEFT).set_run_time(0.8), rate_func=bounce)
            self.wait(1)

        # Question Mark
        question_mark = Text("?", font_size=80, color=YELLOW).next_to(VGroup(apple1, apple2), UP)
        self.play(FadeIn(question_mark))
        with self.voiceover(text="How many apples are there now?"):
            self.play(Wiggle(question_mark))
            self.wait(2)

        # Counting
        one_1 = Text("1", font_size=60).next_to(apple1, DOWN)
        plus = Text("+", font_size=60).next_to(apple1, RIGHT)
        one_2 = Text("1", font_size=60).next_to(apple2, DOWN)
        equals = Text("=", font_size=60).next_to(apple2, RIGHT)
        two = Text("2", font_size=80).next_to(equals, RIGHT)

        box1 = SurroundingRectangle(VGroup(apple1, one_1), color=WHITE, corner_radius=0.2)
        box2 = SurroundingRectangle(VGroup(apple2, one_2), color=WHITE, corner_radius=0.2)

        with self.voiceover(text="Let's count them together. One apple..."):
            self.play(FadeIn(one_1), FadeIn(box1))
            self.wait(1)

        with self.voiceover(text="...Plus one apple..."):
            self.play(FadeOut(box1), FadeIn(plus), FadeIn(one_2), FadeIn(box2))
            self.wait(1)

        with self.voiceover(text="...Equals..."):
            self.play(FadeOut(box2), FadeIn(equals))
            self.wait(1)

        with self.voiceover(text="Two apples!"):
            self.play(FadeOut(question_mark), FadeIn(two))
            self.play(Wiggle(two))
            self.wait(2)

        # Equation
        equation_bg = Rectangle(width=5, height=1, color=GREEN, fill_opacity=0.2).next_to(VGroup(apple1, apple2), DOWN, buff=1)
        equation = MathTex("1 + 1 = 2", font_size=60).next_to(VGroup(apple1, apple2), DOWN, buff=1.5)
        self.play(FadeIn(equation_bg), Write(equation))
        with self.voiceover(text="That's right! 1 + 1 = 2."):
            self.wait(2)

        with self.voiceover(text="Math can be fun and easy!"):
            self.wait(2)

        # Outro
        outro_text = Text("See you next time!", font="Comic Sans", font_size=40, color=BLUE).shift(DOWN)
        with self.voiceover(text="Thanks for joining us! We'll see you next time for more exciting math adventures!"):
            self.play(FadeOut(VGroup(apple1, apple2, one_1, plus, one_2, equals, two, equation, equation_bg)),
                      FadeIn(outro_text))
            self.wait(1)
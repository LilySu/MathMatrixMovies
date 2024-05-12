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
        title = Text("1 + 1 = Fun with Math!", font_size=60, color=BLUE)
        self.play(Write(title))
        with self.voiceover(text="Welcome, everyone, to a super easy math lesson: let's learn about 1 + 1!"):
            self.wait(2) 
        self.play(FadeOut(title))

        # Apples
        apple1 = Circle(radius=1, color=RED, fill_opacity=1).shift(3 * LEFT)
        apple2 = Circle(radius=1, color=RED, fill_opacity=1).shift(3 * RIGHT)

        with self.voiceover(text="We'll start with one red apple. Yum!"):
            self.play(Create(apple1))
            self.wait(1)

        with self.voiceover(text="Now, imagine you get another delicious red apple."):
            self.play(apple2.animate.shift(3*LEFT))
            self.wait(1)

        # Question Mark
        question_mark = Text("?", font_size=80).next_to(VGroup(apple1, apple2), UP)
        self.play(Write(question_mark))
        with self.voiceover(text="How many apples do you have now?"):
            self.play(Wiggle(question_mark))
            self.wait(2)

        # Counting 
        one_1 = Text("1", font_size=60).next_to(apple1, DOWN)
        plus = Text("+", font_size=60).next_to(apple1, RIGHT)
        one_2 = Text("1", font_size=60).next_to(apple2, DOWN)
        equals = Text("=", font_size=60).next_to(apple2, RIGHT)
        two = Text("2", font_size=80).next_to(equals, RIGHT)

        with self.voiceover(text="Let's count them together! One apple..."):
            self.play(Write(one_1))
            self.wait(1)

        with self.voiceover(text="...Plus one apple..."):
            self.play(FadeIn(plus), Write(one_2))
            self.wait(1)
        
        with self.voiceover(text="...Equals..."):
            self.play(Write(equals))
            self.wait(1)

        with self.voiceover(text="Two apples!"):
            self.play(FadeOut(question_mark), Write(two))
            self.play(Wiggle(two))
            self.wait(2)

        # Equation
        equation = MathTex("1 + 1 = 2", font_size=60).next_to(VGroup(apple1, apple2), DOWN, buff=1.5)
        self.play(Write(equation))
        with self.voiceover(text="That’s right!  1 + 1 = 2."):
            self.wait(2)

        with self.voiceover(text="See? Math can be fun and easy!"):
            self.wait(2)

        # Outro
        with self.voiceover(text="Thanks for joining us, and we'll see you next time for more exciting math adventures!"):
            self.play(FadeOut(VGroup(apple1, apple2, one_1, plus, one_2, equals, two, equation)))
            self.wait(1)
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class AdditionExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )

        # Title
        title = Text("Understanding Addition: 3 + 7 = 10", font_size=40, color=BLUE).move_to(ORIGIN)
        with self.voiceover(text="Welcome! Today, we're going to explore the exciting world of addition, specifically the equation 3 + 7 = 10.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(title))

        # Apples
        red_apples = VGroup(*[Dot(radius=0.2, color=RED) for _ in range(3)]).arrange(RIGHT, buff=0.5).shift(3 * LEFT)
        green_apples = VGroup(*[Dot(radius=0.2, color=GREEN) for _ in range(7)]).arrange(RIGHT, buff=0.5).shift(3 * RIGHT)

        with self.voiceover(text="Let's imagine we have three delicious red apples.") as tracker:
            self.play(Create(red_apples), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="Now, let's add seven juicy green apples to our collection.") as tracker:
            self.play(Create(green_apples), run_time=tracker.duration)
        self.wait(0.5)

        plus_sign = Text("+", font_size=60, color=YELLOW).move_to(ORIGIN)

        with self.voiceover(text="The plus sign tells us to combine our groups of apples.") as tracker:
            self.play(Write(plus_sign), run_time=tracker.duration)
        self.wait(0.5)

        all_apples = VGroup(red_apples, green_apples).arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        self.play(Transform(red_apples, all_apples), Transform(green_apples, all_apples), FadeOut(plus_sign))

        with self.voiceover(text="Now, if we count all the apples together, how many do we have?") as tracker:
            self.play(run_time=tracker.duration)
        self.wait(0.5)

        total_number = Text("10", font_size=60, color=ORANGE).next_to(all_apples, UP)
        self.play(Write(total_number))
        self.wait(0.5)

        with self.voiceover(text="That's right! We have ten apples in total. So, 3 + 7 equals 10!") as tracker:
            self.play(run_time=tracker.duration)
        self.wait(0.5)

        equation = MathTex("3 + 7 = 10", font_size=40).next_to(all_apples, DOWN)
        self.play(Write(equation))
        self.wait(1)

        with self.voiceover(text="See? Addition is all about combining things together and finding the total number.") as tracker:
            self.play(run_time=tracker.duration)
        self.wait(1)

        self.play(FadeOut(all_apples), FadeOut(total_number), FadeOut(equation))

        # Outro
        outro = Text("Thanks for learning with us!", font_size=40, color=BLUE).move_to(ORIGIN)

        with self.voiceover(text="We hope you enjoyed learning about addition. Keep exploring and have fun with math!") as tracker:
            self.play(Write(outro), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(outro))
        self.wait(0.5)
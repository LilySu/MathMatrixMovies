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
        title = Text("Let's Learn Addition!", font="Comic Sans MS", font_size=48, color=ORANGE)
        self.play(Write(title))
        self.wait(0.5)

        with self.voiceover(text="Hi everyone! Let's learn about adding numbers!") as tracker:
            self.wait(tracker.duration)

        self.play(FadeOut(title))

        # Stars
        red_stars = VGroup(*[Star(color=RED, fill_opacity=1, scale_factor=0.5).shift(2*i*LEFT) for i in range(3)])
        green_stars = VGroup(*[Star(color=GREEN, fill_opacity=1, scale_factor=0.5).shift(2*i*RIGHT) for i in range(5)])

        self.play(LaggedStart(*[FadeIn(star, scale=1.2, rate_func=there_and_back) for star in red_stars], lag_ratio=0.2))
        self.play(LaggedStart(*[FadeIn(star, scale=1.2, rate_func=there_and_back) for star in green_stars], lag_ratio=0.2))

        with self.voiceover(text="We have three red stars here, one, two, three!") as tracker:
            for i in range(3):
                self.play(red_stars[i].animate.scale(1.5), run_time=tracker.duration/3)

        # Number 3
        number_3 = Text("3", font_size=48, color=RED).next_to(red_stars, DOWN)
        self.play(Write(number_3))

        with self.voiceover(text="And we have five green stars here, one, two, three, four, five!") as tracker:
            for i in range(5):
                self.play(green_stars[i].animate.scale(1.5), run_time=tracker.duration/5)

        # Number 5
        number_5 = Text("5", font_size=48, color=GREEN).next_to(green_stars, DOWN)
        self.play(Write(number_5))

        with self.voiceover(text="Let's count all the stars together!") as tracker:
            self.wait(tracker.duration)

        # Combining Stars
        all_stars = VGroup(*red_stars, *green_stars).arrange(RIGHT, buff=0.5).center()
        self.play(
            LaggedStart(
                *[
                    star.animate.move_to(target).scale(1.2).rate_func(there_and_back)
                    for star, target in zip(red_stars, all_stars[:3])
                ],
                lag_ratio=0.2
            ), 
            LaggedStart(
                *[
                    star.animate.move_to(target).scale(1.2).rate_func(there_and_back)
                    for star, target in zip(green_stars, all_stars[3:])
                ],
                lag_ratio=0.2
            )
        )

        with self.voiceover(text="One, two, three, four, five, six, seven, eight!") as tracker:
            for i in range(8):
                self.play(all_stars[i].animate.scale(1.5), run_time=tracker.duration/8)

        # Equation
        equation = Tex("3", "+", "5", "=", "8", font_size=48).next_to(all_stars, DOWN)
        equation[0].set_color(RED)
        equation[2].set_color(GREEN)
        equation[1].set_color(BLUE)
        equation[3].set_color(BLUE)
        equation[4].set_color(BLUE)

        self.play(Write(equation))

        with self.voiceover(text="Three stars plus five stars equals eight stars!") as tracker:
            self.wait(tracker.duration)

        self.wait(0.5)
        self.play(FadeOut(all_stars), FadeOut(number_3), FadeOut(number_5), FadeOut(equation))

        # Outro
        outro = Text("We learned that 3 + 5 equals 8! You did great!", font="Comic Sans MS", font_size=48, color=ORANGE)
        self.play(Write(outro))
        self.wait(0.5)
        with self.voiceover(text="We learned that 3 + 5 equals 8! You did great!") as tracker:
            self.wait(tracker.duration)
        self.play(FadeOut(outro))
        self.wait()
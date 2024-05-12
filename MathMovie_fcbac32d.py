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
        title = Text("Let's Learn Addition!", font="Comic Sans MS").scale(1.5)
        with self.voiceover(text="Let's learn addition!") as tracker:
            self.play(FadeIn(title), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(title))

        # Apples
        red_apples = VGroup(*[Circle(color=RED, fill_opacity=1).scale(0.3) for _ in range(3)]
                          ).arrange(RIGHT, buff=0.5).shift(3*LEFT)
        green_apples = VGroup(*[Circle(color=GREEN, fill_opacity=1).scale(0.3) for _ in range(5)]
                            ).arrange(RIGHT, buff=0.5).shift(3*RIGHT)

        with self.voiceover(text="Imagine you have three juicy red apples.") as tracker:
            self.play(Create(red_apples), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="And then your friend gives you five yummy green apples.") as tracker:
            self.play(Create(green_apples), run_time=tracker.duration)
        self.wait(0.5)

        # Plus sign
        plus_sign = Text("+").scale(2).shift(UP)

        with self.voiceover(text="When we add things together, we use this sign, a plus sign.") as tracker:
            self.play(FadeIn(plus_sign), run_time=tracker.duration)
        self.wait(0.5)

        # Combining apples
        all_apples = VGroup(red_apples, green_apples).arrange(RIGHT, buff=0.5)

        with self.voiceover(text="Now, let's count all the apples together. One, two, three, four, five, six, seven, eight!") as tracker:
            self.play(
                FadeOut(plus_sign),
                red_apples.animate.shift(3*RIGHT),
                green_apples.animate.shift(3*LEFT),
                run_time=tracker.duration
            )
        self.wait(0.5)

        # Numbers
        three_text = Text("3").scale(1.5).next_to(red_apples, UP)
        five_text = Text("5").scale(1.5).next_to(green_apples, UP)
        equals_sign = Text("=").scale(1.5).next_to(all_apples, RIGHT)
        eight_text = Text("8").scale(1.5).next_to(equals_sign, RIGHT)

        with self.voiceover(text="So, three apples plus five apples equals eight apples!") as tracker:
            self.play(
                FadeIn(three_text), 
                FadeIn(five_text), 
                FadeIn(equals_sign), 
                FadeIn(eight_text), 
                run_time=tracker.duration
            )
        self.wait(0.5)

        # Formula
        formula = Tex("3 + 5 = 8").scale(2).next_to(all_apples, DOWN)
        self.play(Write(formula))
        self.wait(0.5)

        with self.voiceover(text="That's addition! You learned it!") as tracker:
            self.play(FadeOut(all_apples), FadeOut(three_text), FadeOut(five_text), FadeOut(equals_sign), FadeOut(eight_text), run_time=tracker.duration)
        self.wait(0.5)

        # Outro
        outro = Text("The End", font="Comic Sans MS").scale(1.5)
        with self.voiceover(text="The End") as tracker:
            self.play(FadeIn(outro), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(outro))
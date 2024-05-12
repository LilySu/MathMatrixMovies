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
        title = Text("Let's Learn Addition!", font_size=48)
        self.play(Write(title))
        self.wait(0.5)

        with self.voiceover(text="Hi everyone! Let's learn about adding numbers!") as tracker:
            self.wait(tracker.duration)

        self.play(FadeOut(title))

        # Scene 1: Apples
        red_apples = VGroup(*[Circle(radius=0.5, color=RED).shift(2*i*LEFT) for i in range(3)])
        green_apples = VGroup(*[Circle(radius=0.5, color=GREEN).shift(2*i*RIGHT) for i in range(5)])

        self.play(FadeIn(red_apples))
        self.play(FadeIn(green_apples))

        with self.voiceover(text="We have three red apples here, one, two, three!") as tracker:
            self.wait(tracker.duration)

        # Scene 2: Number 3
        number_3 = Text("3", font_size=48).next_to(red_apples, DOWN)
        self.play(Write(number_3))

        with self.voiceover(text="And we have five green apples here, one, two, three, four, five!") as tracker:
            self.wait(tracker.duration)

        # Scene 3: Number 5
        number_5 = Text("5", font_size=48).next_to(green_apples, DOWN)
        self.play(Write(number_5))

        with self.voiceover(text="Let's count all the apples together!") as tracker:
            self.wait(tracker.duration)

        # Scene 4: Apples together
        all_apples = VGroup(*red_apples, *green_apples).arrange(RIGHT, buff=0.5)
        self.play(Transform(red_apples, all_apples[:3]), Transform(green_apples, all_apples[3:]))

        with self.voiceover(text="One, two, three, four, five, six, seven, eight!") as tracker:
            self.wait(tracker.duration)

        # Scene 5: Equation
        equation = Tex("3 + 5 = 8", font_size=48).next_to(all_apples, DOWN)
        self.play(Write(equation))

        with self.voiceover(text="Three apples plus five apples equals eight apples!") as tracker:
            self.wait(tracker.duration)

        self.wait(0.5)
        self.play(FadeOut(all_apples), FadeOut(number_3), FadeOut(number_5), FadeOut(equation))

        # Outro
        outro = Text("We learned that 3 + 5 equals 8! You did great!", font_size=48)
        self.play(Write(outro))
        self.wait(0.5)
        with self.voiceover(text="We learned that 3 + 5 equals 8! You did great!") as tracker:
            self.wait(tracker.duration)
        self.play(FadeOut(outro))
        self.wait()
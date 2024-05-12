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
        title = Text("Let's learn addition!", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Scene 1: Three apples
        apple = ImageMobject(np.uint8([[255,0,0]]))
        apple.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
        apple.height = 0.5
        apples = VGroup(*[apple.copy() for _ in range(3)]).arrange(RIGHT, buff=0.5)
        self.play(FadeIn(apples))

        with self.voiceover(text="We have 3 apples.") as tracker:
            self.wait(tracker.duration)

        # Scene 2: Five more apples
        more_apples = VGroup(*[apple.copy() for _ in range(5)]).arrange(RIGHT, buff=0.5)
        more_apples.next_to(apples, RIGHT, buff=1)
        self.play(FadeIn(more_apples))

        with self.voiceover(text="And then we get 5 more apples.") as tracker:
            self.wait(tracker.duration)

        # Scene 3: Combine the apples
        all_apples = VGroup(apples, more_apples).arrange(RIGHT, buff=0.5)
        self.play(Transform(apples, all_apples[:3]))
        self.play(Transform(more_apples, all_apples[3:]))

        # Equation
        equation = MathTex("3", "+", "5", "=", "8").scale(2)
        equation.next_to(all_apples, DOWN)

        with self.voiceover(text="So if we add them together, how many apples do we have?") as tracker:
            self.wait(tracker.duration)

        self.play(Write(equation))

        with self.voiceover(text="That's right! We have 8 apples in total!") as tracker:
            self.wait(tracker.duration)

        # Outro
        outro = Text("Thanks for learning with us!", font_size=40)
        self.play(FadeOut(all_apples), FadeOut(equation))
        self.play(Write(outro))
        self.wait(2)
        self.play(FadeOut(outro))
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class AddingNumbers(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual"
            )
        )

        # Title
        title = Text("Adding Numbers!", font_size=60, color=BLUE).to_edge(UP)
        with self.voiceover(text="Adding Numbers!") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        self.wait(0.5)

        # Scene 1: Introducing addition
        with self.voiceover(text="Hi everyone! Today we're going to learn how to add numbers.") as tracker:
            self.wait(tracker.duration)
        with self.voiceover(text="Adding means putting things together and counting how many we have in total.") as tracker:
            self.wait(tracker.duration)

        self.play(FadeOut(title))

        # Scene 2: Showing 3 apples
        apples_1 = VGroup(*[Circle(radius=0.3, color=RED, fill_opacity=1) for _ in range(3)])
        apples_1.arrange(RIGHT, buff=0.5).to_edge(LEFT).shift(DOWN)
        with self.voiceover(text="Let's start with 3.") as tracker:
            self.play(Create(apples_1), run_time=tracker.duration)
        with self.voiceover(text="We have 3 juicy red apples!") as tracker:
            self.wait(tracker.duration)

        # Scene 3: Adding 5 more apples
        apples_2 = VGroup(*[Circle(radius=0.3, color=RED, fill_opacity=1) for _ in range(5)])
        apples_2.arrange(RIGHT, buff=0.5).next_to(apples_1, RIGHT, buff=0.5)
        with self.voiceover(text="Now, let's add 5 more apples.") as tracker:
            self.play(Create(apples_2), run_time=tracker.duration)

        # Scene 4: Counting all the apples
        all_apples = VGroup(apples_1, apples_2)
        with self.voiceover(text="Look! Now we have a bunch of apples. Let's count them all together.") as tracker:
            self.wait(tracker.duration)
        for i, apple in enumerate(all_apples):
            with self.voiceover(text=str(i+1)):
                self.play(Flash(apple, color=YELLOW, flash_radius=0.5))
                self.wait(0.2)

        # Scene 5: Showing the equation
        equation = MathTex("3", "+", "5", "=", "8").scale(2).to_edge(DOWN)
        with self.voiceover(text="So, 3 apples plus 5 apples equals 8 apples!") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        self.wait(1)

        # Outro
        self.play(FadeOut(all_apples), FadeOut(equation))
        with self.voiceover(text="You did great! Adding numbers is fun and easy. See you next time!") as tracker:
            self.wait(tracker.duration)
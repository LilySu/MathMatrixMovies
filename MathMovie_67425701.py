from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class MultiplicationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )

        # Show three groups of two apples
        apple = ImageMobject(f"{manim.__path__[0]}/files/assets/raster_images/apple.png").scale(0.2)

        apples_group1 = VGroup(*[apple.copy() for _ in range(2)]).arrange(RIGHT)
        apples_group2 = apples_group1.copy().next_to(apples_group1, DOWN)
        apples_group3 = apples_group1.copy().next_to(apples_group2, DOWN)
        all_apples = VGroup(apples_group1, apples_group2, apples_group3).move_to(ORIGIN)

        # Introduction
        with self.voiceover(text="Let's learn about multiplication!") as tracker:
            self.play(Write(Text("Multiplication").scale(1.5)), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(Text("Multiplication").scale(1.5)))

        # Explain the concept of groups
        with self.voiceover(text="Imagine you have three groups of apples.") as tracker:
            self.play(FadeIn(all_apples), run_time=tracker.duration)

        # Highlight each group
        with self.voiceover(text="Here's one group, two groups, and three groups.") as tracker:
            self.play(
                Succession(
                    ApplyWave(apples_group1),
                    ApplyWave(apples_group2),
                    ApplyWave(apples_group3),
                ),
                run_time=tracker.duration
            )

        # Explain the number of objects in each group
        with self.voiceover(text="Each group has two apples.") as tracker:
            self.play(
                Succession(
                    Indicate(apples_group1[0]),
                    Indicate(apples_group1[1]),
                    Indicate(apples_group2[0]),
                    Indicate(apples_group2[1]),
                    Indicate(apples_group3[0]),
                    Indicate(apples_group3[1]),
                ),
                run_time=tracker.duration
            )

        # Introduce multiplication as a shortcut for repeated addition
        with self.voiceover(text="Instead of adding 2+2+2, we can use multiplication.") as tracker:
            self.play(Write(MathTex("2 + 2 + 2").scale(1.5)), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(MathTex("2 + 2 + 2").scale(1.5)))

        # Write the multiplication equation
        with self.voiceover(text="We have 3 groups times 2 apples in each group.") as tracker:
            self.play(Write(MathTex("3 \\times 2").scale(1.5)), run_time=tracker.duration)

        # Count the total number of apples
        with self.voiceover(text="That equals six apples!") as tracker:
            self.play(
                ReplacementTransform(MathTex("3 \\times 2").scale(1.5), MathTex("3 \\times 2 = 6").scale(1.5)),
                run_time=tracker.duration
            )
            self.play(Indicate(all_apples), run_time=tracker.duration)

        self.wait(2)
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class AdditionScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

        # Create apples
        apples = VGroup(*[Circle(radius=0.3, color=RED) for _ in range(9)])
        apples.arrange_in_grid(rows=2, buff=0.5)

        # Show 5 apples
        with self.voiceover(text="Imagine you have 5 yummy apples!") as tracker:
            self.play(Create(apples[:5]), run_time=tracker.duration)

        # Show 4 more apples
        with self.voiceover(text="Your friend gives you 4 more apples!") as tracker:
            self.play(Create(apples[5:]), run_time=tracker.duration)

        # Group all apples
        with self.voiceover(text="Now, let's count all the apples together!") as tracker:
            self.play(
                apples.animate.arrange_in_grid(rows=1, buff=0.5), 
                run_time=tracker.duration
            )

        # Count the apples
        for i in range(9):
            with self.voiceover(text=f"{i+1}") as tracker:
                self.play(Flash(apples[i]), run_time=tracker.duration)

        # Final count
        with self.voiceover(text="We have 9 apples! So 5 plus 4 equals 9!") as tracker:
            self.play(Circumscribe(apples), run_time=tracker.duration)

        self.wait()
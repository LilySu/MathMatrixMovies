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

        # Define the math problem and audience
        math_problem = "7 + 2 = 9"
        audience_type = "a 5 year old"

        # Create circles
        circles = VGroup(*[Circle(radius=0.3, color=RED) for _ in range(9)])
        circles.arrange(RIGHT, buff=0.5)

        # Show 7 circles
        with self.voiceover(text=f"Let's learn about {math_problem}. Imagine you have 7 yummy cookies!") as tracker:
            self.play(Create(circles[:7]), run_time=tracker.duration)

        # Show 2 more circles
        with self.voiceover(text="Your friend gives you 2 more cookies!") as tracker:
            self.play(Create(circles[7:]), run_time=tracker.duration)

        # Emphasize counting all circles
        with self.voiceover(text="Wow, that's a lot of cookies! Let's count them all, one by one.") as tracker:
            self.play(Wiggle(circles), run_time=tracker.duration)

        # Count the circles, highlighting each one
        for i in range(9):
            with self.voiceover(text=f"{i+1}") as tracker:
                self.play(
                    circles[i].animate.set_fill(YELLOW, opacity=1.0),
                    run_time=tracker.duration / 2
                )
                self.play(
                    circles[i].animate.set_fill(RED, opacity=1.0),
                    run_time=tracker.duration / 2
                )

        # Final count and equation
        with self.voiceover(text=f"We have 9 cookies in total! So {math_problem}.") as tracker:
            self.play(Circumscribe(circles), run_time=tracker.duration)

        self.wait()
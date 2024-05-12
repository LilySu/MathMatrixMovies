import numpy as np
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class FivePlusThree(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

        # Create apples
        apples = VGroup(*[Circle(radius=0.3, color=RED) for _ in range(8)])
        apples.arrange(RIGHT, buff=0.5)

        # Show 5 apples
        five_apples = apples[:5]
        with self.voiceover(text="Let's say we have five apples.") as tracker:
            self.play(Create(five_apples), run_time=tracker.duration)

        # Show 3 more apples
        three_apples = apples[5:]
        with self.voiceover(text="And then we get three more apples.") as tracker:
            self.play(Create(three_apples), run_time=tracker.duration)

        # Count all the apples
        with self.voiceover(text="Let's count how many apples we have now.") as tracker:
            self.play(
                apples.animate.shift(UP),
                run_time=tracker.duration
            )
            for i in range(len(apples)):
                self.play(Flash(apples[i], color=YELLOW), run_time=0.2)
                # Generate a click sound using a numpy array
                rate = 44100  # Samples per second
                duration = 0.1  # Seconds
                frequency = 500  # Hz
                t = np.linspace(0, duration, int(rate * duration), endpoint=False)
                click_sound = 0.5 * np.sin(2 * np.pi * frequency * t) 
                self.add_sound(click_sound, gain=-10)

        # Display the equation
        equation = Tex("5 + 3 = 8").scale(2)
        with self.voiceover(text="So five plus three equals eight!") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        self.wait()
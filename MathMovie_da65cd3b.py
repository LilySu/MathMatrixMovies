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
        apples_5 = VGroup(*[Circle(radius=0.3, color=RED, fill_opacity=1) for _ in range(5)])
        apples_3 = VGroup(*[Circle(radius=0.3, color=RED, fill_opacity=1) for _ in range(3)])
        
        # Arrange the apples
        apples_5.arrange(RIGHT, buff=0.5).to_edge(LEFT)
        apples_3.arrange(RIGHT, buff=0.5).next_to(apples_5, RIGHT, buff=2)

        # Display the apples and narrate
        with self.voiceover(text="Imagine you have five delicious apples.") as tracker:
            self.play(Create(apples_5), run_time=tracker.duration)
        
        with self.voiceover(text="And then, your friend gives you three more apples.") as tracker:
            self.play(Create(apples_3), run_time=tracker.duration)

        # Move all apples together
        all_apples = VGroup(apples_5, apples_3)
        all_apples.generate_target()
        all_apples.target.arrange(RIGHT, buff=0.5).move_to(ORIGIN)

        with self.voiceover(text="Now, let's count all the apples together.") as tracker:
            self.play(MoveToTarget(all_apples), run_time=tracker.duration)

        # Count apples
        for i in range(8):
            with self.voiceover(text=f"{i+1}") as tracker:
                self.play(Flash(all_apples[i], color=YELLOW), run_time=tracker.duration)

        with self.voiceover(text="So, five apples plus three apples equals eight apples!") as tracker:
            self.play(FadeOut(all_apples), run_time=tracker.duration)

        # Display the equation
        equation = MathTex("5 + 3 = 8").scale(2)
        self.play(Write(equation))
        self.wait(2)

        with self.voiceover(text="You got it!") as tracker:
            self.play(FadeOut(equation), run_time=tracker.duration)
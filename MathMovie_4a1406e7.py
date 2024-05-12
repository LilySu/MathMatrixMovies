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
        
        # Introduction
        with self.voiceover(text="Let's learn about multiplication!") as tracker:
            text = Text("Multiplication", font_size=48).shift(UP * 2)
            self.play(Write(text), run_time=tracker.duration)

        self.wait(0.5)
        self.play(FadeOut(text))
        
        # Scenario: Apples in baskets
        with self.voiceover(text="Imagine you have 3 baskets.") as tracker:
            baskets = VGroup(*[
                Rectangle(width=1.5, height=1, color=BLUE).shift(i * RIGHT * 2)
                for i in range(3)
            ])
            self.play(Create(baskets), run_time=tracker.duration)
        
        self.wait(0.5)

        with self.voiceover(text="And each basket has 4 apples.") as tracker:
            apples = VGroup()
            for basket in baskets:
                row1 = VGroup(*[Dot(radius=0.15, color=RED).next_to(basket, UP, buff=0.2) for _ in range(2)])
                row2 = VGroup(*[Dot(radius=0.15, color=RED).next_to(basket, DOWN, buff=0.2) for _ in range(2)])
                apples.add(row1, row2)
            self.play(Create(apples), run_time=tracker.duration)

        self.wait(0.5)
        
        # Multiplication as repeated addition
        with self.voiceover(text="We can count all the apples one by one.") as tracker:
            self.play(
                *[Flash(apple, color=YELLOW) for apple in apples], 
                run_time=tracker.duration
            )

        with self.voiceover(text="But there's a faster way: multiplication!") as tracker:
            pass

        self.wait(0.5)

        with self.voiceover(text="We have 3 baskets, and each basket has 4 apples.") as tracker:
            self.play(Flash(baskets), Flash(apples), run_time=tracker.duration)

        self.wait(0.5)

        with self.voiceover(text="So, we can write this as 3 times 4.") as tracker:
            equation = MathTex("3 \\times 4").next_to(baskets, DOWN)
            self.play(Write(equation), run_time=tracker.duration)

        self.wait(0.5)

        with self.voiceover(text="Which equals 12! We have 12 apples in total.") as tracker:
            result = MathTex("= 12").next_to(equation, RIGHT)
            self.play(Write(result), run_time=tracker.duration)
            self.play(Flash(apples), run_time=tracker.duration)

        self.wait(1)

        # Conclusion
        with self.voiceover(text="That's multiplication!  It's a quick way to add the same number many times.") as tracker:
            self.play(FadeOut(baskets, apples, equation, result), run_time=tracker.duration)

        self.wait()
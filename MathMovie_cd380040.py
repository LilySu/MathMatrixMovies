from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class AdditionExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual"
            )
        )

        # Title
        title = Text("Adding Numbers: 3 + 4", font_size=48).to_edge(UP)
        with self.voiceover(text="Today, we're going to learn about adding numbers. Let's start with a simple example: 3 plus 4.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        self.wait(0.5)

        # Equation
        equation = MathTex("3 + 4 = ?").shift(UP)
        self.play(FadeIn(equation))
        self.wait(0.5)

        # Apples
        red_apples = VGroup(*[Circle(radius=0.3, color=RED, fill_opacity=1) for _ in range(3)]).arrange(RIGHT, buff=0.5).to_edge(LEFT).shift(DOWN)
        green_apples = VGroup(*[Circle(radius=0.3, color=GREEN, fill_opacity=1) for _ in range(4)]).arrange(RIGHT, buff=0.5).to_edge(RIGHT).shift(DOWN)

        with self.voiceover(text="Imagine you have three apples.") as tracker:
            self.play(Create(red_apples), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="And then, your friend gives you four more apples.") as tracker:
            self.play(Create(green_apples), run_time=tracker.duration)
        self.wait(0.5)

        # Combine apples
        all_apples = VGroup(*red_apples, *green_apples).arrange(RIGHT, buff=0.5)
        with self.voiceover(text="To find out how many apples you have in total, you need to add the two groups together.") as tracker:
            self.play(
                red_apples.animate.move_to(all_apples.get_center()),
                green_apples.animate.move_to(all_apples.get_center()),
                run_time=tracker.duration
            )
        self.wait(0.5)

        # Show answer
        answer = MathTex("7").move_to(equation[5])
        with self.voiceover(text="When we combine the three apples and the four apples, we have a total of seven apples.") as tracker:
            self.play(ReplacementTransform(equation[5], answer), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="So, 3 plus 4 equals 7.") as tracker:
            self.play(all_apples.animate.arrange_in_grid(rows=1, buff=0.5), run_time=tracker.duration)
        self.wait(1)

        # Outro
        with self.voiceover(text="That's how we add numbers. See you next time!") as tracker:
            self.play(FadeOut(VGroup(title, equation, all_apples)), run_time=tracker.duration)
        self.wait(1)
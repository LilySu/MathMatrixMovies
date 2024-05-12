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
        title = Text("Let's learn addition!", font_size=40).set_color(BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Scene 1: Three dots
        dot = Dot(radius=0.16, color=RED)
        dots = VGroup(*[dot.copy() for _ in range(3)]).arrange(RIGHT, buff=0.5)
        dots.to_edge(LEFT, buff=2)
        self.play(FadeIn(dots))

        with self.voiceover(text="We have 3 dots.") as tracker:
            self.wait(tracker.duration)

        # Scene 2: Five more dots
        more_dots = VGroup(*[dot.copy() for _ in range(5)]).arrange(RIGHT, buff=0.5)
        more_dots.next_to(dots, RIGHT, buff=1)
        self.play(FadeIn(more_dots))

        with self.voiceover(text="And then we get 5 more dots.") as tracker:
            self.wait(tracker.duration)

        # Scene 3: Combine the dots
        all_dots = VGroup(*[dot.copy() for _ in range(8)]).arrange(RIGHT, buff=0.5)
        all_dots.move_to(dots.get_center())
        self.play(ReplacementTransform(dots, all_dots[:3]))
        self.play(ReplacementTransform(more_dots, all_dots[3:]))

        # Equation
        equation = MathTex("3", "+", "5", "=", "8").scale(2)
        equation.next_to(all_dots, DOWN)

        with self.voiceover(text="So if we add them together, how many dots do we have?") as tracker:
            self.wait(tracker.duration)

        self.play(Write(equation))

        with self.voiceover(text="That's right! We have 8 dots in total!") as tracker:
            self.wait(tracker.duration)

        # Outro
        outro = Text("Thanks for learning with us!", font_size=40).set_color(BLUE)
        self.play(FadeOut(all_dots), FadeOut(equation))
        self.play(Write(outro))
        self.wait(2)
        self.play(FadeOut(outro))
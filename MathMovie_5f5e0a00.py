from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import random  # Import the random module

class AdditionExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual"
            )
        )

        # Title
        title = Text("Addition is Fun!", font_size=60, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        with self.voiceover(text="Hello everyone!  Today we're going to explore the exciting world of addition.") as tracker:
            self.play(FadeOut(title), run_time=tracker.duration)

        # Equation
        equation = MathTex("2 + 3 = ?").scale(1.5).move_to(UP * 2)
        self.play(Write(equation))
        self.wait(0.5)
        with self.voiceover(text="Let's start with a simple problem:  2 + 3 = ?") as tracker:
            self.play(FadeToColor(equation, color=YELLOW), run_time=tracker.duration) 

        # Apples
        apple1 = Circle(radius=0.5, color=RED, fill_opacity=1).shift(LEFT * 2)
        apple2 = Circle(radius=0.5, color=RED, fill_opacity=1).shift(LEFT)
        apple3 = Circle(radius=0.5, color=RED, fill_opacity=1)
        apple4 = Circle(radius=0.5, color=RED, fill_opacity=1).shift(RIGHT)
        apple5 = Circle(radius=0.5, color=RED, fill_opacity=1).shift(RIGHT * 2)

        with self.voiceover(text="Imagine you have two delicious apples.") as tracker:
            self.play(FadeIn(apple1), FadeIn(apple2), run_time=tracker.duration)
            self.play(Wiggle(apple1), Wiggle(apple2), run_time=0.5)

        with self.voiceover(text="Now, your friend gives you three more!") as tracker:
            self.play(FadeIn(apple3), FadeIn(apple4), FadeIn(apple5), run_time=tracker.duration)
            self.play(Wiggle(apple3), Wiggle(apple4), Wiggle(apple5), run_time=0.5)

        # Encompassing Circle
        circle = Circle(radius=2.5, color=YELLOW, stroke_width=2).move_to(DOWN * 0.5)
        with self.voiceover(text="How many apples do you have in total?") as tracker:
            self.play(Create(circle), run_time=tracker.duration)

        # Solution
        solution = MathTex("5").scale(1.5).move_to(equation.get_center() + RIGHT * 2.2)
        with self.voiceover(text="You got it! You have 5 apples. 2 + 3 = 5") as tracker:
            self.play(ReplacementTransform(equation[-1], solution), run_time=tracker.duration)
            self.play(Flash(VGroup(apple1, apple2, apple3, apple4, apple5)))

        # Explanation
        with self.voiceover(text="That's addition! Combining things together to get a bigger number. We can use addition for all sorts of things, like counting toys, adding up scores in a game, or even figuring out how much money you have.") as tracker:
            self.play(FadeOut(circle), FadeOut(apple1), FadeOut(apple2), FadeOut(apple3), FadeOut(apple4), FadeOut(apple5), run_time=tracker.duration)

            # Example Scenes - Replace with Manim creations later
            toys = VGroup(*[Dot(radius=0.1, color=random_bright_color()).shift(random.uniform(-2, 2) * RIGHT + random.uniform(-1, 1) * UP) for _ in range(10)])
            scoreboard = VGroup(Rectangle(width=2, height=1), Text("Home: 10", font_size=20), Text("Away: 8", font_size=20).shift(DOWN * 0.5)).arrange(DOWN)
            piggy_bank = Text("Piggy Bank", font_size=30) 
            coins = VGroup(*[Circle(radius=0.1, color=GOLD).shift(random.uniform(-1, 1) * RIGHT + random.uniform(-0.5, 0.5) * UP) for _ in range(5)])

            self.play(FadeIn(toys))
            self.wait(0.5)
            self.play(ReplacementTransform(toys, scoreboard))
            self.wait(0.5)
            self.play(ReplacementTransform(scoreboard, piggy_bank), FadeIn(coins))
            self.wait(0.5)
            self.play(FadeOut(piggy_bank), FadeOut(coins))

        # Closing
        with self.voiceover(text="So next time you need to add things up, remember the apples!") as tracker:
            self.play(FadeIn(apple1), FadeIn(apple2), FadeIn(apple3), FadeIn(apple4), FadeIn(apple5), run_time=tracker.duration)
            self.play(Wiggle(apple1), Wiggle(apple2), Wiggle(apple3), Wiggle(apple4), Wiggle(apple5), run_time=0.5)

        # Outro
        outro = Text("The End", font_size=60, color=ORANGE)
        with self.voiceover(text="Thanks for watching!") as tracker:
            self.play(FadeOut(apple1), FadeOut(apple2), FadeOut(apple3), FadeOut(apple4), FadeOut(apple5), run_time=tracker.duration)
            self.play(Write(outro))
            self.wait(1)
            self.play(FadeOut(outro))
            self.wait()
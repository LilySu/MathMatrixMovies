from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

BROWN = "#A52A2A"  # Define the BROWN color

class AddingSixAndNine(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )

        # Title
        title = Text("Adding 6 and 9").scale(1.5).set_color(BLUE)
        self.play(Write(title))
        with self.voiceover(text="Hello everyone! Today, we're going to learn how to add 6 and 9.") as tracker:
            self.wait(tracker.duration)
        self.play(FadeOut(title))

        # Apples
        apples = VGroup(*[Circle(radius=0.3, color=RED, fill_opacity=1) for _ in range(6)]).arrange(RIGHT, buff=0.5).to_edge(LEFT)
        self.play(Create(apples))
        with self.voiceover(text="Let's start with 6 juicy red apples.") as tracker:
            self.wait(tracker.duration)

        # Bananas
        bananas = VGroup(*[Ellipse(width=0.5, height=0.8, color=YELLOW, fill_opacity=1) for _ in range(9)]).arrange(RIGHT, buff=0.3).to_edge(RIGHT)
        self.play(Create(bananas))
        with self.voiceover(text="Now, we have 9 yummy yellow bananas.") as tracker:
            self.wait(tracker.duration)

        # Plus sign and "and"
        plus = Text("+").scale(2).move_to(ORIGIN)
        and_text = Text("and").scale(1.5).move_to(ORIGIN)
        self.play(Write(plus))
        with self.voiceover(text="We want to add the apples and bananas together.") as tracker:
            self.wait(tracker.duration)
        self.play(Transform(plus, and_text))
        with self.voiceover(text="Adding means putting them all together in a basket.") as tracker:
            self.wait(tracker.duration)

        # Basket
        basket = VGroup(
            Rectangle(width=4, height=1.5, color=BROWN, fill_opacity=1), 
            Line(start=[-1, 0.75, 0], end=[1, 2, 0], color=BROWN, stroke_width=8),
            Line(start=[1, 0.75, 0], end=[-1, 2, 0], color=BROWN, stroke_width=8)
        ).to_edge(DOWN)
        self.play(Create(basket))

        # Moving fruits to basket
        fruits = VGroup(*apples, *bananas)
        count = 0
        for fruit in fruits:
            self.play(fruit.animate.move_to(basket.get_center() + np.random.uniform(-0.5, 0.5, 3))) # 3D offset
            count += 1
            with self.voiceover(text=str(count)) as tracker:
                self.wait(tracker.duration)

        # Equation
        equation = MathTex("6 + 9 = 15").next_to(basket, DOWN)
        self.play(Write(equation))
        with self.voiceover(text="Look! We have 15 fruits in total! So, 6 + 9 equals 15!") as tracker:
            self.play(Wiggle(fruits), run_time=tracker.duration)

        with self.voiceover(text="You did a great job adding! Now you know that 6 plus 9 equals 15!") as tracker:
            self.wait(tracker.duration)

        # Outro
        outro = Text("Thanks for learning with us today! See you next time!").scale(1.2).set_color(GREEN).move_to(ORIGIN)
        self.play(FadeIn(outro))
        with self.voiceover(text="Thanks for learning with us today! See you next time!") as tracker:
            self.wait(tracker.duration)
        self.play(FadeOut(outro))

        self.wait()
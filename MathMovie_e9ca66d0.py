from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class ProbabilityPuzzle(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual"
            )
        )

        # Title card
        title = Text("The Probability Puzzle: Fertility Edition", font_size=48).move_to(UP*2)
        with self.voiceover(text="The Probability Puzzle: Fertility Edition"):
            self.play(FadeIn(title))
            self.wait(2)
        self.play(FadeOut(title))

        # Coin flipping
        coin = Circle(radius=0.5, color=YELLOW).set_fill(YELLOW, opacity=1)
        heads_text = Text("H", font_size=24).move_to(coin.get_center())
        tails_text = Text("T", font_size=24).move_to(coin.get_center())

        self.play(FadeIn(coin))

        with self.voiceover(text="Imagine flipping a coin with a 20% chance of landing on heads. We're going to flip it six times.") as tracker:
            for _ in range(6):
                self.play(Rotate(coin, angle=PI/2, about_point=ORIGIN), run_time=0.5)
                self.add(tails_text)
                self.remove(heads_text)
                self.wait(0.2)
            self.wait(tracker.duration - 3)

        self.play(FadeOut(coin), FadeOut(tails_text))

        # 20% and 80% probability
        prob20 = Text("20% Probability", font_size=36).move_to(UP*2 + LEFT*3)
        prob80 = Text("80% Probability", font_size=36).move_to(UP*2 + RIGHT*3)

        with self.voiceover(text="Let's break down this 20% probability.  This means, for each individual attempt, there's a 20% chance of success and an 80% chance of failure.") as tracker:
            self.play(FadeIn(prob20))
            self.wait(tracker.duration / 2)
            self.play(FadeIn(prob80))
            self.wait(tracker.duration / 2)

        # Formula for failing all six times
        formula = MathTex("0.8 \\times 0.8 \\times 0.8 \\times 0.8 \\times 0.8 \\times 0.8 = 0.262", font_size=36).next_to(prob80, DOWN)

        with self.voiceover(text="We need to consider the probability of failing every single time. To do this, we multiply the probability of failing on each attempt together.") as tracker:
            self.play(FadeIn(formula))
            self.wait(tracker.duration)

        self.play(FadeOut(prob20), FadeOut(prob80), FadeOut(formula))

        # Probability of at least one success
        success_text = Text("Probability of at least ONE Success", font_size=36).move_to(UP*2)
        success_formula = MathTex("1 - 0.262 = 0.738", font_size=36).next_to(success_text, DOWN)

        with self.voiceover(text="To find the probability of at least one success, we simply subtract the probability of failing every time from 1, or 100%.") as tracker:
            self.play(FadeIn(success_text))
            self.wait(tracker.duration / 2)
            self.play(FadeIn(success_formula))
            self.wait(tracker.duration / 2)

        self.play(FadeOut(success_text), FadeOut(success_formula))

        # Conclusion
        conclusion1 = Text("So, Dr. Huberman, while your enthusiasm is appreciated,", font_size=30).move_to(UP*1)
        conclusion2 = Text("the math doesn't quite add up. Probability can be tricky!", font_size=30).next_to(conclusion1, DOWN)
        self.play(FadeIn(conclusion1), FadeIn(conclusion2))

        with self.voiceover(text="So, Dr. Huberman, while your enthusiasm is appreciated, the math doesn't quite add up. Probability can be tricky!") as tracker:
            self.wait(tracker.duration)

        self.play(FadeOut(conclusion1), FadeOut(conclusion2))

        # Reminder: Probability doesn't stack!
        reminder = Text("Remember: Probability doesn't stack!", font_size=36, color=RED).move_to(UP*2)
        with self.voiceover(text="Remember: Probability doesn't stack!") as tracker:
            self.play(FadeIn(reminder))
            self.wait(tracker.duration)
        self.play(FadeOut(reminder))

        # Outro card
        outro = Text("The Probability Puzzle: Fertility Edition", font_size=48).move_to(UP*2)
        with self.voiceover(text="The Probability Puzzle: Fertility Edition"):
            self.play(FadeIn(outro))
            self.wait(2)
        self.play(FadeOut(outro))

        self.wait()
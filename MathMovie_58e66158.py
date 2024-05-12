from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class ProbabilityExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )

        # Title
        title = Text("The Odds Are In Your Favor (Maybe?)", font_size=40)
        self.play(Write(title))
        self.wait(1)
        with self.voiceover(text="Hi everyone! Today, we're diving into the world of probability. We're going to figure out what happens when you do something with a 20% chance of success, six times in a row.") as tracker:
            self.play(FadeOut(title), run_time=tracker.duration)

        # Coin Visualization
        coin = Circle(radius=1, fill_opacity=1, color=GOLD)
        text_H = Text("H", font_size=30).move_to(coin)
        text_T = Text("T", font_size=30).move_to(coin)
        coin_group = VGroup(coin, text_H).shift(2*LEFT)
        self.play(FadeIn(coin_group))

        with self.voiceover(text="Imagine you have a coin that's a bit weird. Instead of having a 50/50 chance of landing on heads or tails, it only lands on heads 20% of the time. That's like 1 out of every 5 flips!") as tracker:
            self.play(Rotate(coin_group, PI, axis=RIGHT), run_time=0.5)
            self.play(FadeOut(text_H), FadeIn(text_T), run_time=0.1)
            self.wait(0.4)

            for i in range(4):
                self.play(Rotate(coin_group, PI, axis=RIGHT), run_time=0.5)
                self.play(FadeOut(text_T), FadeIn(text_H), run_time=0.1) if i % 2 == 0 else self.play(FadeOut(text_H), FadeIn(text_T), run_time=0.1)
                self.wait(0.4)

        # Question
        question = Text("What are the odds of getting at least one head in 6 flips?", font_size=30)
        self.play(FadeOut(coin_group), Write(question))
        self.wait(2)

        # Calculations (staggered appearance for emphasis)
        eq1 = MathTex(r"P(Tails) = 1 - 0.2 = 0.8").shift(UP)
        with self.voiceover(text="Instead of directly calculating the probability of getting at least one head, it's easier to figure out the probability of getting NO heads at all and subtract that from 1.") as tracker:
            self.play(FadeOut(question), run_time=tracker.duration)
        self.wait(1)
        with self.voiceover(text="The probability of getting tails on one flip is 80%, which is the same as 0.8.") as tracker:
            self.play(Write(eq1), run_time=tracker.duration)
            self.wait(1)

        eq2 = MathTex(r"P(6 \, Tails) = 0.8 \times 0.8 \times 0.8 \times 0.8 \times 0.8 \times 0.8").shift(DOWN)
        with self.voiceover(text="To get the probability of getting tails on six flips in a row, we multiply 0.8 by itself six times.") as tracker:
            self.play(Write(eq2), run_time=tracker.duration)
            self.wait(2)

        eq3 = MathTex(r"P(6 \, Tails) \approx 0.262").shift(2*DOWN)
        with self.voiceover(text="This gives us approximately 0.262.") as tracker:
            self.play(Write(eq3), run_time=tracker.duration)
            self.wait(2)

        eq4 = MathTex(r"P(At \, Least \, One \, Head) = 1 - 0.262 = 0.738").shift(3*DOWN)
        with self.voiceover(text="Finally, the probability of getting at least one head is 1 minus 0.262, which equals 0.738.") as tracker:
            self.play(Write(eq4), run_time=tracker.duration)
            self.wait(3)

        # Result Visualization
        result = Text("73.8% chance!", font_size=40, color=GREEN).shift(UP)
        surprised_face = Text(":O", font_size=60).next_to(result, DOWN)
        self.play(FadeOut(eq1), FadeOut(eq2), FadeOut(eq3), FadeOut(eq4), 
                  FadeIn(result), FadeIn(surprised_face))
        self.wait(3)

        # Outro
        outro = Text("That's it for today! Remember, even if something seems unlikely, doing it multiple times can really change the odds. See you next time!", font_size=25)
        self.play(FadeOut(result), FadeOut(surprised_face), Write(outro))
        with self.voiceover(text="That's it for today! Remember, even if something seems unlikely, doing it multiple times can really change the odds. See you next time!") as tracker:
            self.play(FadeOut(outro), run_time=tracker.duration)
        self.wait(1)
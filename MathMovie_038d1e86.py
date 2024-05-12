from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class FertilityFallacy(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )
        
        # Title
        title = Text("The Fertility Fallacy: Why 20% Doesn't Mean 120% (👶)").scale(0.8)
        self.play(Write(title))
        self.wait(1)
        with self.voiceover(text="The Fertility Fallacy: Why 20% Doesn't Mean 120%  Let's debunk a common misconception about probability, especially in the context of fertility.") as tracker:
            self.play(FadeOut(title), run_time=tracker.duration)

        # Scene 1: The Misconception
        eq = MathTex("20\\% \\times 6 = 120\\%").scale(1.2)
        with self.voiceover(text="Imagine a couple trying to conceive. Let's say there's a 20% chance of success each month. Some might think that trying for 6 months guarantees a 120% chance of pregnancy!") as tracker:
            self.play(FadeIn(eq), run_time=tracker.duration)
        self.wait(1)
        with self.voiceover(text="This, my friends, is where the fallacy lies. Probability doesn't work by simple addition.") as tracker:
            self.play(FadeOut(eq), run_time=tracker.duration)

        # Scene 2: Flipping a Coin
        coin = Circle(radius=0.5, fill_color=GREY, stroke_color=WHITE, stroke_width=4).shift(UP*2)
        coin_text = Text("H").move_to(coin.get_center())
        self.play(FadeIn(coin), FadeIn(coin_text))
        with self.voiceover(text="Think of it like flipping a coin. You have a 50% chance of getting heads.") as tracker:
            self.play(Rotate(coin, angle=PI, axis=RIGHT), FadeTransform(coin_text, Text("T").move_to(coin.get_center())), run_time=tracker.duration)
            self.play(Rotate(coin, angle=PI, axis=RIGHT), FadeTransform(coin_text, Text("T").move_to(coin.get_center())), run_time=tracker.duration)
        self.play(FadeOut(coin), FadeOut(coin_text))

        with self.voiceover(text="Flipping it twice doesn't guarantee you'll get heads at least once. You could get tails both times!") as tracker:
            self.wait(tracker.duration)

        # Scene 3: Understanding Probability 
        circles = VGroup(*[Circle(radius=0.7, fill_color=BLUE_D, stroke_color=WHITE, stroke_width=2) for _ in range(6)]).arrange(RIGHT, buff=1)
        nums = VGroup(*[Text(f"{i+1}").move_to(circles[i].get_center()) for i in range(6)])
        probs = VGroup(*[Text("20%").move_to(circles[i].get_center()).scale(0.8) for i in range(6)])
        self.play(FadeIn(circles), FadeIn(nums))
        with self.voiceover(text="With fertility, the 20% chance each month is independent. Each month is a fresh start, unaffected by the previous months.") as tracker:
            self.play(FadeIn(probs), run_time=tracker.duration)
        self.wait(1)
        with self.voiceover(text="To find the probability of getting pregnant at least ONCE in those 6 months, we need to look at the probability of NOT getting pregnant each month.") as tracker:
            self.play(Transform(probs, VGroup(*[Text("80%").move_to(circles[i].get_center()).scale(0.8) for i in range(6)])), run_time=tracker.duration)
        self.wait(1)
        eq2 = MathTex("0.8 \\times 0.8 \\times 0.8 \\times 0.8 \\times 0.8 \\times 0.8 = 0.26").scale(0.8).shift(DOWN*2)
        with self.voiceover(text="That's 80%, or 0.8. We multiply 0.8 by itself six times, representing the six months.") as tracker:
            self.play(FadeIn(eq2), run_time=tracker.duration)
        self.wait(1)
        with self.voiceover(text="This gives us about 0.26, or 26%. This is the probability of NOT getting pregnant in 6 months.") as tracker:
            self.wait(tracker.duration)

        # Scene 4: The Real Probability
        eq3 = MathTex("1 - 0.26 = 0.74").scale(0.8).shift(DOWN*2.5)
        with self.voiceover(text="To find the probability of getting pregnant AT LEAST ONCE, we subtract this from 1 (or 100%).") as tracker:
            self.play(Transform(eq2, eq3), run_time=tracker.duration)
        self.wait(1)
        with self.voiceover(text="The answer?  There's approximately a 74% chance of getting pregnant at least once within those six months, NOT 120%.") as tracker:
            self.wait(tracker.duration)

        # Scene 5: Outro 
        self.play(FadeOut(circles), FadeOut(nums), FadeOut(probs), FadeOut(eq2))
        outro_text = Text("So, Dr. Huberman, while we appreciate your enthusiasm,\nprobability is a bit more nuanced than simple addition.\nRemember, in probability, 1 plus 1 doesn't always equal 2,\nespecially when babies are involved!").scale(0.6)
        with self.voiceover(text="So, Dr. Huberman, while we appreciate your enthusiasm, probability is a bit more nuanced than simple addition. Remember, in probability, 1 plus 1 doesn't always equal 2, especially when babies are involved!") as tracker:
            self.play(FadeIn(outro_text), run_time=tracker.duration)
        self.wait(2)
        self.play(FadeOut(outro_text))
        
        # Outro Title Card
        outro_title = Text("The Fertility Fallacy: Debunked! 👶").scale(0.8)
        with self.voiceover(text="The Fertility Fallacy: Debunked!") as tracker:
            self.play(Write(outro_title), run_time=tracker.duration)
        self.wait(2)
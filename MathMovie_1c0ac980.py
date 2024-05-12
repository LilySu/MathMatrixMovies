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

        BROWN = manim.color.rgb_to_hex((139/255, 69/255, 19/255)) # Defining BROWN color

        # Title Card
        title_background = Rectangle(width=config.frame_width, height=config.frame_height, 
                                     fill_color=BLUE, fill_opacity=1)
        title = Text("Let's Learn Addition!", font="Comic Sans MS").scale(1.5)
        with self.voiceover(text="Let's learn addition!") as tracker:
            self.play(FadeIn(title_background), Create(title, run_time=tracker.duration))
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(title_background))

        # Apples
        red_apples = VGroup()
        for i in range(3):
            apple = VGroup(
                Circle(color=RED, fill_opacity=1).scale(0.3),
                Line(start=UP * 0.15, end=UP * 0.3, stroke_width=2, color=BROWN).shift(DOWN * 0.15),
                Ellipse(width=0.1, height=0.2, color=GREEN, fill_opacity=1).rotate(PI/4).shift(UP * 0.2 + RIGHT * 0.1)
            )
            red_apples.add(apple)
        red_apples.arrange(RIGHT, buff=0.5).shift(3*LEFT)

        green_apples = VGroup()
        for i in range(5):
            apple = VGroup(
                Circle(color=GREEN, fill_opacity=1).scale(0.3),
                Line(start=UP * 0.15, end=UP * 0.3, stroke_width=2, color=BROWN).shift(DOWN * 0.15),
                Ellipse(width=0.1, height=0.2, color=GREEN, fill_opacity=1).rotate(PI/4).shift(UP * 0.2 + RIGHT * 0.1)
            )
            green_apples.add(apple)
        green_apples.arrange(RIGHT, buff=0.5).shift(3*RIGHT)

        with self.voiceover(text="Imagine you have three juicy red apples.") as tracker:
            self.play(AnimationGroup(*[Create(apple) for apple in red_apples], lag_ratio=0.2), 
                      run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="And then your friend gives you five yummy green apples.") as tracker:
            self.play(AnimationGroup(*[Create(apple) for apple in green_apples], lag_ratio=0.2), 
                      run_time=tracker.duration)
        self.wait(0.5)

        # Combining Apples
        with self.voiceover(text="Now, let's count all the apples together."
                               "One, two, three, four, five, six, seven, eight!") as tracker:
            self.play(
                red_apples.animate.shift(3 * RIGHT),
                green_apples.animate.shift(3 * LEFT),
                run_time=tracker.duration
            )
            all_apples = VGroup(red_apples, green_apples).arrange(RIGHT, buff=0.5)
            for i in range(len(all_apples)):
                self.play(all_apples[i].animate.set_fill(YELLOW), run_time=0.2)
                self.play(all_apples[i].animate.set_fill(RED if i < 3 else GREEN), run_time=0.2)

        self.wait(0.5)

        # Plus Sign
        plus_sign = Text("+").scale(2)
        with self.voiceover(text="When we add things together, we use this sign,"
                               " a plus sign.") as tracker:
            self.play(FadeIn(plus_sign), run_time=tracker.duration)
        self.wait(0.5)

        # Numbers and Formula
        three_text = Text("3", color=RED).scale(1.5).next_to(red_apples, UP)
        five_text = Text("5", color=GREEN).scale(1.5).next_to(green_apples, UP)
        equals_sign = Text("=", color=BLUE).scale(1.5).next_to(all_apples, RIGHT)
        eight_text = Text("8", color=YELLOW).scale(1.5).next_to(equals_sign, RIGHT)
        formula = Tex("3 + 5 = 8").scale(2).next_to(all_apples, DOWN)

        with self.voiceover(text="So, three apples plus five apples equals eight apples!") as tracker:
            self.play(FadeIn(three_text), FadeIn(five_text), FadeIn(equals_sign), FadeIn(eight_text), run_time=tracker.duration)
        self.wait(0.5)

        self.play(Write(formula))
        self.wait(0.5)

        for i, part in enumerate(formula):
            color = [RED, WHITE, GREEN, BLUE, YELLOW][i]
            self.play(part.animate.set_color(color), run_time=0.2)
            self.wait(0.2)
            self.play(part.animate.set_color(WHITE), run_time=0.2)
        self.wait(0.5)

        with self.voiceover(text="That's addition! You learned it!") as tracker:
            self.play(FadeOut(all_apples), FadeOut(three_text), FadeOut(five_text),
                    FadeOut(equals_sign), FadeOut(eight_text), FadeOut(plus_sign), FadeOut(formula),
                    run_time=tracker.duration)
        self.wait(0.5)

        # Outro
        outro_background = Rectangle(width=config.frame_width, height=config.frame_height,
                                      fill_color=BLUE, fill_opacity=1)
        outro = Text("The End", font="Comic Sans MS").scale(1.5)
        with self.voiceover(text="The End") as tracker:
            self.play(FadeIn(outro_background), Create(outro, run_time=tracker.duration))
        self.wait(0.5)
        self.play(FadeOut(outro), FadeOut(outro_background))
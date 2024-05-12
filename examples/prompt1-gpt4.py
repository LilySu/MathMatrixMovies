from manim import *


class AddNumbers(Scene):
    def construct(self):
        # Introduction
        text = Text("Let's add 5 and 3!")
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))

        # Show 5 balloons
        balloons_5 = VGroup(*[Circle(fill_color=color, fill_opacity=0.8).scale(0.5)
                            for color in [BLUE, YELLOW, GREEN, RED, PURPLE]])
        balloons_5.arrange(RIGHT, buff=0.2)
        self.play(LaggedStart(*(DrawBorderThenFill(balloon)
                  for balloon in balloons_5)))
        self.wait(1)

        # Adding 3 more balloons
        balloons_3 = VGroup(*[Circle(fill_color=color, fill_opacity=0.8).scale(0.5)
                            for color in [ORANGE, PINK, TEAL]])
        balloons_3.arrange(RIGHT, buff=0.2).next_to(balloons_5, RIGHT, buff=1)
        self.play(LaggedStart(*(DrawBorderThenFill(balloon)
                  for balloon in balloons_3)))
        self.wait(1)

        # Combine and count all balloons
        all_balloons = VGroup(*balloons_5, *balloons_3)
        all_balloons.arrange(RIGHT, buff=0.2).move_to(ORIGIN)
        self.play(ReplacementTransform(
            VGroup(*balloons_5.copy(), *balloons_3.copy()), all_balloons))
        self.wait(1)

        # Show result
        result_text = Text("5 + 3 = 8 Balloons!").scale(1.2)
        result_text.next_to(all_balloons, DOWN, buff=0.5)
        self.play(Write(result_text))
        self.wait(2)

        # Conclusion
        self.play(FadeOut(VGroup(all_balloons, result_text)))

        # Goodbye message
        goodbye_text = Text("Great counting! See you next time!").scale(0.8)
        self.play(FadeIn(goodbye_text), run_time=2)
        self.wait(2)
        self.play(FadeOut(goodbye_text))

# To run this scene, use:
# manim -pql your_script_name.py AddNumbers

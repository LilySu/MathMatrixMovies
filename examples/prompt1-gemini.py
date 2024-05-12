from manim import *


class CountingApples(Scene):
    def construct(self):
        # Create bunny using Manim shapes
        bunny_body = Ellipse(
            width=1, height=2, color=WHITE).set_fill(WHITE, opacity=1)
        bunny_head = Circle(radius=0.5, color=WHITE).set_fill(
            WHITE, opacity=1).next_to(bunny_body, UP)
        left_ear = Ellipse(width=0.4, height=1, color=WHITE).set_fill(WHITE, opacity=1).rotate(
            45*DEGREES).next_to(bunny_head, UP, buff=0.1).shift(LEFT*0.3)
        right_ear = Ellipse(width=0.4, height=1, color=WHITE).set_fill(
            WHITE, opacity=1).rotate(-45*DEGREES).next_to(bunny_head, UP, buff=0.1).shift(RIGHT*0.3)

        bunny = VGroup(bunny_body, bunny_head, left_ear,
                       right_ear).scale(0.5).to_edge(LEFT)

        self.play(FadeIn(bunny))

        # Create apples
        red_apples = VGroup(
            *[Circle(radius=0.3, color=RED).set_fill(RED, opacity=0.8) for _ in range(5)])
        red_apples.arrange(RIGHT, buff=0.5)
        red_apples.next_to(bunny, RIGHT)

        # Counting the first five apples
        self.play(LaggedStart(*[FadeIn(apple)
                  for apple in red_apples], lag_ratio=0.2))
        self.wait(0.5)

        number_text = Text("5", font_size=40).next_to(red_apples, UP)
        self.play(Write(number_text))
        self.wait(0.5)

        # Add three more apples
        green_apples = VGroup(
            *[Circle(radius=0.3, color=GREEN).set_fill(GREEN, opacity=0.8) for _ in range(3)])
        green_apples.arrange(RIGHT, buff=0.5)
        green_apples.next_to(red_apples, RIGHT)

        self.play(LaggedStart(*[FadeIn(apple)
                  for apple in green_apples], lag_ratio=0.2))
        self.wait(0.5)

        number_text_3 = Text("3", font_size=40).next_to(green_apples, UP)
        self.play(Write(number_text_3))
        self.wait(0.5)

        # Count all the apples
        # Correctly combine the apples
        all_apples = VGroup(*red_apples, *green_apples)
        self.play(FadeOut(number_text), FadeOut(number_text_3))

        for i in range(8):  # Iterate through all 8 apples
            self.play(Indicate(all_apples[i], color=YELLOW), run_time=0.5)
            count_text = Text(str(i+1), font_size=40).next_to(all_apples, DOWN)
            self.play(FadeIn(count_text), run_time=0.5)
            self.play(FadeOut(count_text), run_time=0.5)

        # Show equation
        equation = MathTex("5 + 3 = 8", font_size=60).next_to(all_apples, DOWN)
        self.play(Write(equation))
        self.wait(2)

        # Bunny eats an apple
        self.play(FadeOut(equation), FadeOut(all_apples[0]))
        self.play(bunny.animate.shift(RIGHT*0.5))
        self.wait(1)

        # The end
        self.play(FadeOut(bunny), FadeOut(all_apples))
        the_end = Text("The End!", font_size=60, color=YELLOW).move_to(ORIGIN)
        self.play(Write(the_end))
        self.wait(2)

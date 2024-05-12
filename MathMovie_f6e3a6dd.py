from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class QuadraticEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )
        
        # Introduction
        with self.voiceover(text="Imagine you're throwing a ball straight up in the air.") as tracker:
            ball = Dot(color=RED).shift(2*DOWN)
            path = TracedPath(ball.get_center, stroke_width=2, stroke_color=YELLOW)
            self.play(Create(ball), run_time=tracker.duration)

        with self.voiceover(text="It goes up, slows down, stops for a moment, and then falls back down.") as tracker:
            self.play(ball.animate.shift(5*UP), run_time=tracker.duration/2)
            self.play(ball.animate.shift(5*DOWN), run_time=tracker.duration/2)

        with self.voiceover(text="The path the ball takes makes a curve, kind of like a smile.") as tracker:
            self.add(path)

        with self.voiceover(text="This curve is called a parabola, and it's described by a type of equation called a quadratic equation.") as tracker:
            parabola = ParametricFunction(
                lambda t: np.array([t, -t**2 + 4, 0]),
                t_range = [-2, 2],
                color=BLUE
            ).shift(DOWN)
            self.play(Create(parabola), run_time=tracker.duration)

        # Explaining the equation
        with self.voiceover(text="A basic quadratic equation looks like this: y equals ax squared plus bx plus c.") as tracker:
            equation = MathTex("y = ax^2 + bx + c").shift(3*RIGHT+UP)
            self.play(Write(equation), run_time=tracker.duration)

        with self.voiceover(text="The letters a, b, and c are like knobs we can turn to change the shape and position of our parabola.") as tracker:
            a_label = Tex("a").next_to(equation[0][3:6], DOWN)
            b_label = Tex("b").next_to(equation[0][7:9], DOWN)
            c_label = Tex("c").next_to(equation[0][10:], DOWN)
            self.play(Write(a_label), Write(b_label), Write(c_label), run_time=tracker.duration)

        # Showing the effect of 'a'
        with self.voiceover(text="For example, changing 'a' makes the parabola wider or narrower.") as tracker:
            self.play(FadeOut(ball), FadeOut(path), run_time=tracker.duration/2)
            for i in range(3):
                new_parabola = ParametricFunction(
                    lambda t: np.array([t, -(i+1)*t**2 + 4, 0]),
                    t_range = [-2, 2],
                    color=BLUE
                ).shift(DOWN)
                self.play(Transform(parabola, new_parabola), run_time=tracker.duration/6)
            self.play(FadeIn(ball), FadeIn(path), run_time=tracker.duration/2)

        # Showing the effect of 'c'
        with self.voiceover(text="Changing 'c' moves the whole parabola up or down.") as tracker:
            for i in range(3):
                new_parabola = ParametricFunction(
                    lambda t: np.array([t, -t**2 + 4 + i, 0]),
                    t_range = [-2, 2],
                    color=BLUE
                ).shift(DOWN)
                self.play(Transform(parabola, new_parabola), run_time=tracker.duration/6)

        # Conclusion
        with self.voiceover(text="So, quadratic equations are a powerful tool for describing curves and arcs, like the path of a ball or the shape of a bridge.") as tracker:
            bridge = ArcBetweenPoints(start=4*LEFT+DOWN, end=4*RIGHT+DOWN, angle=-PI/2, color=GREY)
            self.play(Create(bridge), run_time=tracker.duration)

        with self.voiceover(text="They pop up all over in math and science, so understanding them opens up a whole world of possibilities.") as tracker:
            self.play(FadeOut(parabola), FadeOut(bridge), FadeOut(equation),
                      FadeOut(a_label), FadeOut(b_label), FadeOut(c_label), run_time=tracker.duration)

        self.wait()
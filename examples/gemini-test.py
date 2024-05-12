from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class IntegralCalculusExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )
        # Introduction
        with self.voiceover(text="Let's dive into integral calculus!") as tracker:
            intro_text = Text("Integral Calculus").scale(1.5)
            self.play(Write(intro_text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(intro_text))

        # Area under the curve
        with self.voiceover(text="Imagine we have a curve, like this.") as tracker:
            axes = Axes(
                x_range=[0, 5, 1],
                y_range=[0, 8, 2],
                x_length=5,
                y_length=4,
                axis_config={"include_numbers": True},
            )
            graph = axes.plot(lambda x: x**2, color=BLUE)
            self.play(Create(axes), run_time=tracker.duration/2)
            self.play(Create(graph), run_time=tracker.duration/2)
        self.wait(0.5)

        with self.voiceover(text="Integral calculus helps us find the area under this curve.") as tracker:
            area = axes.get_area(graph, x_range=[1, 4], color=[BLUE_D, BLUE_E])
            self.play(FadeIn(area), run_time=tracker.duration)
        self.wait(0.5)

        # Rectangles and approximation
        with self.voiceover(text="We can approximate this area by using rectangles.") as tracker:
            rects = axes.get_riemann_rectangles(
                graph,
                x_range=[1, 4],
                dx=0.5,
                input_sample_type="right",
            )
            self.play(Create(rects), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="The thinner the rectangles, the more accurate our approximation.") as tracker:
            for dx in [0.25, 0.1, 0.05]:
                new_rects = axes.get_riemann_rectangles(
                    graph,
                    x_range=[1, 4],
                    dx=dx,
                    input_sample_type="right",
                )
                self.play(Transform(rects, new_rects),
                          run_time=tracker.duration / 3)
        self.wait(0.5)

        # The integral symbol
        with self.voiceover(text="We represent this process of finding the exact area with the integral symbol.") as tracker:
            integral_symbol = Tex(r"$\int$")
            self.play(FadeOut(rects), run_time=tracker.duration/2)
            self.play(Write(integral_symbol), run_time=tracker.duration/2)
        self.wait(0.5)

        # Function and limits of integration
        with self.voiceover(text="We integrate a function, in this case, x squared.") as tracker:
            function_text = Tex(r"$x^2$").next_to(integral_symbol, RIGHT)
            self.play(Write(function_text), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="And we specify the limits of integration, from 1 to 4.") as tracker:
            limits = Tex("1", r"$\,$", "4").scale(0.7)
            limits[0].next_to(integral_symbol, DOWN, buff=0.1)
            limits[2].next_to(integral_symbol, UP, buff=0.1)
            self.play(Write(limits), run_time=tracker.duration)
        self.wait(0.5)

        # Conclusion
        with self.voiceover(text="This integral gives us the precise area under the curve between these limits.") as tracker:
            self.play(FadeOut(axes), FadeOut(graph), FadeOut(
                area), run_time=tracker.duration/2)
            self.play(
                integral_symbol.animate.scale(2).move_to(ORIGIN),
                function_text.animate.scale(2).next_to(integral_symbol, RIGHT),
                limits.animate.scale(2).next_to(integral_symbol, DOWN),
                run_time=tracker.duration/2
            )
        self.wait(1)

        with self.voiceover(text="That's a glimpse into the power of integral calculus!") as tracker:
            self.play(FadeOut(integral_symbol), FadeOut(function_text),
                      FadeOut(limits), run_time=tracker.duration)
        self.wait(1)

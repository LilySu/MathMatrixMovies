from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class QuadraticExpressions(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

        # Force generation of all voiceovers at the beginning 
        self.generate_voiceovers(
            "Hey there! Today, we're diving into the world of quadratic expressions.",
            "In a nutshell, a quadratic expression is like a mathematical sentence with an 'x squared' term as the superstar.",
            "Think of it like this: you're tossing a ball. The path it takes? That's a parabola, and we can describe it using a quadratic expression. Let's take a look at a simple one.",
            "This is the graph of the simple quadratic expression x squared. See how it makes that graceful, symmetrical curve? That's the signature move of a parabola.",
            "Now, the coefficients 'a', 'b', and 'c' in our general form? They're like the control panel for our parabola. They decide how steep, how wide, and where it sits on the graph.",
            "And that's a quick peek into quadratic expressions! They pop up everywhere, from physics to engineering. So, keep an eye out for those parabolas, you'll be seeing a lot of them!"
        )

        # Introduction
        with self.voiceover(text="Hey there! Today, we're diving into the world of quadratic expressions.") as tracker:
            text = Tex("Quadratic Expressions").scale(1.5).set_color(BLUE)
            self.play(Write(text), run_time=tracker.duration)
            self.wait(0.5)
            self.play(FadeOut(text))

        # What are quadratic expressions?
        with self.voiceover(text="In a nutshell, a quadratic expression is like a mathematical sentence with an 'x squared' term as the superstar.") as tracker:
            text = Tex("General Form: ", "ax² + bx + c").scale(1.2)
            self.play(Write(text), run_time=tracker.duration)
            self.wait(1)
            self.play(FadeOut(text))

        # Example
        with self.voiceover(text="Think of it like this: you're tossing a ball. The path it takes? That's a parabola, and we can describe it using a quadratic expression. Let's take a look at a simple one.") as tracker:
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[-1, 5, 1],
                axis_config={"include_tip": False},
            )
            graph = axes.get_graph(lambda x: x**2)
            graph.set_color(BLUE)
            label = axes.get_graph_label(graph, "x²") 
            label.set_color(YELLOW)
            self.play(Create(axes), run_time=tracker.duration / 2)
            self.play(Create(graph), Write(label), run_time=tracker.duration / 2)
            self.wait(1.5)

        # Explanation
        with self.voiceover(text="This is the graph of the simple quadratic expression x squared. See how it makes that graceful, symmetrical curve? That's the signature move of a parabola.") as tracker:
            dot = Dot(axes.i2gp(1, graph), color=RED)
            self.play(FadeIn(dot), run_time=tracker.duration / 2)
            self.play(
                dot.animate.move_to(axes.i2gp(2, graph)), run_time=tracker.duration / 2
            )
            self.wait(1)

        # Importance of coefficients
        with self.voiceover(text="Now, the coefficients 'a', 'b', and 'c' in our general form? They're like the control panel for our parabola. They decide how steep, how wide, and where it sits on the graph.") as tracker:
            self.play(FadeOut(dot), run_time=tracker.duration)
            text = Tex("a, b, c - Control the parabola").set_color(GREEN).to_edge(DOWN)
            self.play(Write(text), run_time=tracker.duration)
            self.wait(2)

        # Conclusion
        with self.voiceover(text="And that's a quick peek into quadratic expressions! They pop up everywhere, from physics to engineering. So, keep an eye out for those parabolas, you'll be seeing a lot of them!") as tracker:
            self.play(FadeOut(graph), FadeOut(label), FadeOut(axes), FadeOut(text), run_time=tracker.duration)
            self.wait(1)
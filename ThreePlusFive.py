from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class GradientDescent(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )
        
        # Function
        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 10, 1],
            axis_config={"include_tip": False},
        )
        func = lambda x: x**2 + 1
        graph = ax.plot(func, color=BLUE)

        # Initial point
        x = ValueTracker(-2)
        dot = Dot(ax.c2p(x.get_value(), func(x.get_value())), color=RED)

        with self.voiceover(text="Imagine you're standing on this curve, and you want to find the lowest point.") as tracker:
            self.play(Create(ax), run_time=2)
            self.play(Create(graph), run_time=2)
            self.play(Create(dot), run_time=2)

        with self.voiceover(text="You can't see the whole curve, so you need a way to find the minimum just by feeling the slope around you.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="That's where Gradient Descent comes in. It's like taking small steps downhill, following the steepest descent.") as tracker:
            self.wait(tracker.duration)

        # Gradient descent steps
        for i in range(5):
            slope = 2 * x.get_value()
            step_size = 0.3  # Learning rate
            new_x = x.get_value() - step_size * slope
            x.set_value(new_x)

            with self.voiceover(text=f"We calculate the slope at our current location and take a step downhill. The size of the step is controlled by a parameter called the learning rate.") as tracker:
                self.play(dot.animate.move_to(ax.c2p(x.get_value(), func(x.get_value()))), run_time=2)

        with self.voiceover(text="By repeatedly taking these steps, we get closer and closer to the minimum point of the function.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="And that's Gradient Descent in a nutshell! A simple yet powerful algorithm for finding minimums.") as tracker:
            self.wait(tracker.duration)

        self.wait()
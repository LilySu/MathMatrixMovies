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
        
        # Function to minimize
        def f(x):
            return x**2

        # Derivative of f(x)
        def df(x):
            return 2*x
        
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 1],
            axis_config={"include_numbers": True},
        )
        
        # Create graph of f(x)
        graph = axes.plot(f, color=BLUE)

        # Create a dot representing the starting point
        x = 2.5
        dot = Dot(axes.c2p(x, f(x)), color=RED)
        
        # Show axes and graph
        with self.voiceover(text="Let's understand Gradient Descent, an algorithm for finding the minimum of a function.") as tracker:
            self.play(Create(axes), run_time=tracker.duration)
            self.play(Create(graph), run_time=tracker.duration)
            self.wait(1)

        with self.voiceover(text="Imagine you're on a hill, and you want to find the lowest point.") as tracker:
            self.play(FadeIn(dot), run_time=tracker.duration)
            self.wait(1)

        with self.voiceover(text="You can do this by taking steps downhill, in the direction of the steepest descent.") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="The gradient of a function tells us the direction of the steepest ascent. So, we move in the opposite direction.") as tracker:
            self.wait(tracker.duration)

        # Gradient Descent iterations
        for i in range(5):
            # Calculate gradient
            gradient = df(x)

            # Update position 
            x = x - 0.3 * gradient # 0.3 is the learning rate

            # Move dot to new position
            with self.voiceover(text=f"Step {i+1}. We calculate the gradient and take a step downhill.") as tracker:
                self.play(dot.animate.move_to(axes.c2p(x, f(x))), run_time=tracker.duration)
                self.wait(1)

        with self.voiceover(text="We continue this process, taking smaller and smaller steps as we approach the minimum.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Eventually, we converge to the lowest point of the function.") as tracker:
            self.wait(tracker.duration)

        self.wait(2)
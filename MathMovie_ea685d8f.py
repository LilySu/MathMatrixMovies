from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class FiniteFields(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15,
                # Add your Azure credentials here
                # subscription_key="YOUR_SUBSCRIPTION_KEY",
                # service_region="YOUR_SERVICE_REGION" 
            )
        )

        # Title
        title = Text("Exploring Finite Fields: A Clock's Secret").scale(0.8)
        self.play(Write(title))
        with self.voiceover(text="Exploring Finite Fields: A Clock's Secret") as tracker:
            self.wait(tracker.duration)
        self.play(FadeOut(title))

        # Scene 1: Introduction with a Clock
        with self.voiceover(text="Hi everyone! Today, we're going on a mathematical adventure to explore a fascinating concept called 'finite fields.' ") as tracker:
            self.wait(tracker.duration)

        with self.voiceover(text="You might be wondering what those are. Well, imagine a clock face...") as tracker:
            self.wait(tracker.duration)

        clock = Circle(radius=2, color=WHITE).shift(UP*0.5)
        clock_numbers = VGroup(*[
            Text(str(i+1)).move_to(clock.point_at_angle((i/12)*TAU + PI/2)).scale(0.6)
            for i in range(12)
        ])
        self.play(Create(clock), Write(clock_numbers), run_time=2)

        with self.voiceover(text="It has 12 numbers, right? But when we talk about time, we don't go past 12. Instead, we start again from 1. That's the basic idea behind finite fields - they loop around!") as tracker:
            self.play(
                Circumscribe(clock, color=YELLOW, fade_in=True, fade_out=True, run_time=tracker.duration),
            )

        # Scene 2: Introducing Modular Arithmetic
        with self.voiceover(text="Let's try an example. What's 9 + 5 on our clock?") as tracker:
            self.wait(tracker.duration)

        # Correcting the hour hand creation and rotation
        hour_hand = Line(clock.get_center(), clock.point_at_angle((9/12)*TAU + PI/2), stroke_width=8, color=RED).scale(0.7)
        self.play(Create(hour_hand))
        self.play(Rotate(hour_hand, angle=(5/12)*TAU, about_point=np.array(clock.get_center())), run_time=2) 

        with self.voiceover(text="It's 2, not 14! We went past 12 and looped back around. This special kind of math is called modular arithmetic.") as tracker:
            self.wait(tracker.duration)

        # ... (rest of the code is the same)
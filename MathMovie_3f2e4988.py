from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class FiniteFields(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

        # Title
        title = Text("Exploring Finite Fields: A Clock's Secret").scale(0.8)
        self.play(Write(title))
        with self.voiceover(text="Exploring Finite Fields: A Clock's Secret") as tracker:
            self.wait(tracker.duration)
        self.play(FadeOut(title))

        # Scene 1: Introduction with a Clock
        with self.voiceover(text="Hi everyone! Today, we're going on a mathematical adventure to explore a fascinating concept called 'finite fields.' You might be wondering what those are. Well, imagine a clock face.") as tracker:
            self.wait(tracker.duration)

        clock = Circle(radius=2, color=WHITE).shift(UP*0.5)
        clock_numbers = VGroup(*[
            Text(str(i+1)).move_to(clock.point_at_angle((i/12)*TAU + PI/2)).scale(0.6)
            for i in range(12)
        ])
        self.play(Create(clock), Write(clock_numbers))

        with self.voiceover(text="It has 12 numbers, right? But when we talk about time, we don't go past 12. Instead, we start again from 1. That's the basic idea behind finite fields - they loop around!") as tracker:
            self.wait(tracker.duration)

        # Scene 2: Introducing Modular Arithmetic
        with self.voiceover(text="Let's try an example. What's 9 + 5 on our clock?") as tracker:
            self.wait(tracker.duration)

        hour_hand = Line(clock.get_center(), clock_numbers[8].get_center(), stroke_width=8, color=RED).scale(0.7)
        self.play(Create(hour_hand))
        self.play(Rotate(hour_hand, angle=(5/12)*TAU, about_point=clock.get_center()))

        with self.voiceover(text="It's 2, not 14! We went past 12 and looped back around. This special kind of math is called modular arithmetic.") as tracker:
            self.wait(tracker.duration)

        # Scene 3: Defining Finite Fields
        self.play(FadeOut(clock), FadeOut(clock_numbers), FadeOut(hour_hand))

        with self.voiceover(text="Finite fields work similarly. They have a limited number of elements, like the 12 numbers on our clock. And when we add or multiply numbers within the field, we loop back around if we go past the limit.") as tracker:
            self.wait(tracker.duration)

        field_box = Rectangle(width=4, height=2, color=BLUE).shift(UP*0.5)
        field_elements = VGroup(*[
            Text(str(i)).move_to(field_box.get_center() + (i-2)*RIGHT*0.8)
            for i in range(5)
        ])
        self.play(Create(field_box), Write(field_elements))

        with self.voiceover(text="Let's look at this finite field with 5 elements. If we add 3 and 4, we get 7. But since 7 is bigger than our limit, we subtract 5, leaving us with 2.") as tracker:
            self.wait(tracker.duration)

        self.play(field_elements[3].animate.set_color(YELLOW), field_elements[4].animate.set_color(YELLOW))
        temp_sum = Text("7", color=RED).move_to(field_box.get_center() + RIGHT * 3).scale(0.7)
        self.play(Write(temp_sum))
        self.play(FadeOut(temp_sum))
        self.play(Indicate(field_elements[2]))
        self.play(field_elements[3].animate.set_color(WHITE), field_elements[4].animate.set_color(WHITE))

        # Scene 4: Real-World Applications
        with self.voiceover(text="Finite fields are used in lots of cool places, like cryptography - the science of secret codes! They help keep our information safe when we use the internet.") as tracker:
            self.wait(tracker.duration)

        lock = SVGMobject("path/to/lock.svg").scale(0.5).shift(DOWN*0.5) # replace 'path/to/lock.svg' with your svg file
        self.play(Create(lock))

        # Outro
        self.play(FadeOut(field_box), FadeOut(field_elements), FadeOut(lock))

        with self.voiceover(text="So, the next time you look at a clock, remember that you're looking at a simple version of a finite field! They might seem strange at first, but these mathematical structures play a crucial role in our technological world. Thanks for joining me!") as tracker:
            self.wait(tracker.duration)
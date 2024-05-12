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

        # Correcting the hour hand creation
        hour_hand = Line(clock.get_center(), clock.point_at_angle((9/12)*TAU + PI/2), stroke_width=8, color=RED).scale(0.7)
        self.play(Create(hour_hand))
        self.play(Rotate(hour_hand, angle=(5/12)*TAU, about_point=clock.get_center), run_time=2) 

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

        with self.voiceover(text="Let's look at this finite field with 5 elements.  If we add 3 and 4, we get 7.") as tracker:
            self.wait(tracker.duration)

        self.play(field_elements[3].animate.set_color(YELLOW), field_elements[4].animate.set_color(YELLOW), run_time=1) 
        temp_sum = Text("7", color=RED).move_to(field_box.get_center() + RIGHT * 3).scale(0.7)
        self.play(Write(temp_sum))

        with self.voiceover(text="But since 7 is bigger than our limit, we subtract 5, leaving us with 2.") as tracker:
            self.play(Transform(temp_sum, Text("-5", color=RED).move_to(temp_sum.get_center()).scale(0.7)), run_time = 1)
            self.play(
                MoveAlongPath(temp_sum, Arc(radius=1, start_angle=0, angle=PI, color=RED).shift(UP*0.5 + RIGHT*2)),
                temp_sum.animate.scale(0.4),
                run_time = 2,
            )
            self.play(FadeOut(temp_sum))
            self.play(Indicate(field_elements[2]), run_time=1.5) 
            self.play(field_elements[3].animate.set_color(WHITE), field_elements[4].animate.set_color(WHITE), run_time = 1)

        # Scene 4: Real-World Applications
        with self.voiceover(text="Finite fields are used in lots of cool places, like cryptography - the science of secret codes! They help keep our information safe when we use the internet.") as tracker:
            self.wait(tracker.duration)

        # Creating a simple lock shape
        lock_body = Rectangle(width=1, height=1.5, color=GREY).shift(DOWN*0.5)
        lock_top = Arc(radius=0.5, angle=PI, start_angle=PI/2, color=GREY).next_to(lock_body, UP)
        lock_hole = Circle(radius=0.1, color=BLACK, fill_opacity=1).move_to(lock_body.get_center() + UP*0.3)
        lock = VGroup(lock_body, lock_top, lock_hole)
        key = Rectangle(width=0.2, height=0.8, color=YELLOW).rotate(PI/4).next_to(lock_hole, RIGHT, buff=0.1)
        self.play(Create(lock))
        self.play(ShowCreation(key), run_time=0.5)
        self.play(key.animate.shift(LEFT*0.6), run_time=0.5)
        self.play(FadeOut(key), run_time=0.5)

        # Outro
        self.play(FadeOut(field_box), FadeOut(field_elements), FadeOut(lock))

        with self.voiceover(text="So, the next time you look at a clock, remember that you're looking at a simple version of a finite field! They might seem strange at first, but these mathematical structures play a crucial role in our technological world. Thanks for joining me!") as tracker:
            self.wait(tracker.duration)
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class AddingBigNumber(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )
        
        # Title
        title = Text("Adding Big Numbers!").scale(1.5)
        self.play(Write(title))
        self.wait(1)
        with self.voiceover(text="Hello, math whizzes! Today we are going to add two really big numbers, 777 and 999.") as tracker:
            self.play(FadeOut(title), run_time=tracker.duration)

        # Numbers
        num1 = Text("777").scale(2).move_to(2*LEFT)
        num2 = Text("999").scale(2).move_to(2*RIGHT)
        plus_sign = Text("+").scale(2)

        self.play(Write(num1), Write(num2), Write(plus_sign))
        self.wait(1)
        
        with self.voiceover(text="Adding big numbers can seem scary, but it's actually just like adding smaller numbers, just with a few extra steps! Let's break it down together.") as tracker:
            self.wait(tracker.duration)

        # Place value lines
        line1 = Line(start=num1.get_bottom() + DOWN * 0.5, end=num1.get_top() + UP * 0.5).shift(0.3*LEFT)
        line2 = Line(start=num1.get_bottom() + DOWN * 0.5, end=num1.get_top() + UP * 0.5).shift(0.9*LEFT)
        line3 = Line(start=num2.get_bottom() + DOWN * 0.5, end=num2.get_top() + UP * 0.5).shift(0.3*RIGHT)
        line4 = Line(start=num2.get_bottom() + DOWN * 0.5, end=num2.get_top() + UP * 0.5).shift(0.9*RIGHT)

        self.play(Create(line1), Create(line2), Create(line3), Create(line4))
        self.wait(1)

        # Adding ones place
        with self.voiceover(text="First, we add the digits in the ones place, 7 and 9.") as tracker:
            self.play(
                num1[0].animate.set_color(RED), 
                num2[0].animate.set_color(RED),
                run_time=tracker.duration
            )
        self.wait(1)

        with self.voiceover(text="7 plus 9 equals 16.  Since 16 is bigger than 10, we write down the 6 in the ones place and carry-over the 1 to the tens place.") as tracker:
            sum_ones = Text("6").scale(2).next_to(plus_sign, DOWN, buff=1.5).shift(0.9 * RIGHT)
            carry_over_tens = Text("1").scale(0.7).next_to(num1[1], UP, buff=0.2)
            self.play(Write(sum_ones), Write(carry_over_tens), run_time=tracker.duration)
        self.wait(1)

        # Adding tens place
        with self.voiceover(text="Now, let's add the digits in the tens place, remembering to add the carry-over 1. So, it's 7 plus 9 plus 1.") as tracker:
            self.play(
                num1[1].animate.set_color(BLUE), 
                num2[1].animate.set_color(BLUE), 
                carry_over_tens.animate.set_color(BLUE), 
                run_time=tracker.duration
            )
        self.wait(1)

        with self.voiceover(text="7 plus 9 plus 1 equals 17. Again, we write down the 7 in the tens place and carry-over the 1 to the hundreds place.") as tracker:
            sum_tens = Text("7").scale(2).next_to(sum_ones, LEFT)
            carry_over_hundreds = Text("1").scale(0.7).next_to(num1[2], UP, buff=0.2)
            self.play(Write(sum_tens), Write(carry_over_hundreds), run_time=tracker.duration)
        self.wait(1)

        # Adding hundreds place
        with self.voiceover(text="Finally, we add the digits in the hundreds place: 7 plus 9 plus 1.") as tracker:
            self.play(
                num1[2].animate.set_color(GREEN), 
                num2[2].animate.set_color(GREEN), 
                carry_over_hundreds.animate.set_color(GREEN), 
                run_time=tracker.duration
            )
        self.wait(1)

        with self.voiceover(text="That gives us 17! Since this is the last place value, we write down the entire 17. ") as tracker:
            sum_hundreds = Text("17").scale(2).next_to(sum_tens, LEFT)
            self.play(Write(sum_hundreds), run_time=tracker.duration)
        self.wait(1)

        # Final answer
        with self.voiceover(text="So, 777 plus 999 equals 1776!") as tracker:
            final_answer = VGroup(sum_hundreds, sum_tens, sum_ones).copy()
            self.play(
                final_answer.animate.scale(1.2).next_to(plus_sign, DOWN, buff=2), 
                run_time=tracker.duration
            )
        self.wait(2)

        # Outro
        with self.voiceover(text="Great job, everyone! Now you know how to add even the biggest numbers. Keep practicing, and you'll become math superstars!") as tracker:
            self.play(FadeOut(*self.mobjects), run_time=tracker.duration)
        self.wait(1)
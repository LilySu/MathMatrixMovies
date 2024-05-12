from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class AdditionScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )

        # Title
        title = Text("Let's Learn Addition! 🍎➕🍎").scale(1.5)
        self.play(FadeIn(title))
        self.wait(0.5)
        with self.voiceover(text="Hi everyone! Today, we're going to learn how to add!") as tracker:
            self.play(FadeOut(title), run_time=tracker.duration)
        
        # Scene setup
        apple_group1 = VGroup(*[Apple(color=RED) for _ in range(6)]).arrange(RIGHT, buff=0.5)
        apple_group1.to_edge(LEFT, buff=1)
        apple_group2 = VGroup(*[Apple(color=RED) for _ in range(3)]).arrange(RIGHT, buff=0.5)
        apple_group2.to_edge(RIGHT, buff=1)
        plus_sign = Text("+").scale(2).move_to(ORIGIN)

        # Show and count the first group of apples
        self.play(FadeIn(apple_group1))
        with self.voiceover(text="Look! We have six juicy red apples here. Let's count them together: one, two, three, four, five, six.") as tracker:
            for i in range(6):
                self.play(FadeIn(Text(str(i+1)).scale(0.8).next_to(apple_group1[i], UP)), run_time=tracker.duration/6)
            
        # Show and count the second group of apples
        self.play(FadeIn(apple_group2))
        with self.voiceover(text="Wow! Three more delicious red apples just arrived. Let's count these too: one, two, three!") as tracker:
            for i in range(3):
                self.play(FadeIn(Text(str(i+1)).scale(0.8).next_to(apple_group2[i], UP)), run_time=tracker.duration/3)

        # Bringing them together for addition
        self.play(FadeIn(plus_sign))
        with self.voiceover(text="Now, let's add them all together. We had six apples, and then we got three more.") as tracker:
            self.play(apple_group1.animate.shift(2*LEFT), apple_group2.animate.shift(2*RIGHT), run_time=tracker.duration)

        # Counting all the apples
        all_apples = VGroup(*apple_group1, *apple_group2)
        with self.voiceover(text="Six apples plus three apples, how many apples do we have now? Let's count them all!") as tracker:
            for i in range(9):
                self.play(ApplyMethod(all_apples[i].set_fill, YELLOW, opacity=1), run_time=tracker.duration/9)
                self.play(ApplyMethod(all_apples[i].set_fill, RED, opacity=1), run_time=tracker.duration/9)

        # Showing the equation
        equation = Text("6 + 3 = 9").scale(2).set_color_by_gradient(BLUE, GREEN)
        self.play(FadeOut(all_apples), FadeOut(plus_sign))
        with self.voiceover(text="That's right! Six plus three equals nine! You did amazing!") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        self.wait(1)

        # Outro
        outro = Text("You're a Math Whiz! 🎉").scale(1.5)
        self.play(FadeIn(outro))
        with self.voiceover(text="You're a math whiz! See you next time!") as tracker:
            self.play(FadeOut(outro), run_time=tracker.duration)

        self.wait()

class Apple(VMobject):
    def __init__(self, color=RED, **kwargs):
        super().__init__(**kwargs)
        self.body = Ellipse(width=1, height=1.2, color=color, fill_opacity=1).shift(0.1*DOWN)
        self.leaf = Ellipse(width=0.4, height=0.6, color=GREEN, fill_opacity=1).rotate(PI/4).next_to(self.body, UP, buff=0.1)
        self.add(self.body, self.leaf)
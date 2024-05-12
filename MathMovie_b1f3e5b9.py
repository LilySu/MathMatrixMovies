from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class Eigenvectors(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
                global_speed=1.15
            )
        )

        # Title
        title = Text("Eigenvectors: The Stretchers of Linear Transformations", font_size=40)
        self.play(Write(title))
        self.wait()
        with self.voiceover(text="Eigenvectors: The Stretchers of Linear Transformations.") as tracker:
            pass
        self.play(FadeOut(title))

        # Scene 1: Mirror Analogy
        emoji = Text(":)", font_size=100)
        mirror = Line(start=2*LEFT, end=2*RIGHT).set_color(GREY)
        reflected_emoji = emoji.copy().flip().move_to(3*RIGHT)
        
        with self.voiceover(text="Imagine a mirror.") as tracker:
            self.play(FadeIn(mirror))

        with self.voiceover(text="The reflection in the mirror is a transformation of the original image.") as tracker:
            self.play(FadeIn(emoji))
            self.play(FadeIn(reflected_emoji))
            self.wait()

        with self.voiceover(text="It's flipped, but it's still the same basic shape, right?") as tracker:
            pass

        self.play(FadeOut(emoji, mirror, reflected_emoji))

        # Scene 2: Square Stretching
        square = Square(side_length=2).set_color(BLUE)
        rectangle = Rectangle(width=4, height=1).set_color(BLUE).move_to(square)
        diagonal1 = Line(start=square.get_corner(UL), end=square.get_corner(DR)).set_color(RED)
        diagonal2 = Line(start=square.get_corner(UR), end=square.get_corner(DL)).set_color(RED)

        with self.voiceover(text="Now imagine stretching a square into a rectangle.") as tracker:
            self.play(FadeIn(square))
            self.play(Transform(square, rectangle), run_time=2)
            self.wait()

        with self.voiceover(text="Some lines in the square, like its diagonals, change direction during this stretching.") as tracker:
            self.play(FadeIn(diagonal1, diagonal2))
            self.wait()
            self.play(FadeOut(diagonal1, diagonal2))

        # Scene 3: Horizontal & Vertical Lines Remain Unchanged in Direction
        h_line = Line(start=square.get_corner(UL), end=square.get_corner(UR)).set_color(GREEN)
        v_line = Line(start=square.get_corner(UL), end=square.get_corner(DL)).set_color(GREEN)
        
        self.play(Transform(square, rectangle), run_time=2)

        with self.voiceover(text="But the horizontal and vertical lines, they just get longer or shorter, they don't change direction.") as tracker:
            self.play(FadeIn(h_line, v_line))
            self.wait()

        with self.voiceover(text="They stay on the same line they started on.") as tracker:
            pass
        
        # Scene 4: Introducing Eigenvectors
        eigenvector_label_h = Text("Eigenvector", font_size=20).next_to(h_line, UP)
        eigenvector_label_v = Text("Eigenvector", font_size=20).next_to(v_line, LEFT)

        with self.voiceover(text="These special lines are called eigenvectors.") as tracker:
            self.play(FadeIn(eigenvector_label_h, eigenvector_label_v))
            self.wait()

        with self.voiceover(text="Eigenvectors are special vectors that, when a transformation is applied, don't change their direction, they just get scaled - stretched or compressed.") as tracker:
            pass

        # Scene 5: Introducing Eigenvalues
        equation = MathTex("A \\cdot v = \\lambda \\cdot v").move_to(3*DOWN)
        A_label = Text("Transformation", font_size=16).next_to(equation[0], DOWN)
        v_label = Text("Eigenvector", font_size=16).next_to(equation[2], DOWN)
        lambda_label = Text("Eigenvalue (scaling factor)", font_size=16).next_to(equation[4], DOWN)
        
        with self.voiceover(text="How much an eigenvector is stretched or compressed is determined by its eigenvalue.") as tracker:
            self.play(FadeIn(equation))
            self.wait()

        with self.voiceover(text="An eigenvalue is like a scaling factor.") as tracker:
            self.play(FadeIn(A_label, v_label, lambda_label))
            self.wait()

        with self.voiceover(text="You can think of this equation, A times v equals lambda times v, where A is the transformation, v is the eigenvector, and lambda is the eigenvalue.") as tracker:
            pass
        
        with self.voiceover(text="This equation tells us that applying the transformation to an eigenvector is the same as just multiplying it by its eigenvalue.") as tracker:
            pass

        self.wait()

        # Outro
        outro = Text("So, eigenvectors and eigenvalues are like a secret code that helps us understand how transformations work!", font_size=30).move_to(UP)
        outro2 = Text("They are used in many different areas of math, physics, computer science, and even Google's PageRank algorithm!", font_size=20)
        self.play(FadeOut(square, rectangle, h_line, v_line, eigenvector_label_h, eigenvector_label_v, equation, A_label, v_label, lambda_label))
        self.play(Write(outro))
        with self.voiceover(text="So, eigenvectors and eigenvalues are like a secret code that helps us understand how transformations work!") as tracker:
            pass

        self.play(Write(outro2))
        with self.voiceover(text="They are used in many different areas of math, physics, computer science, and even Google's PageRank algorithm!") as tracker:
            pass

        self.wait(2)
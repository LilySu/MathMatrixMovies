from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class BezierCurvesExplained(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )

        # Introduction
        with self.voiceover(text="Imagine you're drawing a smooth curve, but instead of using a single line, you're using special points to guide the curve's shape. These points are called control points, and they're the key to understanding Bezier curves.") as tracker:
            title = Text("Bezier Curves", font_size=48).shift(UP * 2)
            self.play(Write(title), run_time=tracker.duration)

        # Two control points
        with self.voiceover(text="Let's start with the simplest form: a linear Bezier curve. We'll need two control points, which we'll mark as A and B.") as tracker:
            dot_A = Dot(LEFT * 3, color=RED).set_label("A")
            dot_B = Dot(RIGHT * 3, color=BLUE).set_label("B")
            self.play(FadeIn(dot_A), FadeIn(dot_B), run_time=tracker.duration)

        with self.voiceover(text="Now, imagine a line connecting points A and B. This line represents our curve, but it's not very interesting yet.") as tracker:
            line_AB = Line(dot_A.get_center(), dot_B.get_center())
            self.play(Create(line_AB), run_time=tracker.duration)

        # Moving dot on the line
        with self.voiceover(text="Here's where the magic happens. Let's introduce a moving dot that travels from point A to point B. As this dot moves, it traces out our Bezier curve.") as tracker:
            dot_moving = Dot(LEFT * 3, color=YELLOW)
            self.play(FadeIn(dot_moving), run_time=tracker.duration)

        with self.voiceover(text="In this case, the curve is simply a straight line, as the moving dot follows the direct path from A to B.") as tracker:
            self.play(MoveAlongPath(dot_moving, line_AB), run_time=tracker.duration)
            self.play(FadeOut(dot_moving), run_time=0.5)

        # Three control points
        with self.voiceover(text="Let's add another control point, C, and see how it changes our curve. This becomes a quadratic Bezier curve.") as tracker:
            dot_C = Dot(UP * 3, color=GREEN).set_label("C")
            self.play(FadeIn(dot_C), run_time=tracker.duration)

        with self.voiceover(text="Instead of one line, we now have two: A to C and C to B.") as tracker:
            line_AC = Line(dot_A.get_center(), dot_C.get_center())
            line_CB = Line(dot_C.get_center(), dot_B.get_center())
            self.play(Create(line_AC), Create(line_CB), run_time=tracker.duration)

        with self.voiceover(text="Now imagine two moving dots, one on each line. These dots move simultaneously from A to C and C to B.") as tracker:
            dot_AC = Dot(LEFT * 3, color=YELLOW)
            dot_CB = Dot(UP * 3, color=YELLOW)
            self.play(FadeIn(dot_AC), FadeIn(dot_CB), run_time=tracker.duration)

        with self.voiceover(text="As they move, we draw a line connecting them. This line's movement traces out our quadratic Bezier curve.") as tracker:
            line_moving = Line(dot_AC.get_center(), dot_CB.get_center()).set_color(PINK)
            self.play(Create(line_moving), run_time=tracker.duration)
            self.play(
                MoveAlongPath(dot_AC, line_AC),
                MoveAlongPath(dot_CB, line_CB),
                UpdateFromFunc(line_moving, lambda z: z.become(Line(dot_AC.get_center(), dot_CB.get_center()).set_color(PINK))),
                run_time=tracker.duration
            )
            self.play(FadeOut(dot_AC), FadeOut(dot_CB), FadeOut(line_moving), run_time=0.5)

        # Visualizing the Bezier curve
        with self.voiceover(text="Let's visualize the final curve, the smooth path created by the moving line.") as tracker:
            bezier_curve = CubicBezier(dot_A.get_center(), dot_C.get_center(), dot_C.get_center(), dot_B.get_center()).set_color(ORANGE)
            self.play(Create(bezier_curve), run_time=tracker.duration)

        # Conclusion
        with self.voiceover(text="That's a quadratic Bezier curve! By adding more control points, we can create even more complex and interesting curves. These curves are used in everything from computer graphics and animation to font design and computer-aided design.") as tracker:
            self.play(FadeOut(line_AB), FadeOut(line_AC), FadeOut(line_CB), run_time=tracker.duration)
            self.wait()
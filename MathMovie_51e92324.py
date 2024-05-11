from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class ChessMoves(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",
            )
        )
        # Introduction
        with self.voiceover(text="Imagine a game of chess.  After just the first few moves, things can get really complex, really quickly!") as tracker:
            pass

        with self.voiceover(text="Let's explore the sheer number of possible moves after only 10 moves.") as tracker:
            pass

        # Illustrating Growth
        number_plane = NumberPlane(
            x_range=[0, 11, 1],
            y_range=[0, 40000000, 10000000],
            x_length=10,
            y_length=7,
            axis_config={"include_numbers": True, "label_direction": DOWN},
        ).to_edge(LEFT, buff=0.5)

        dots = VGroup()
        y_values = [1, 20, 400, 8902, 197281, 4865609, 119060324, 3195901860]  # Approximation of the real values 
        for i, y in enumerate(y_values):
            dot = Dot(number_plane.c2p(i+1, y), color=YELLOW)
            dots.add(dot)

        with self.voiceover(text="This graph shows approximately how many different chess games are possible after each move.") as tracker:
            self.play(Create(number_plane), run_time=tracker.duration)

        with self.voiceover(text="After just one move per player, there are already 20 possible games!") as tracker:
            self.play(Create(dots[0:2]), run_time=tracker.duration)

        with self.voiceover(text="That number jumps to 400 after two moves each.") as tracker:
            self.play(Create(dots[2]), run_time=tracker.duration)

        with self.voiceover(text="After five moves, it's already hard to imagine: almost 200,000 possible games!") as tracker:
            self.play(Create(dots[3:5]), run_time=tracker.duration)

        with self.voiceover(text="But after 10 moves, things explode.") as tracker:
            self.play(Create(dots[5:8]), run_time=tracker.duration)

        # Emphasize the huge number
        final_number = MathTex(r"3,195,901,860").scale(1.5).next_to(dots[-1], RIGHT)
        brace = Brace(final_number, UP)
        brace_text = brace.get_text("Over 3 billion!")

        with self.voiceover(text="Over 3 billion different possible chess games exist after just 10 moves!") as tracker:
            self.play(FadeIn(final_number), FadeIn(brace), FadeIn(brace_text), run_time=tracker.duration)

        # Conclusion
        with self.voiceover(text="That's why chess is so amazing.  It's a game of near infinite possibilities, even in just a few moves.") as tracker:
            pass

        self.wait(2)
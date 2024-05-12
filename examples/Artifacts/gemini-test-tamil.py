from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class IntegralCalculusExplanationTamil(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="ta-IN-ValluvarNeural",
                style="newscast-casual",
            )
        )
        # Introduction
        with self.voiceover(text="சரி, இன்டெக்ரல் கால்குலஸ் பத்தி கொஞ்சம் ஆழமா பாக்கலாம்!") as tracker:
            intro_text = Text("இன்டெக்ரல் கால்குலஸ்", font='Lohit Tamil').scale(1.5)
            self.play(Write(intro_text), run_time=tracker.duration)
        self.wait(0.5)
        self.play(FadeOut(intro_text))

        # Area under the curve
        with self.voiceover(text="இங்க ஒரு வளைவு இருக்குனு வச்சுக்கோங்க, இது மாதிரி.") as tracker:
            axes = Axes(
                x_range=[0, 5, 1],
                y_range=[0, 8, 2],
                x_length=5,
                y_length=4,
                axis_config={"include_numbers": True},
            )
            graph = axes.plot(lambda x: x**2, color=BLUE)
            self.play(Create(axes), run_time=tracker.duration/2)
            self.play(Create(graph), run_time=tracker.duration/2)
        self.wait(0.5)

        with self.voiceover(text="இந்த வளைவுக்கு கீழ இருக்கிற பரப்பளவ கண்டுபிடிக்க இன்டெக்ரல் கால்குலஸ் உதவுது.") as tracker:
            area = axes.get_area(graph, x_range=[1, 4], color=[BLUE_D, BLUE_E])
            self.play(FadeIn(area), run_time=tracker.duration)
        self.wait(0.5)

        # Rectangles and approximation
        with self.voiceover(text="இந்த பரப்பளவை செவ்வகங்களை பயன்படுத்தி தோராயமா கணக்கிடலாம்.") as tracker:
            rects = axes.get_riemann_rectangles(
                graph,
                x_range=[1, 4],
                dx=0.5,
                input_sample_type="right",
            )
            self.play(Create(rects), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="செவ்வகங்கள் எவ்வளவு மெல்லியதோ, அவ்வளவு துல்லியமா நம்ம தோராயம் இருக்கும்.") as tracker:
            for dx in [0.25, 0.1, 0.05]:
                new_rects = axes.get_riemann_rectangles(
                    graph,
                    x_range=[1, 4],
                    dx=dx,
                    input_sample_type="right",
                )
                self.play(Transform(rects, new_rects),
                          run_time=tracker.duration / 3)
        self.wait(0.5)

        # The integral symbol
        with self.voiceover(text="துல்லியமான பரப்பளவை கண்டுபிடிக்கிற இந்த செயல்முறைக்கு இன்டெக்ரல் சின்னத்தை பயன்படுத்துறோம்.") as tracker:
            integral_symbol = Tex(r"$\int$")
            self.play(FadeOut(rects), run_time=tracker.duration/2)
            self.play(Write(integral_symbol), run_time=tracker.duration/2)
        self.wait(0.5)

        # Function and limits of integration
        with self.voiceover(text="நாம ஒரு சார்ப  ஒருங்கிணைக்கிறோம், இந்த விஷயத்துல, எக்ஸ் ஸ்கொயர்ட்.") as tracker:
            function_text = Tex(r"$x^2$").next_to(integral_symbol, RIGHT)
            self.play(Write(function_text), run_time=tracker.duration)
        self.wait(0.5)

        with self.voiceover(text="ஒருங்கிணைப்பு எல்லைகளை 1 லிருந்து 4 வரை குறிப்பிடுறோம்.") as tracker:
            limits = Tex("1", r"$\,$", "4").scale(0.7)
            limits[0].next_to(integral_symbol, DOWN, buff=0.1)
            limits[2].next_to(integral_symbol, UP, buff=0.1)
            self.play(Write(limits), run_time=tracker.duration)
        self.wait(0.5)

        # Conclusion
        with self.voiceover(text="இந்த இன்டெக்ரல் இந்த எல்லைகளுக்கு இடையில உள்ள வளைவுக்கு கீழ துல்லியமான பரப்பளவை தருது.") as tracker:
            self.play(FadeOut(axes), FadeOut(graph), FadeOut(
                area), run_time=tracker.duration/2)
            self.play(
                integral_symbol.animate.scale(2).move_to(ORIGIN),
                function_text.animate.scale(2).next_to(integral_symbol, RIGHT),
                limits.animate.scale(2).next_to(integral_symbol, DOWN),
                run_time=tracker.duration/2
            )
        self.wait(1)

        with self.voiceover(text="இன்டெக்ரல் கால்குலஸின் ஆற்றலை பத்தி இது ஒரு சின்ன எடுத்துக்காட்டு!") as tracker:
            self.play(FadeOut(integral_symbol), FadeOut(function_text),
                      FadeOut(limits), run_time=tracker.duration)
        self.wait(1)

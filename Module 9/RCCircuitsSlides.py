
from manim import *
from manim_slides import Slide

class RCCircuitSlides(Slide):
    def construct(self):
        # Slide 1: RC circuit setup
        title = Text("RC Circuit Analysis", font_size=48)
        eq1 = MathTex("C \, \frac{dV_c(t)}{dt} = \frac{V_s - V_c(t)}{R}")
        self.play(Write(title))
        self.next_slide()

        self.play(Transform(title, Text("Step 1: Setting Up KCL")))
        self.play(Write(eq1))
        self.next_slide()

        eq2 = MathTex("\frac{dV_c(t)}{dt} + \frac{V_c(t)}{RC} = \frac{V_s}{RC}")
        self.play(Transform(eq1, eq2))
        self.next_slide()

        # Slide 2: Integrating factor and simplification
        eq3 = MathTex("\mu = e^{\int \frac{1}{RC} dt} = e^{\frac{t}{RC}}")
        eq4 = MathTex("\frac{d}{dt}(e^{\frac{t}{RC}} V_c(t)) = \frac{V_s}{RC} e^{\frac{t}{RC}}")
        self.play(FadeOut(title), Write(eq3))
        self.next_slide()

        self.play(Transform(eq3, eq4))
        self.next_slide()

        # Slide 3: General solution
        eq5 = MathTex("V_c(t) = V_s + A e^{-\frac{t}{RC}}")
        self.play(Transform(eq4, eq5))
        self.next_slide()

        # Slide 4: RL circuit setup
        rl_title = Text("RL Circuit Analysis", font_size=48)
        self.play(FadeOut(eq5), Write(rl_title))
        self.next_slide()

        eq6 = MathTex("L \, \frac{di(t)}{dt} + R i(t) = V_s")
        self.play(Write(eq6))
        self.next_slide()

        eq7 = MathTex("\frac{di(t)}{dt} + \frac{R}{L} i(t) = \frac{V_s}{L}")
        self.play(Transform(eq6, eq7))
        self.next_slide()

        eq8 = MathTex("i(t) = \frac{V_s}{R} + A e^{-\frac{R}{L}t}")
        self.play(Write(eq8))
        self.next_slide()

        final = Text("Generalized Form Complete!", font_size=36)
        self.play(FadeOut(eq8), Write(final))
        self.next_slide()

from manim import *
from manim_slides import Slide
from manim_circuit import *

class RLCircuitSlides(Slide):
    def construct(self):
        # Slide 1: RL circuit setup
        title = Text("RL Circuit Analysis", font_size=48).to_edge(UP)
        circuit = Circuit()
        v = VoltageSource()
        v.remove(v.label)
        r = Resistor("", direction=RIGHT).shift(UP * 1 + RIGHT * 1)
        r.remove(r.label)
        ind = Inductor("").rotate(DEGREES * 90).shift(RIGHT * 2.5)
        ind.remove(ind.label)
        circuit.add(v, r, ind)
        circuit.add_wire(v.get_terminals("positive"), r.get_terminals("left"))
        circuit.add_wire(r.get_terminals("right"), ind.get_terminals("right"), invert=True)
        line1 = Line(start=ind.get_terminals("left"), end=ind.get_terminals("left") + (0, -1, 0))
        endpoint = (v.get_terminals("negative")) * (1,0,1) + (ind.get_terminals("left") + (0,-1,0)) * (0,1,0)
        line2 = Line(start=v.get_terminals("negative"), end=endpoint)
        line3 = Line(start=ind.get_terminals("left") + (0, -1, 0), end=endpoint)
        circuit.add(line1, line2, line3)
        circuit.scale(0.8).next_to(title, DOWN, buff=0.2).to_edge(LEFT)

        eq = Tex(r"$I_L = I_R$").next_to(title, DOWN, buff=0.2)
        eq1 = Tex(r"$L \cdot \frac{dI_L(t)}{dt} + R I_L(t) = V_s$").next_to(eq, DOWN, buff=0.2)
        self.play(Write(title))
        self.play(FadeIn(circuit))
        self.next_slide()

        self.play(Transform(title, Text("Step 1: Setting Up KVL").to_edge(UP)), Write(eq))
        self.play(Write(eq1))
        self.next_slide()

        eq2 = Tex(r"$\frac{dI_L(t)}{dt} + \frac{R}{L} I_L(t) = \frac{V_s}{L}$").next_to(eq1, DOWN, buff=0.2)
        self.play(Write(eq2))
        self.next_slide()

        # Slide 2: Integrating factor and simplification
        rs = Tex(r"First order differential equation, of the form $y'+p(x)y=A$").to_edge(UP)
        self.play(Transform(title, rs), FadeOut(circuit))
        self.play(FadeOut(eq, eq1), eq2.animate.next_to(title, DOWN, buff=0.2))
        eq3 = Tex(r"$\mu = e^{\int \frac{R}{L} dt} = e^{\frac{R}{L}t}$").next_to(eq2, DOWN, buff=0.2)
        eq_new = Tex(r"Multiply Through: $e^{\frac{R}{L}t}\frac{dI_L(t)}{dt}+e^{\frac{R}{L}t}\frac{R}{L}I_L(t)=e^{\frac{R}{L}t}\frac{V_s}{L}$").next_to(eq3, DOWN, buff=.2)
        eq4 = Tex(r"$\frac{d}{dx}\left[ f(x)g(x) \right] = f'(x)g(x) + f(x)g'(x)$").next_to(eq_new, DOWN, buff=0.2)
        self.play(Write(eq3))
        self.play(Write(eq_new))
        self.play(Write(eq4))
        self.next_slide()

        eq5 = Tex(r"$\frac{d}{dt}(e^{\frac{R}{L}t} I_L(t)) = \frac{V_s}{L} e^{\frac{R}{L}t}$").next_to(eq4, DOWN, buff=0.2)
        self.play(Write(eq5))
        eq6 = Tex(r"$\int \frac{d}{dt}(e^{\frac{R}{L}t}I_L(t))=\int \frac{V_s}{L}e^{\frac{R}{L}t} dt$").next_to(eq5, DOWN, buff=0.2)
        self.play(Write(eq6))
        eq7 = Tex(r"$e^{\frac{R}{L}t}I_L(t)=\frac{V_s L}{R}e^{\frac{R}{L}t}+A$").next_to(eq6, DOWN, buff=0.2)
        self.play(Write(eq7))
        self.next_slide()

        all_mobs = self.mobjects.copy()
        all_mobs.remove(title)
        all_mobs.remove(eq7)
        self.play(*[FadeOut(mob) for mob in all_mobs], eq7.animate.next_to(title, DOWN, buff=0.2))

        eq8 = Tex(r"Simplify: $I_L(t) = \frac{V_s}{R} + A e^{-\frac{R}{L}t}$").next_to(eq7, DOWN, buff=0.2)
        self.play(Write(eq8), FadeIn(circuit))
        self.next_slide()

        self.play(FadeOut(eq7), eq8.animate.next_to(title, DOWN, buff=0.2))
        eq9 = Tex(r"Assume switch closed at $t=0$").next_to(eq8, DOWN, buff=0.1).shift(RIGHT * 0.75)
        eq10 = Tex(r"$I_L(0) = 0$, $I_L(\infty) = \frac{V_s}{R}$").next_to(eq9, DOWN, buff=0.1)
        eq11 = Tex(r"$I_L(0) = A + \frac{V_s}{R}$").next_to(eq10, DOWN, buff=0.1)
        eq13 = MathTex(r"\boxed{I_L(t) = \left(I_L(t_0)-I_L(\infty)\right)e^{-tR/L}+I_L(\infty)}").next_to(eq11, DOWN, buff=0.1)
        self.play(Write(eq9))
        self.play(Write(eq10))
        self.play(Write(eq11))
        self.play(Write(eq13))
        self.next_slide()

        # Plotting current response
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        V_s = 5
        R = 1
        L = 1
        tau = L / R

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, V_s + 1, 1],
            x_length=10,
            y_length=4,
            axis_config={"include_numbers": True}
        ).to_edge(DOWN).shift(UP * .5)

        labels = axes.get_axis_labels(x_label="t (s)", y_label="I_L(t)")
        charging_curve = axes.plot(lambda t: V_s / R * (1 - np.exp(-t / tau)), x_range=[0, 5], color=YELLOW)
        charging_label = MathTex(r"I_L(t) = \frac{V_s}{R}(1 - e^{-tR/L})").to_edge(UP)

        self.play(Create(axes), Write(labels))
        self.play(Write(charging_label))
        self.play(Create(charging_curve), run_time=3)

        self.next_slide()

        discharge_curve = axes.plot(lambda t: V_s / R * np.exp(-t / tau), x_range=[0, 5], color=BLUE)
        discharge_label = MathTex(r"I_L(t) = \frac{V_s}{R} e^{-tR/L}").next_to(charging_label, DOWN)

        self.play(Write(discharge_label))
        self.play(Create(discharge_curve), run_time=3)
        self.wait()

        self.next_slide()
        self.play(FadeOut(charging_curve), FadeOut(charging_label), FadeOut(discharge_curve), FadeOut(discharge_label))

        I_0 = 2
        charging_from_2 = axes.plot(
            lambda t: I_0 + (V_s / R - I_0) * (1 - np.exp(-t / tau)),
            x_range=[0, 5],
            color=GREEN
        )
        charging_from_2_label = MathTex(
            r"I_L(t) = 2 + \left(\frac{V_s}{R} - 2\right)(1 - e^{-tR/L})"
        ).to_edge(UP)

        self.play(Write(charging_from_2_label))
        self.play(Create(charging_from_2), run_time=3)

        self.next_slide()

        discharging_to_2 = axes.plot(
            lambda t: I_0 + (V_s / R - I_0) * np.exp(-t / tau),
            x_range=[0, 5],
            color=RED
        )
        discharging_to_2_label = MathTex(
            r"I_L(t) = 2 + \left(\frac{V_s}{R} - 2\right)e^{-tR/L}"
        ).next_to(charging_from_2_label, DOWN)

        self.play(Write(discharging_to_2_label))
        self.play(Create(discharging_to_2), run_time=3)
        self.wait()

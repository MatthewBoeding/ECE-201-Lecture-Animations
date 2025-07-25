
from manim import *
from manim_slides import Slide
from manim_circuit import *

class RCCircuitSlides(Slide):
    def construct(self):
        # Slide 1: RC circuit setup
        title = Text("RC Circuit Analysis", font_size=48).to_edge(UP)
        circuit = Circuit()
        v = VoltageSource()
        v.remove(v.label)
        r =  Resistor("", direction=RIGHT).shift(UP*1+RIGHT*1)
        r.remove(r.label)
        cap = Capacitor("").rotate(DEGREES*90).shift(RIGHT*2.5)
        cap.remove(cap.label)
        circuit.add(v,r,cap)
        circuit.add_wire(v.get_terminals("positive"), r.get_terminals("left"))
        circuit.add_wire(r.get_terminals("right"), cap.get_terminals("right"), invert = True)
        line1 = Line(start = cap.get_terminals("left"), end = cap.get_terminals("left")+(0,-1,0))
        line2 = Line(start = v.get_terminals("negative"), end = v.get_terminals("negative")+(0,-.5,0))
        line3 = Line(start = cap.get_terminals("left")+(0,-1,0), end = v.get_terminals("negative")+(0,-.5,0))
        circuit.add(line1, line2, line3)
        #circuit.add_wire(cap.get_terminals("left"), v.get_terminals("negative"))
        circuit.scale(.8).next_to(title, DOWN, buff = 0.2).to_edge(LEFT)
        eq = Tex(r"$I_C = I_R$").next_to(title, DOWN, buff = 0.2)
        eq1 = Tex(r"$C \cdot \frac{dV_c(t)}{dt} = \frac{V_s - V_c(t)}{R}$").next_to(eq, DOWN, buff = 0.2)
        self.play(Write(title))
        self.play(FadeIn(circuit))
        self.next_slide()

        self.play(Transform(title, Text("Step 1: Setting Up KCL").to_edge(UP)), Write(eq))
        self.play(Write(eq1))
        self.next_slide()

        eq2 = Tex(r"$\frac{dV_c(t)}{dt} + \frac{V_c(t)}{RC} = \frac{V_s}{RC}$").next_to(eq1, DOWN, buff = 0.2)
        self.play(Write(eq2))
        self.next_slide()



        # Slide 2: Integrating factor and simplification
        rs = Tex(r"First order differential equation, of the form $y'+p(x)y=A$").to_edge(UP)

        #self.play()
        self.play(Transform(title, rs), FadeOut(circuit))
        self.play(FadeOut(eq, eq1), eq2.animate.next_to(title, DOWN, buff=0.2))
        eq3 = Tex(r"$\mu = e^{\int \frac{1}{RC} dt} = e^{\frac{t}{RC}}$").next_to(eq2, DOWN, buff = 0.2)
        eq_new = Tex(r"Multiply Through: $e^{\frac{1}{RC}t}\frac{dV_c(t)}{dt}+e^{\frac{1}{RC}t}\frac{V_c(t)}{RC}=e^{\frac{1}{RC}t}\frac{V_s}{RC}$").next_to(eq3, DOWN, buff = .2)
        eq4 = Tex(r"$\frac{d}{dx}\left[ f(x)g(x) \right] = f'(x)g(x) + f(x)g'(x)$").next_to(eq_new, DOWN, buff = 0.2)
        self.play(Write(eq3))
        self.play(Write(eq_new))
        self.play(Write(eq4))
        self.next_slide()

        eq5 = Tex(r"$\frac{d}{dt}(e^{\frac{t}{RC}} V_c(t)) = \frac{V_s}{RC} e^{\frac{t}{RC}}$").next_to(eq4, DOWN, buff = 0.2)
        self.play(Write(eq5))
        eq6 = Tex(r"$\int \frac{d}{dt}(e^{\frac{1}{RC}t}V_c(t))=\int \frac{V_s}{RC}e^{\frac{1}{RC}t} dt$").next_to(eq5, DOWN, buff = 0.2)
        self.play(Write(eq6))
        eq7 = Tex(r"$e^{\frac{1}{RC}t}V_c(t)=V_se^{\frac{1}{RC}t}+A$").next_to(eq6, DOWN, buff = 0.2)
        self.play(Write(eq7))

        self.next_slide()
        all_mobs = self.mobjects.copy()

        # Remove 'title' from the list
        all_mobs.remove(title)
        all_mobs.remove(eq7)
        self.play(*[FadeOut(mob) for mob in all_mobs], eq7.animate.next_to(title, DOWN, buff = 0.2))
        eq8 = Tex(r"Simplify: $V_c(t) = V_s + Ae^{-\frac{1}{RC}t}$").next_to(eq7, DOWN, buff = .2)
        self.play(Write(eq8), FadeIn(circuit))

        self.next_slide()
        self.play(FadeOut(eq7), eq8.animate.next_to(title, DOWN, buff = .2))
        eq9 = Tex(r"Consider power $V_s$ is connected at $t=0$").next_to(eq8, DOWN, buff = .1).shift(RIGHT*.75)
        eq10 = Tex(r"$V_c(0) = 0$ and $V_c(\infty) = V_s$").next_to(eq9, DOWN, buff = .1)
        eq11 = Tex(r"Consider $t=0 \implies e^0 = 1$").next_to(eq10, DOWN, buff = .1)
        eq12 = Tex(r"so $V_c(0) = A +V_s$ and $V_c(\infty) = V_s$").next_to(eq11, DOWN, buff = .1)
        eq13 = MathTex(r"\boxed{V_c(t) = (V_c(t_0)-V_c(\infty))e^{-t/RC}+V_c(\infty); \; t\ge t_0}").next_to(eq12, DOWN, buff = .1)
        self.play(Write(eq9))
        self.play(Write(eq10))
        self.play(Write(eq11))
        self.play(Write(eq12))
        self.play(Write(eq13))

        '''slide'''
        self.next_slide()
        all_mobs = self.mobjects.copy()
        self.play(*[FadeOut(mob) for mob in all_mobs])
        # Parameters
        V_s = 5      # Source voltage (volts)
        R = 1        # Resistance (ohms)
        C = 1        # Capacitance (farads)
        tau = R * C  # Time constant

        # Axes setup
        axes = Axes(
            x_range=[0, 5, 1],  # Time from 0 to 5 seconds
            y_range=[0, V_s + 1, 1],  # Voltage range
            x_length=10,
            y_length=4,
            axis_config={"include_numbers": True}
        ).to_edge(DOWN).shift(UP*1)

        labels = axes.get_axis_labels(x_label="t (s)", y_label="V_c(t)")

        # Charging function: Vc(t) = Vs * (1 - e^(-t/RC))
        charging_curve = axes.plot(
            lambda t: V_s * (1 - np.exp(-t / tau)),
            x_range=[0, 5],
            color=YELLOW
        )

        charging_label = MathTex(r"V_c(t) = V_s(1 - e^{-t/RC})").to_edge(UP)

        # Animate
        self.play(Create(axes), Write(labels))
        self.play(Write(charging_label))
        self.play(Create(charging_curve), run_time=3)

        ''' slide'''
        self.next_slide()  # Wait for click / transition

        # Discharge plot (overlapping same axes)
        discharge_curve = axes.plot(
            lambda t: V_s * np.exp(-t / tau),
            x_range=[0, 5],
            color=BLUE
        )
        discharge_label = MathTex(r"V_c(t) = V_s e^{-t/RC}").next_to(charging_label, DOWN)

        self.play(Write(discharge_label))
        self.play(Create(discharge_curve), run_time=3)
        self.wait()
        self.next_slide()
        '''
        slide
        '''
        self.play(FadeOut(discharge_curve), FadeOut(charging_curve), FadeOut(discharge_label), FadeOut(charging_label))
        # New initial voltage
        V_0 = 2  # Starting voltage for both charge and discharge

        # Charging from 2V to 5V
        charging_from_2 = axes.plot(
            lambda t: V_0 + (V_s - V_0) * (1 - np.exp(-t / tau)),
            x_range=[0, 5],
            color=GREEN
        )
        charging_from_2_label = MathTex(
            r"V_c(t) = 2 + (V_s - 2)(1 - e^{-t/RC})"
        ).to_edge(UP)

        self.play(Write(charging_from_2_label))
        self.play(Create(charging_from_2), run_time=3)

        ''' slide '''
        self.next_slide()

        # Discharging to 2V
        discharging_to_2 = axes.plot(
            lambda t: V_0 + (V_s - V_0) * np.exp(-t / tau),
            x_range=[0, 5],
            color=RED
        )
        discharging_to_2_label = MathTex(
            r"V_c(t) = 2 + (V_s - 2)e^{-t/RC}"
        ).next_to(charging_from_2_label, DOWN)

        self.play(Write(discharging_to_2_label))
        self.play(Create(discharging_to_2), run_time=3)
        self.wait()

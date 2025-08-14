from manim import *
from manim_slides import Slide
from manim_circuit import *
import numpy as np

def power_efficiency_plot():
    rs = np.linspace(2000, 2000, 50)
    rl = np.linspace(10, 10000, 50)
    x_vals = rl / rs
    y_vals = np.linspace(1,1,50) / (1+rs/rl)

    return x_vals, y_vals

def power_transfer_ratio():
    rs = np.linspace(2000, 2000, 50)
    rl = np.linspace(10, 10000, 50)
    x_vals = rl/rs
    power_max = (20 /np.multiply((rs+rs),(rs+rs))) * rs
    curr_power = (20 / np.multiply((rl+rs),(rl+rs))) * rl
    y_vals = curr_power / power_max
    return x_vals, y_vals

class MaxPowerTransfer(Slide):
    def construct(self):
        # === Title ===
        title = Tex("Maximum Power Transfer Theorem").scale(1.2).to_edge(UP)
        self.play(Write(title))
        
        
        circuit = Circuit()
        vo = VoltageSource(value = " ",label=False, dependent = False)
        vo.remove(vo.label)
        vo_lab = Tex(r"$V_{TH}$").next_to(vo, LEFT, buff=0.2)
        rth = Resistor().next_to(vo, RIGHT, buff=0.5).shift(UP*1)
        rl = Resistor().rotate(90*DEGREES).next_to(vo, RIGHT, buff=0.2).shift(RIGHT*3)
        rth.remove(rth.label)
        rl.remove(rl.label)
        rth_lab = Tex(r"$R_{TH}$").next_to(rth, UP, buff=.2)
        rl_lab = Tex(r"$R_L$").next_to(rl, RIGHT, buff=.2)
        circuit.add(vo,rth,rl,rth_lab,rl_lab, vo_lab).scale(.6)
        circuit.add_wire(vo.get_terminals("positive"), rth.get_terminals("left"))
        circuit.add_wire(rth.get_terminals("right"), rl.get_terminals("right"), invert=True)
        circuit.add_wire(rl.get_terminals("left"), vo.get_terminals("negative"), invert=True)
        self.play(FadeIn(circuit))
        self.next_slide()
        self.play(Transform(title, Tex(r"Derivation: Maximum Power Transfer").scale(1.1).to_edge(UP)))
        self.wait()
        self.play(circuit.animate.to_edge(LEFT))
        # Step 1: Define power equation
        eq1 = MathTex(
            r"P = \frac{V_{th}^2 R_L}{(R_{th} + R_L)^2}"
        ).scale(0.7).next_to(title, DOWN, buff=0.2).to_edge(RIGHT)
        self.play(Write(eq1))
        self.wait()

        self.next_slide()

        # Step 2: Differentiate P w.r.t R_L
        eq2 = MathTex(
            r"\frac{dP}{dR_L} = \frac{V_{th}^2 \left[(R_{th} + R_L)^2 - 2R_L(R_{th} + R_L)\right]}{(R_{th} + R_L)^4}"
        ).scale(0.7).next_to(eq1, DOWN, buff=0.2).to_edge(RIGHT)
        self.play(Write(eq2))
        self.wait()

        self.next_slide()

        # Step 3: Set derivative = 0
        eq3 = MathTex(
            r"\frac{dP}{dR_L} = 0 \Rightarrow (R_{th} + R_L)^2 = 2R_L(R_{th} + R_L)"
        ).scale(0.7).next_to(eq2, DOWN, buff=0.2).to_edge(RIGHT)
        self.play(Write(eq3))
        self.wait()

        self.next_slide()

        # Step 4: Solve for R_L
        eq4 = MathTex(
            r"(R_{th} + R_L)^2 = 2R_L(R_{th} + R_L) \\ \Rightarrow R_{th} + R_L = 2R_L \\ \Rightarrow R_{th} = R_L"
        ).scale(0.7).next_to(eq3, DOWN, buff=0.2).to_edge(RIGHT)
        self.play(Write(eq4))
        self.wait()

        self.next_slide()

        # Final box
        result = Tex(r"\\[1em]Maximum power transfer occurs when:", r"$\quad R_L = R_{th}$").scale(0.9).set_color(YELLOW).next_to(eq4, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(result))
        self.wait()
        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.play(FadeIn(circuit))
        title = Tex(r"Power Transfer vs Efficiency").to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[0, 5, .5],
            y_range=[0,1,.1],
            x_length=10,
            y_length=10,
            axis_config={"include_numbers": True},
            tips=False,
        )
        axes.scale(.4).shift(RIGHT*.5)
        axes_labels = axes.get_axis_labels(x_label=r"\frac{R_L}{R_{TH}}", y_label=r"\frac{P}{P_{max}}/\frac{P_{R_L}}{P_T}")
        
        x_pow_eff, y_pow_eff = power_efficiency_plot()
        graph = axes.plot_line_graph(
            x_values=x_pow_eff,
            y_values=y_pow_eff,
            line_color=RED,
            add_vertex_dots=False
        )

        x_pow_tran, y_pow_tran = power_transfer_ratio()
        graph2 = axes.plot_line_graph(
            x_values=x_pow_tran,
            y_values=y_pow_tran,
            line_color=BLUE,
            add_vertex_dots=False
        )

        self.next_slide()
        
        self.play(circuit.animate.to_edge(LEFT))
        self.play(FadeIn(axes), Write(axes_labels))
        self.play(Create(graph))
        self.play(Create(graph2))

        legend_dot1 = Dot(color=RED).scale(0.5)
        legend_label1 = Tex("Power Efficiency").scale(0.4).next_to(legend_dot1, RIGHT, buff=0.2)

        legend_dot2 = Dot(color=BLUE).scale(0.5)
        legend_label2 = Tex("Power Transfer").scale(0.4).next_to(legend_dot2, RIGHT, buff=0.2)

        legend_item1 = VGroup(legend_dot1, legend_label1)
        legend_item2 = VGroup(legend_dot2, legend_label2)

        legend = VGroup(legend_item1, legend_item2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.next_to(axes, RIGHT, buff=.5)

        self.play(FadeIn(legend))

        # === Dashed Line at R_L = R_th (max power transfer point) ===
        max_x = 1  # Replace with your actual R_th value if dynamic
        max_power_y = axes.coords_to_point(max_x, 1.0)[1]  # y-value here is 1.0 as a visual cue

        dashed_line = DashedLine(
            start=axes.c2p(max_x, 0),
            end=axes.c2p(max_x, 1),
            color=RED,
            stroke_width=2,
            dash_length=0.1
        )
        label = Tex(r"$R_L = R_{th}$").scale(0.5).next_to(dashed_line, RIGHT)

        self.play(Create(dashed_line), Write(label))

        self.next_slide()
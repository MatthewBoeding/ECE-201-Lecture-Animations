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
        self.wait()
        self.next_slide()

        # === Thevenin Equivalent Circuit ===
        v_th = Tex(r"$V_{th}$").scale(0.6)
        R_th = Rectangle(width=0.5, height=1, color=BLUE).next_to(v_th, RIGHT, buff=0.3)
        R_th_label = Tex(r"$R_{th}$").scale(0.5).next_to(R_th, DOWN, buff=0.1)

        load = Rectangle(width=0.5, height=1, color=YELLOW).next_to(R_th, RIGHT, buff=1)
        load_label = Tex(r"$R_L$").scale(0.5).next_to(load, DOWN, buff=0.1)

        wire_left = Line(LEFT * 3, v_th.get_left())
        wire_vth = Line(v_th.get_right(), R_th.get_left())
        wire_th = Line(R_th.get_right(), load.get_left())
        wire_right = Line(load.get_right(), RIGHT * 3)
        bottom_wire = Line(wire_left.get_start(), wire_right.get_end()).shift(DOWN * 1.2)

        v_th_group = VGroup(v_th, R_th, load, wire_left, wire_vth, wire_th, wire_right, bottom_wire, R_th_label, load_label).shift(DOWN)

        self.play(Create(v_th_group))
        self.wait()
        self.next_slide()

        # === Narration Text ===
        statement = Tex(
            r"The maximum power is transferred to the load when ",
            r"$R_L = R_{th}$"
        ).scale(0.7).next_to(v_th_group, UP, buff=0.8)

        self.play(Write(statement))
        self.wait()
        self.next_slide()

        # === Derivation Step ===
        deriv = Tex(r"$P = \frac{V_{th}^2 R_L}{(R_{th} + R_L)^2}$").scale(0.8).to_edge(UP)
        self.play(Write(deriv))
        self.wait()

        highlight = SurroundingRectangle(deriv[0][10:15], color=YELLOW)  # around R_L in numerator
        self.play(Create(highlight))
        self.next_slide()

        # === Power vs Load Resistance Graph ===
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.2],
            x_length=6,
            y_length=3,
            axis_config={"include_numbers": True}
        ).shift(DOWN * 1)

        axes_labels = axes.get_axis_labels(x_label="R_L", y_label="Power")

        # Example curve: P = k * R_L / (R_th + R_L)^2
        R_th_val = 5
        V_th_val = 1
        power_curve = axes.plot(
            lambda r: (V_th_val**2 * r) / ((R_th_val + r) ** 2),
            color=BLUE
        )

        self.play(Create(axes), Write(axes_labels))
        self.play(Create(power_curve))
        self.next_slide()

        # === Marking Maximum Point ===
        max_x = R_th_val
        max_y = (V_th_val**2 * R_th_val) / ((R_th_val + R_th_val)**2)
        dot = Dot(axes.c2p(max_x, max_y), color=YELLOW)
        label = Tex(r"$R_L = R_{th}$").scale(0.5).next_to(dot, UP)

        self.play(FadeIn(dot), Write(label))
        self.wait()
        self.next_slide()

        # === Final Summary ===
        box = Tex(
            r"\textbf{Maximum Power Transfer occurs when:}",
            r"$\quad R_L = R_{th}$"
        ).scale(0.8).to_edge(DOWN)

        self.play(Write(box))
        self.wait()

        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
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

        axes = Axes(
            x_range=[0, 5, .5],
            y_range=[0,1,.1],
            x_length=10,
            y_length=10,
            axis_config={"include_numbers": True},
            tips=False,
        )
        axes.scale(.4)
        #axes_labels = axes.get_axis_labels(x_label="V", y_label="I")

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

        self.play(FadeIn(circuit))
        self.next_slide()
        
        self.play(circuit.animate.to_edge(LEFT))
        self.play(FadeIn(axes))
        self.play(Create(graph))
        self.play(Create(graph2))
        self.next_slide()
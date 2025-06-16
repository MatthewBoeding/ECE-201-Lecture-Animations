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
        self.next_slide
        self.play(circuit.animate.to_edge(LEFT))
        self.play(FadeIn(axes))
        self.play(Create(graph))
        self.play(Create(graph2))
        self.next_slide()
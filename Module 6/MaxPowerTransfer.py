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
    max = (20 / 16000) * 2000
    power_max = np.linspace(max, max, 50)
    curr_power = (20 / (rl+rs)*(rl+rs)) * rl
    y_vals = curr_power / power_max
    return x_vals, y_vals

class MaxPowerTransfer(Slide):
    def construct(self):
        axes = Axes(
            x_range=[0, 5, .5],
            y_range=[0,1,.1],
            x_length=10,
            y_length=10,
            axis_config={"include_numbers": True},
            tips=False,
        )
        axes.scale(.6)
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
        self.play(FadeIn(axes))
        self.play(Create(graph))
        self.play(Create(graph2))
        self.next_slide()
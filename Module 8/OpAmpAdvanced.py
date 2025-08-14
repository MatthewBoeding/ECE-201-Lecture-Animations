from manim import *
from manim_circuit import VoltageSource, Resistor
from manim_slides import Slide

class OpAmpAdvanced(Slide):
    def construct(self):
        # === Voltage Input ===
        vin = VoltageSource(direction=DOWN).shift(LEFT * 5 + UP * 1)
        vin.remove(vin.label)
        vinlab = Tex(r"$V_{in}$").scale(0.75).next_to(vin, DOWN, buff=0.2)

        # === Op-Amp ===
        op_amp = Polygon(
            ORIGIN,
            RIGHT * 2 + UP,
            RIGHT * 2 + DOWN,
            ORIGIN,
            color=WHITE
        ).shift(RIGHT * 1)

        plus = Tex("+").scale(0.5).next_to(op_amp, LEFT).shift(UP * 0.4 + LEFT * 0.1)
        minus = Tex("–").scale(0.5).next_to(op_amp, LEFT).shift(DOWN * 0.4 + LEFT * 0.1)

        # === Resistors ===
        rf = Resistor(direction=DOWN).shift(RIGHT * 3 + UP * 1)
        rf.remove(rf.label)
        rflab = Tex(r"$R_f$").scale(0.75).next_to(rf, RIGHT, buff=0.1)

        r1 = Resistor(direction=DOWN).shift(RIGHT * 3 + DOWN * 0.5)
        r1.remove(r1.label)
        r1lab = Tex(r"$R_1$").scale(0.75).next_to(r1, RIGHT, buff=0.1)

        # === Output Voltage ===
        vout = VoltageSource(direction=RIGHT).shift(RIGHT * 5)
        vout.remove(vout.label)
        voutlab = Tex(r"$V_{out}$").scale(0.75).next_to(vout, RIGHT, buff=0.2)

        # === Wiring ===
        # Vin to + input
        wire_vin_to_plus = Line(vin.get_right(), op_amp.get_left() + UP * 0.4)

        # Ground Vin
        ground_vin_line = Line(vin.get_bottom(), vin.get_bottom() + DOWN * 0.5)
        ground_vin_symbol = Line(
            vin.get_bottom() + DOWN * 0.5,
            vin.get_bottom() + DOWN * 0.6
        )

        # Op-Amp output to Vout
        wire_opamp_out = Line(op_amp.get_right(), vout.get_left())

        # Feedback loop: Vout → Rf → R1 → – input
        wire_vout_to_rf = Line(vout.get_left(), rf.get_top())
        wire_rf_to_r1 = Line(rf.get_bottom(), r1.get_top())
        wire_r1_to_minus = Line(r1.get_bottom(), op_amp.get_left() + DOWN * 0.4)

        # Ground R1 bottom
        ground_r1_line = Line(r1.get_bottom(), r1.get_bottom() + DOWN * 0.5)
        ground_r1_symbol = Line(
            r1.get_bottom() + DOWN * 0.5,
            r1.get_bottom() + DOWN * 0.6
        )

        # === Draw Circuit ===
        self.play(Create(vin), Create(vinlab))
        self.play(Create(wire_vin_to_plus), Create(ground_vin_line), Create(ground_vin_symbol))
        self.play(Create(op_amp), Write(plus), Write(minus))
        self.play(Create(rf), Create(rflab), Create(r1), Create(r1lab))
        self.play(Create(wire_opamp_out), Create(vout), Create(voutlab))
        self.play(Create(wire_vout_to_rf), Create(wire_rf_to_r1), Create(wire_r1_to_minus))
        self.play(Create(ground_r1_line), Create(ground_r1_symbol))

        self.wait(2)
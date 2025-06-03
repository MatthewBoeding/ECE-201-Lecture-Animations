from manim import *
from manim_slides import Slide
from manim_circuit import *


class DeltaWyeExample(Slide):
    def construct(self):
        # It is helpful to use a Numberplane() to help move the parts and place them appropriately.
        n = NumberPlane().set_opacity(0.5)
        self.add(n)
        title = Text(r"What is the equivalent total current supplied by the Voltage Source?").scale(.5).to_edge(UP)
        self.add(title)
        # Place the components down first. Then, connect with wires later.
        r270 = Resistor(270).shift(LEFT * 3.5 + UP*3)
        r4k1 = (
            Resistor("4k", direction=RIGHT)
            .rotate(90 * DEGREES)
            .shift(LEFT * 1.75 + UP * 2)
        )
        r1100 = Resistor("1.1k", direction=DOWN).shift(DOWN * 2 + LEFT * 0.25)
        r4k2 = (
            Resistor("4k", direction=RIGHT)
            .rotate(90 * DEGREES)
            .shift(RIGHT * 1.25 + UP * 2)
        )
        r2k = Resistor("2k", direction=DOWN).shift(UP*.5)
        r10k = Resistor("10k", direction=RIGHT).rotate(90 * DEGREES).shift(LEFT*1.75 + DOWN *.5)
        r6202 = (
            Resistor(620, direction=RIGHT)
            .rotate(90 * DEGREES)
            .shift(RIGHT * 1.25 + DOWN *.5)
        )
        v20 = VoltageSource(20).shift(LEFT * 5+UP*.5)

        gnd = Ground(ground_type="ground").shift(LEFT * 5 + DOWN * 3)

        # Add Circuit components.
        circuit = Circuit()
        circuit.add_components(r270, r4k1, r1100, r4k2, r2k, r10k, r6202, v20, gnd)

        # A much streamline and easier way to edit.
        circuit.add_wire(gnd.get_terminals(), v20.get_terminals("negative"))
        circuit.add_wire(v20.get_terminals("negative"), r1100.get_terminals("left"))
        circuit.add_wire(r10k.get_terminals("left"), r1100.get_terminals("left"))
        circuit.add_wire(v20.get_terminals("positive"), r270.get_terminals("left"))
        circuit.add_wire(r270.get_terminals("right"), r4k2.get_terminals("right"), invert = True)
        circuit.add_wire(r270.get_terminals("right"), r4k1.get_terminals("right"), invert = True)
        circuit.add_wire(r4k1.get_terminals("left"), r10k.get_terminals("right"))
        circuit.add_wire(r6202.get_terminals("right"), r4k2.get_terminals("left"))
        circuit.add_wire(r6202.get_terminals("right"), r2k.get_terminals("right"))
        circuit.add_wire(r10k.get_terminals("right"), r2k.get_terminals("left"))
        circuit.add_wire(r6202.get_terminals("left"), r1100.get_terminals("right"))


        circuit.scale(.8)
        self.add(circuit)
        self.wait()

        self.wait()
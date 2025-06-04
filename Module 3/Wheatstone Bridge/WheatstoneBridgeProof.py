from manim import *
from manim_slides import Slide
from manim_circuit import *

class Resistor(VMobject):
    def __init__(self, label=None, direction=DOWN, **kwargs):
        # initialize the vmobject
        super().__init__(**kwargs)
        self._direction = direction
 
        # Less points, more cleaner!
        self.main_body = VMobject()
        points = [
            [-2.5, 0, 0],
            [-2.2438, 0, 0],
            [-1.39324, 0, 0],
            [-0.54268, 1, 0],
            [0.30788, -1, 0],
            [1.15843, 1, 0],
            [2.00899, -1, 0],
            [2.85954, 1, 0],
            [3.7101, -1, 0],
            [4.13537, 0, 0],
            [4.98593, 0, 0]
        ]
        self.main_body.start_new_path(points[0])
        for i in points[1:]:
            self.main_body.add_line_to(np.array(i))
        self.main_body.scale(0.25).center()
 
        self.add(self.main_body)
 
        # check if lebel is present.
        if not label is None:
            self.label = (
                Tex(str(label))
                .scale(0.5)
                .next_to(self.main_body, self._direction, buff=0.1)
            )
            self.add(self.label)
        else:
            self.label = None
 
    def get_anchors(self):
        return [self.main_body.get_start(), self.main_body.get_end()]
 
    def get_terminals(self, val):
        if val == "left":
            return self.main_body.get_start()
        elif val == "right":
            return self.main_body.get_end()
 
    def center(self):
        self.shift(
            DOWN * self.main_body.get_center()[1] + LEFT * self.main_body.get_center()
        )
 
        return self
 
    def rotate(self, angle, *args, **kwargs):
        super().rotate(angle, about_point=self.main_body.get_center(), *args, **kwargs)
        if not self.label == None:
            self.label.rotate(-angle).next_to(self.main_body, self._direction, buff=0.1)
 
        return self

class WheatstoneProof(Slide):
    def construct(self):
        bridge = VGroup()
        #Top Terminals are "right"
        r1 = Resistor("$R_1$", direction=UP).rotate(45 * DEGREES).shift(LEFT * .75 + UP * .75)
        r2 = Resistor("$R_2$", direction=UP).rotate(135 * DEGREES).shift(UP * .75 + RIGHT * .75)
        r3 = Resistor("$R_3$", direction=DOWN).rotate(135 * DEGREES).shift(LEFT * .75 + DOWN*.75)
        r4 = Resistor("$R_4$", direction=DOWN).rotate(45 * DEGREES).shift(DOWN * .75 + RIGHT * .75)
        vo = VoltageSource(value= " ").shift(LEFT * 3)
        circuit = Circuit().add(r1,r2,r3,r4,vo)
        circuit.add_wire(vo.get_terminals("positive"),r1.get_terminals("right"))
        circuit.add_wire(r1.get_terminals("right"),r2.get_terminals("right"), invert = True)
        circuit.add_wire(r1.get_terminals("left"), r3.get_terminals("right"), invert = True)
        circuit.add_wire(r2.get_terminals("left"), r4.get_terminals("right"), invert = True)
        circuit.add_wire(r4.get_terminals("left"), vo.get_terminals("negative"), invert = True)
        circuit.add_wire(r4.get_terminals("left"), vo.get_terminals("negative"), invert = True)
        self.add(circuit)
        self.next_slide()
        self.wait()
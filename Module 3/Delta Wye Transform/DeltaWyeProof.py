from manim import *
from manim_slides import Slide
from manim_circuit import *
 
delta_map = {
    "node1": 0,
    "node2": 1,
    "node3": 2,
    "right1": 3,
    "right2": 4,
    "top1": 5,
    "top2": 6,
    "left1": 7,
    "left2": 8,
    "circuit": 9,
    "n1": 10,
    "n2": 11,
    "n3": 12,
    "ral": 13,
    "rbl": 14,
    "rcl": 15,
}
 
wye_map = {
    "r1": 0,
    "r2": 1,
    "r3": 2,
    "node1": 3,
    "node2": 4,
    "node3": 5,
    "line1": 6,
    "line2": 7,
    "r1l": 8,
    "r2l": 9,
    "r3l": 10,
    "n1": 11,
    "n2": 12,
    "n3": 13
}
 
 
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
def WyeCreate():
    wye = VGroup()
    r1 = Resistor("", direction=UP).rotate(270*DEGREES).shift(UP*3.5)
    r2 = (
            Resistor("", direction=UP)
            .rotate(45 * DEGREES)
            .shift(LEFT * 1 + UP * 1.5)
        )
    r3 = Resistor("", direction=UP).rotate(135 * DEGREES).shift(UP * 1.5 + RIGHT * 1)
    node1 = Dot(point=r1.get_terminals("left"))
    n1 = MathTex(r"n_1")
    n1.next_to(node1, UP, buff=0.2)
    node2 = Dot(point=r2.get_terminals("left"))
    n2 = MathTex(r"n_2")
    n2.next_to(node2, LEFT, buff=0.2)
    node3 = Dot(point=r3.get_terminals("left"))
    n3 = MathTex(r"n_3")
    n3.next_to(node3, RIGHT, buff=0.2)
    line1 = Line(start=r1.get_terminals("right"), end = r2.get_terminals("right"))
    line2 = Line(start=r1.get_terminals("right"), end = r3.get_terminals("right"))
    r1l = MathTex(r"R_1")
    r1l.next_to(r1, LEFT, buff=0.2)
    r2l = MathTex(r"R_2")
    r2l.next_to(r2, LEFT, buff=0.2)
    r3l = MathTex(r"R_3")
    r3l.next_to(r3, RIGHT, buff=0.2)
    wye.add(r1,r2,r3,node1,node2,node3, line1, line2, r1l,r2l,r3l, n1,n2,n3)
 
    return wye
 
def DeltaCreate():
    delta = VGroup()
    ra = (
            Resistor("", direction=UP)
            .rotate(45 * DEGREES)
            .shift(LEFT * 2 + UP * 2)
        )
    rb = Resistor("", direction=UP).rotate(135 * DEGREES).shift(UP * 2 + RIGHT * 2)
    rc = (
        Resistor("", direction=UP)
    )
 
    # Add Circuit components.
    circuit = Circuit()
    circuit.add_components(ra,rb,rc)
 
    # A much streamline and easier way to edit.
 
    # The order in which the wires are added matters.
 
    ra_right = ra.get_terminals("right")
    rb_right = rb.get_terminals("right")
    rc_right = rc.get_terminals("right")
 
    ra_left = ra.get_terminals("left")
    rb_left = rb.get_terminals("left")
    rc_left = rc.get_terminals("left")
 
    top1 = Line(start = ra_right, end=[0,4,0])
    top2 = Line(start = rb_right, end=[0,4,0])
    right1 = Line(start = rc_right, end = [4,0,0])
    right2 = Line(start = rb_left, end = [4,0,0])
    left1 = Line(start = rc_left, end = [-4,0,0])
    left2 = Line(start = ra_left, end = [-4,0,0])
    node3 = Dot(point = [4,0,0])
    n3 = MathTex(r"n_3")
    n3.next_to(node3, RIGHT, buff=0.2)
    node2 = Dot(point = [-4,0,0])
    n2 = MathTex(r"n_2")
    n2.next_to(node2, LEFT, buff=0.2)
    node1 = Dot(point = [0,4,0])
    n1 = MathTex(r"n_1")
    n1.next_to(node1, UP, buff=0.2)
    ral = MathTex(r"R_a")
    ral.next_to(ra, LEFT, buff=0.2)
    rbl = MathTex(r"R_b")
    rbl.next_to(rb, RIGHT, buff=0.2)
    rcl = MathTex(r"R_c")
    rcl.next_to(rc, DOWN, buff=0.2)
    delta.add(node1) #index 0
    delta.add(node2) #index 1
    delta.add(node3) #index 2
    delta.add(right1) #index 3
    delta.add(right2) #index 4
    delta.add(top1) #index 5
    delta.add(top2) #index 6
    delta.add(left1) #index 7
    delta.add(left2) #index 8
    delta.add(circuit) #index 9
    delta.add(n1) #index 10
    delta.add(n2) #index 11
    delta.add(n3) #index 12
    delta.add(ral, rbl, rcl) #index 13, 14, 15
    return delta
 
class DeltaWyeProof(Slide):
    def construct(self):
 
        # It is helpful to use a Numberplane() to help move the parts and place them appropriately.
        n = NumberPlane(y_range=(-4,4.0,1)).set_opacity(0.25)
        self.add(n)
        self.wait()
        title = Text(r"Delta-Wye Transform", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.next_slide()
 
 
        delta = DeltaCreate()
        # Place the components down first. Then, connect with wires later.
        delta.shift(DOWN *2)
        wye= WyeCreate()
        wye.shift(DOWN*3+RIGHT*1)

        self.play(FadeIn(delta))
        self.wait()
 
        self.next_slide()
 
        transform = Arrow(buff=2.2, start = 1.2*LEFT, end = 2*RIGHT, color = RED)
        self.play(delta.animate.scale(.65))
        self.play(delta.animate.shift(LEFT*4))
        wye.scale(.65)
        wye.shift(RIGHT*3)
        self.play(FadeIn(wye))
        self.play(Create(transform))
        self.next_slide()
 
 
        self.play(Uncreate(transform))
        delta[delta_map["node1"]].set_color(YELLOW)
        delta[delta_map["node3"]].set_color(YELLOW)
        delta[delta_map["n3"]].shift(UP*.2)
        line1 = Line(start=delta[delta_map["node1"]].get_center(), end=delta[delta_map["node1"]].get_center()+[3.5,0,0])
        line2 = Line(start=delta[delta_map["node3"]].get_center(), end=delta[delta_map["node3"]].get_center()+[1,0,0])
        r13 = MathTex(r"\leftarrow R_{n_1n_3}")
        r13.shift(LEFT*.5)
        r13.scale(.8)
        self.play(Create(r13))
        self.play(Create(line1))
        self.play(Create(line2))
        self.next_slide()
 
 
        wye[wye_map["n3"]].shift(UP*.2)
        wye[wye_map["node3"]].set_color(YELLOW)
        wye[wye_map["node1"]].set_color(YELLOW)
        line3 = Line(start=wye[wye_map["node1"]].get_center(), end=wye[wye_map["node1"]].get_center()+[2,0,0])
        line4 = Line(start=wye[wye_map["node3"]].get_center(), end=wye[wye_map["node3"]].get_center()+[1,0,0])
        self.play(Create(line3))
        self.play(Create(line4))
        r13dup = MathTex(r"\leftarrow R_{n_1n_3}")
        r13dup.next_to(line3, DOWN, buff=.2)
        r13dup.scale(.8)
        r13dup.shift(RIGHT*1,DOWN*.5)
        self.play(Create(r13dup))
        self.next_slide()
 
 
        self.remove(r13dup, line1, line2, line3, line4, r13)
        self.play(FadeOut(wye))
        self.play(delta.animate.shift(RIGHT*6))
        self.play(delta.animate.scale(1.54))
        self.next_slide()
 
 
        equ = MathTex(r"R_{n_1n_3} = R_b || (R_a + R_c)").to_corner(UL)
        self.play(Uncreate(title))
        self.play(Write(equ))
        self.wait()
        self.next_slide()
 
 
        equ1 = MathTex(r"R_{n_1n_3}= \frac{R_b(R_a+R_c)}{R_a+R_b+R_c}").to_corner(UL).shift(DOWN*1)
        self.play(Write(equ1))
        self.wait()
        self.next_slide()
        self.play(Uncreate(equ))
        self.play(equ1.animate.scale(.5))
        self.play(equ1.animate.to_corner(UL))
        delta[delta_map["node3"]].set_color(WHITE)
        delta[delta_map["node2"]].set_color(YELLOW)
        self.play(delta[delta_map["node2"]].animate.scale(2))
        self.play(delta[delta_map["node1"]].animate.scale(2))
        equ= MathTex(r"R_{n_1n_2} = R_a || (R_b + R_c)").to_corner(UL).shift(DOWN*1)
        self.play(Write(equ))
        self.next_slide()
        equ2= MathTex(r"R_{n_1n_2} = \frac{R_a(R_b + R_c)}{R_a+R_b+R_c}").next_to(equ, DOWN, buff=.2)
        self.play(Write(equ2))
 
        self.next_slide()
 
        self.play(Uncreate(equ))
        self.play(equ2.animate.scale(.5))
        self.play(equ2.animate.next_to(equ1, DOWN, buff=.2))
        delta[delta_map["node1"]].set_color(WHITE).scale(.5)
        delta[delta_map["node2"]].set_color(YELLOW).scale(.5)
        delta[delta_map["node3"]].set_color(YELLOW)
        self.play(delta[delta_map["node2"]].animate.scale(2))
        self.play(delta[delta_map["node3"]].animate.scale(2))
        equ= MathTex(r"R_{n_2n_3} = R_c || (R_a + R_b)").next_to(equ2, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(equ))
        self.next_slide()
        equ3= MathTex(r"R_{n_2n_3} = \frac{R_c(R_a + R_b)}{R_a+R_b+R_c}").next_to(equ, DOWN, buff=.2)
        self.play(Write(equ3))
 
        self.next_slide()
 
        self.play(Uncreate(equ))
        self.play(equ3.animate.scale(.5))
        self.play(equ3.animate.next_to(equ2, DOWN, buff=.2))
        delta[delta_map["node3"]].set_color(WHITE).scale(.5)
        delta[delta_map["node2"]].set_color(WHITE).scale(.5)
 
        self.next_slide()
 
        self.play(FadeOut(delta))
        wye= WyeCreate()
        wye.shift(DOWN*3+RIGHT*1)
        self.play(FadeIn(wye))
        self.play(wye.animate.scale(1.3))
 
        self.play(FadeOut(wye[wye_map["r2"]]))
        equ = MathTex(r"R_{n_1n_3} = R_1+R_3").to_corner(UL).shift(DOWN*4)
 
        self.play(Create(equ))
        self.next_slide()
        self.add(wye[wye_map["r2"]])
        self.play(equ.animate.scale(.5))
        self.play(equ.animate.next_to(equ3, DOWN, buff=.2))
        self.wait()
        self.play(FadeOut(wye[wye_map["r3"]]))
        equ4 = MathTex(r"R_{n_1n_2} = R_1+R_2").to_corner(UL).shift(DOWN*5)
        self.play(Create(equ4))
        
        self.next_slide()
 
        self.add(wye[wye_map["r3"]])
        self.play(equ4.animate.scale(.5))
        self.play(equ4.animate.next_to(equ, DOWN, buff=.2))
        self.wait()
        self.play(FadeOut(wye[wye_map["r1"]]))
        equ5 = MathTex(r"R_{n_2n_3} = R_2+R_3").to_corner(UL).shift(DOWN*6)
        self.play(Create(equ5))

        self.next_slide()

        self.add(wye[wye_map["r1"]])
        self.play(equ5.animate.scale(.5))
        self.play(equ5.animate.next_to(equ4, DOWN, buff=.2))
        wyeEqu = VGroup()
        deltaEqu = VGroup()
        wyeEqu.add(equ, equ4, equ5)
        deltaEqu.add(equ1, equ2, equ3)

        self.next_slide()

        self.play(FadeOut(wye))
        self.play(wyeEqu.animate.scale(1.5))
        self.play(wyeEqu.animate.to_corner(UR))
        self.play(deltaEqu.animate.scale(1.5))
        self.play(deltaEqu.animate.to_corner(UL))
        equ6 = MathTex(r"Eq. 1: R_1+R_2 = \frac{R_a(R_b + R_c)}{R_a+R_b+R_c}").to_corner(DR).shift(UP*3)
        equ7 = MathTex(r"Eq. 2: R_1+R_3 = \frac{R_b(R_a + R_c)}{R_a+R_b+R_c}").to_corner(DR).shift(UP*1.5)
        equ8 = MathTex(r"Eq. 3: R_2+R_3 = \frac{R_c(R_a + R_b)}{R_a+R_b+R_c}").to_corner(DR)

        self.next_slide()

        self.play(equ1.animate.set_color(RED))
        self.play(equ.animate.set_color(RED))
        self.play(Write(equ6))
        self.play(FadeOut(equ1))
        self.play(FadeOut(equ))

        self.next_slide()

        self.play(equ2.animate.set_color(RED))
        self.play(equ4.animate.set_color(RED))
        self.play(Write(equ7))
        self.play(FadeOut(equ2))
        self.play(FadeOut(equ4))
        
        self.next_slide()

        self.play(equ3.animate.set_color(RED))
        self.play(equ5.animate.set_color(RED))
        self.play(Write(equ8))
        self.play(FadeOut(equ3))
        self.play(FadeOut(equ5))
        
        self.next_slide()

        moreEqus = VGroup()
        moreEqus.add(equ6,equ7,equ8)
        self.play(moreEqus.animate.scale(.5))
        self.play(moreEqus.animate.to_edge(RIGHT))
        title = Text(r"Solving for Individual Resistors").to_edge(UP)
        
        self.next_slide()

        self.play(Write(title))
        instructions = Text(r"Eq. 1 + Eq. 2 - Eq. 3").scale(.75).next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(instructions))
        solve = MathTex(r"(R_1+R_2) + (R_1 + R_3) - (R_2 + R_3) = 2R_1").scale(.6).next_to(instructions, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(solve))
        solve2 = MathTex(r"R_1 = \frac{R_aR_b}{R_a+R_b+R_c}").scale(.75).next_to(solve, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(solve2))

        self.next_slide()

        instr2 = Text(r"Eq. 1 + Eq. 3 - Eq. 2").scale(.75).next_to(solve2, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(instr2))
        solv1 = MathTex(r"(R_1+R_2) + (R_2 + R_3) - (R_1 + R_3) = 2R_2").scale(.6).next_to(instr2, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(solv1))
        solv2 = MathTex(r"R_2 = \frac{R_aR_c}{R_a+R_b+R_c}").scale(.75).next_to(solv1, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(solv2))

        self.next_slide()

        instr3 = Text(r"Eq. 2 + Eq. 3 - Eq. 1").scale(.75).next_to(title, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(instr3))
        solv3 = MathTex(r"(R_1+R_3) + (R_2 + R_3) - (R_1 + R_2) = 2R_3").scale(.6).next_to(instr3, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(solv3))
        solv4 = MathTex(r"R_3 = \frac{R_bR_c}{R_a+R_b+R_c}").scale(.75).next_to(solv3, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(solv4))

        self.next_slide()

        fadeout = VGroup()
        fadeout.add(title, instructions, instr2, instr3, solv1, solv3, solve)
        self.play(FadeOut(fadeout))
        instructions = MathTex(r"\Delta \rightarrow Y").to_edge(UP)
        self.play(Write(instructions))
        self.play(solve2.animate.next_to(instructions, DOWN, buff=.2))
        self.play(solve2.animate.to_edge(LEFT))
        self.play(solv2.animate.next_to(instructions, DOWN, buff=.2))
        self.play(solv4.animate.next_to(solv2, RIGHT, buff=1))
        
        self.next_slide()

        self.play(FadeOut(moreEqus))
        wyedelta = MathTex(r"Y \rightarrow \Delta").next_to(solv2, DOWN, buff=.2)
        self.play(FadeIn(wyedelta))
        wd1 = MathTex(r"1) R_1R_2 = \frac{R_a^2R_bR_c}{(R_a+R_b+R_c)^2}").scale(.6).next_to(wyedelta, DOWN, buff=.2).to_edge(LEFT)
        wd2 = MathTex(r"2) R_1R_3 = \frac{R_aR_b^2R_c}{(R_a+R_b+R_c)^2}").scale(.6).next_to(wd1, DOWN, buff=.2)
        wd3 = MathTex(r"3) R_2R_3 = \frac{R_aR_bR_c^2}{(R_a+R_b+R_c)^2}").scale(.6).next_to(wd2, DOWN, buff=.2)
        self.play(Write(wd1))
        self.play(Write(wd2))
        self.play(Write(wd3))
        
        self.next_slide()

        wd4 = MathTex(r"1)+2)+3) = R_1R_2+R_1R_3+R_2R_3 = \frac{R_a^2R_bR_c+R_aR_b^2R_c+R_aR_bR_c^2}{(R_a+R_b+R_c)^2}").scale(.6).next_to(wd1, RIGHT, buff=.5)
        self.play(Write(wd4))
        
        self.next_slide()
        
        wd5 = MathTex(r"R_1R_2+R_1R_3+R_2R_3 = \frac{R_aR_bR_c(R_a+R_b+R_c)}{(R_a+R_b+R_c)^2} = \frac{R_aR_bR_c}{R_a+R_b+R_c}").scale(.6).next_to(wd4, DOWN, buff=.5)
        self.play(Write(wd5))
        
        self.next_slide()
        wd6 = MathTex(r"R_1R_2+R_1R_3+R_2R_3 = R_a\frac{R_bR_c}{R_a+R_b+R_c} = R_aR_3").scale(.6).next_to(wd5, DOWN, buff=.5)
        self.play(Write(wd6))
        
        self.next_slide()
        wd7 = MathTex(r"Ra = \frac{R_1R_2+R_1R_3+R_2R_3}{R_3}").scale(.6).next_to(wd6, DOWN, buff=.5)
        self.play(Write(wd7))

        self.next_slide()
        
        fadeout = VGroup()
        fadeout.add(wd1, wd2, wd3, wd4, wd5, wd6)
        self.play(FadeOut(fadeout))
        wd5 = MathTex(r"R_1R_2+R_1R_3+R_2R_3 = \frac{R_aR_bR_c}{R_a+R_b+R_c}").scale(.6).next_to(wyedelta, DOWN, buff=.2).to_edge(LEFT)
        self.play(FadeIn(wd5))
        self.play(wd7.animate.next_to(wd5, RIGHT, buff=.2))
        wd8 = MathTex(r"R_1R_2+R_1R_3+R_2R_3 = R_b\frac{R_aR_c}{R_a+R_b+R_c} = R_bR_2").scale(.6).next_to(wd5, DOWN, buff=.5).to_edge(LEFT)
        wd9 = MathTex(r"R_b = \frac{R_1R_2+R_1R_3+R_2R_3}{R_2}").scale(.6).next_to(wd8, RIGHT, buff=.5)
        wd10 = MathTex(r"R_1R_2+R_1R_3+R_2R_3 = R_c\frac{R_aR_b}{R_a+R_b+R_c} = R_cR_1").scale(.6).next_to(wd8, DOWN, buff=.5).to_edge(LEFT)
        wd11 = MathTex(r"R_c = \frac{R_1R_2+R_1R_3+R_2R_3}{R_1}").scale(.6).next_to(wd10, RIGHT, buff=.5)
        self.play(Write(wd8))
        self.play(Write(wd9))
        
        self.next_slide()

        self.play(Write(wd10))
        self.play(Write(wd11))


        self.next_slide()

        fadeout = VGroup()
        fadeout.add(wd5, wd8, wd10)
        self.play(FadeOut(fadeout))
        self.play(wd7.animate.to_edge(LEFT))
        self.play(wd9.animate.next_to(wd7, RIGHT, buff=.5))
        self.play(wd11.animate.next_to(wd9, RIGHT, buff=.5))
        delta = DeltaCreate().scale(.5).to_corner(DL).shift(UP*1)
        wye= WyeCreate().scale(.6).to_corner(DR).shift(UP*1)
        fadein = VGroup().add(delta,wye)
        self.play(FadeIn(fadein))
        # keep 7 9 and 11
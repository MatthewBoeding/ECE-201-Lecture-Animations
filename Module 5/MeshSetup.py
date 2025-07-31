from manim import *
from manim_circuit import *
from manim_slides import Slide

def MeshLoop(source : list, dir="RIGHT"):
    offset1 = [1,0,0]
    offset2 = [1.4,0,0]
    offset3 = [1,0,0]
    if dir == "LEFT":
        offset1 = [-num for num in offset1]
        offset2 = [-num for num in offset2]
        offset3 = [-num for num in offset3]
    start = source+offset1
    end = source+offset2
    radius = .35

    arc = Arc(
        radius=radius,
        start_angle=PI,    # start from LEFT
        angle=-3*PI/2,          # go to RIGHT
        color=WHITE,
        stroke_width=4
    )
    arc.move_arc_center_to(ORIGIN)

    # Arrow tip: small triangle
    tip = Polygon(
        ORIGIN, 0.2*LEFT + 0.1*DOWN, 0.2*LEFT + 0.1*UP,
        color=WHITE, fill_opacity=1
    )

    # Position tip at end of arc
    end_point = arc.point_from_proportion(1)
    direction = arc.point_from_proportion(1) - arc.point_from_proportion(0.99)
    angle = angle_of_vector(direction)

    tip.rotate(angle)
    tip.move_to(end_point)

    # Group the arc and the arrow tip
    arrow = VGroup(arc, tip).move_to(source+offset3)
    return arrow
    

class MeshSetup(Slide):
    def construct(self):
        io = CurrentSource("2m", dependent=False)
        r1 = Resistor("3k", UP).shift(UP*1+RIGHT*1.5)
        vs = VoltageSource("3", dependent=False).next_to(r1, DOWN, buff=.2).shift(RIGHT*1.5+DOWN*.3)
        vs.remove(vs.label)
        vslab = Tex("$3$V").scale(.6).next_to(vs, RIGHT, buff=.2)
        r2 = Resistor("6k", RIGHT).rotate(DEGREES*-90).next_to(vs, DOWN, buff=.5)
        r2.shift(RIGHT*.3)
        r3 = Resistor("3k", RIGHT).rotate(DEGREES*-90).next_to(r2, RIGHT, buff=.5).shift(UP*1+RIGHT*1)

        circuit = Circuit().add(io, r1, r2, r3, vs, vslab)
        circuit.add_wire(io.get_terminals("positive"), r1.get_terminals("left"))
        circuit.add_wire(r1.get_terminals("right"), vs.get_terminals("positive"), invert = True)
        
        circuit.add_wire(r2.get_terminals("right"), io.get_terminals("negative"), invert = True)
        circuit.add_wire(r1.get_terminals("right"), r3.get_terminals("left"), invert = True)
        circuit.add_wire(r3.get_terminals("right"), r2.get_terminals("right"))
        r2.shift(UP*.25)
        circuit.add_wire(vs.get_terminals("negative"), r2.get_terminals("left"), invert = True)
        circuit.add_wire(r2.get_terminals("right"), r2.get_terminals("right")+[0,-.25,0])
        title = Tex("Mesh Analysis").to_edge(UP)
        self.add(title)
        step1 = Tex(r"$\bullet$ Identify all independent loops (N)").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        step2 =  Tex(r"$\bullet$ Count Current Sources (M)").next_to(step1, DOWN, buff=.2).to_edge(LEFT)
        step3 = Tex(r"$\bullet$ Complexity C = N-M").next_to(step2, DOWN, buff=.2).to_edge(LEFT)
        step4 = Tex(r"$\bullet$ Solve C simulatneous equations").next_to(step3, DOWN, buff=.2).to_edge(LEFT)
        self.next_slide()
        self.play(Write(step1))
        self.play(Write(step2))
        self.play(Write(step3))
        self.play(Write(step4))
        self.next_slide()
        self.play(FadeOut(step2), FadeOut(step3), FadeOut(step4))
        self.play(Create(circuit))
        self.next_slide()
        mesh1 = MeshLoop(source = io.get_terminals("negative"))
        i1 = Tex("$I_1$").scale(.5).move_to(mesh1.get_center())
        mesh2 = MeshLoop(source = r3.get_terminals("right"), dir="LEFT")
        i2 = Tex("$I_2$").scale(.5).move_to(mesh2.get_center())
        self.play(Create(mesh1), Create(mesh2))
        self.play(Write(i1), Write(i2))
        self.next_slide()

        step2.next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(Transform(step1, step2))
        circ = Circle(radius=.5).move_to(io.get_center())
        self.play(Create(circ))

        self.next_slide()
        step3.next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(Transform(step1, step3))
        eq = Tex(r"$C = N-M = 2-1 = 1$").next_to(step1, DOWN, buff=.2)
        self.play(Write(eq))

        self.next_slide()

        eq2 = Tex(r"$C=1$").next_to(step1, DOWN, buff=.2)
        self.play(Transform(eq, eq2))
        eq3 = Tex(r"$I_1 = 2mA$").scale(.75).next_to(eq2, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(eq3), FadeOut(circ))

        self.next_slide()

        eq4 = Tex(r"$3kI_2 + 6k (I_2 - I_1) - 3V = 0$").scale(.75).next_to(eq3, DOWN, buff=.2).to_edge(LEFT)
        eq5 = Tex(r"$-6kI_1 + 9kI_2 = 3V$").scale(.75).next_to(eq4, DOWN, buff=.2).to_edge(LEFT)
        eq6 = Tex(r"$9kI_2 = 15V$").scale(.75).next_to(eq5, DOWN, buff=.2).to_edge(LEFT)
        eq7 = Tex(r"$I_2 = \frac{5}{3}mA$").scale(.75).next_to(eq6, DOWN, buff=.2).to_edge(LEFT)
        eq8 = Tex(r"$I_1-I_2 = 2mA - \frac{5}{3}mA = \frac{1}{3}mA$").scale(.75).next_to(eq6, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(eq4))
        self.wait()
        self.play(Write(eq5))
        self.wait()
        self.play(Write(eq6))
        self.wait()
        self.play(Write(eq7))
        self.wait()
        self.play(Write(eq8))
        self.wait()
        self.next_slide()

        
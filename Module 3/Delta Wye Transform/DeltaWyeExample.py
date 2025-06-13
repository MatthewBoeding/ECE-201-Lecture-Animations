from manim import *
from manim_slides import Slide
from manim_circuit import *

def WyeCreate():
    wye = VGroup()
    r1 = Resistor("1.6k", direction=UP).rotate(270*DEGREES).shift(UP*3.5)
    r2 = (
            Resistor("800", direction=UP)
            .rotate(45 * DEGREES)
            .shift(LEFT * 1 + UP * 1.5)
        )
    r3 = Resistor("800", direction=UP).rotate(135 * DEGREES).shift(UP * 1.5 + RIGHT * 1)
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
    
    wye.add(r1,r2,r3,node1,node2,node3, line1, line2, n1,n2,n3)
 
    return wye

def DeltaCreate():
    delta = VGroup()
    ra = (
            Resistor("4k", direction=UP)
            .rotate(45 * DEGREES)
            .shift(LEFT * 2 + UP * 2)
        )
    rb = Resistor("4k", direction=UP).rotate(135 * DEGREES).shift(UP * 2 + RIGHT * 2)
    rc = (
        Resistor("2k", direction=UP)
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
    return delta

class DeltaWyeExample(Slide):
    def construct(self):
        '''
        SLIDE 1
        '''
        # It is helpful to use a Numberplane() to help move the parts and place them appropriately.
        n = NumberPlane().set_opacity(0.5)
        #self.add(n)
        title = Text(r"What is the equivalent total current supplied by the Voltage Source?").scale(.5).to_edge(UP)
        self.add(title)
        # Place the components down first. Then, connect with wires later.
        
        r270 = Resistor(270).shift(LEFT * 3.5 + UP*3.5)
        r4k1 = (
            Resistor("4k", direction=RIGHT)
            .rotate(90 * DEGREES)
            .shift(LEFT * 1.75 + UP * 2)
        )
        r1100 = Resistor("3.3k", direction=DOWN).shift(DOWN * 2 + LEFT * 0.25)
        r4k2 = (
            Resistor("4k", direction=RIGHT)
            .rotate(90 * DEGREES)
            .shift(RIGHT * 1.25 + UP * 2)
        )
        r2k = Resistor("2k", direction=DOWN).shift(UP*.5)
        r10k = Resistor("4.2k", direction=RIGHT).rotate(90 * DEGREES).shift(LEFT*1.75 + DOWN *.5)
        r6202 = (
            Resistor(900, direction=RIGHT)
            .rotate(90 * DEGREES)
            .shift(RIGHT * 1.25 + DOWN *.5)
        )
        v20 = VoltageSource(20).shift(LEFT * 5+UP*.5)

        gnd = Ground(ground_type="ground").shift(LEFT * 5 + DOWN * 3)

        # Add Circuit components.
        circuit = Circuit()
        circuit.add_components(r270, r4k1, r4k2, r2k, r1100, r10k, r6202, v20, gnd)

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

        circuit.scale(.8).shift(DOWN*1)
        self.add(circuit)
        self.wait()

        '''
        SLIDE 2
        '''
        self.next_slide()

        test = VGroup()
        test.add(r4k1, r4k2, r2k)
        self.play(FadeToColor(test, color=RED))
        self.play(circuit.node_list[2].animate.set_color(RED))
        self.play(circuit.node_list[3].animate.set_color(RED))
        self.play(circuit.node_list[4].animate.set_color(RED))
        
        '''
        SLIDE 3
        '''
        self.next_slide()

        self.play(circuit.animate.scale(.8))
        self.play(circuit.animate.to_edge(LEFT))
        delta = DeltaCreate().scale(.75).to_edge(RIGHT).shift(DOWN*2)
        self.play(FadeIn(delta))

        '''
        SLIDE 4
        '''
        self.next_slide()

        self.play(FadeOut(circuit))
        known_vals = MathTex(r"R_a = 4k\Omega \quad R_b = 4k\Omega \quad R_c = 2k").scale(.75).next_to(title, DOWN, buff=.2).to_edge(RIGHT)
        
        r1_eq = MathTex(r"R_1 = \frac{R_aR_b}{R_a+R_b+R_c}").scale(.75).next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(FadeIn(r1_eq))
        r2_eq = MathTex(r"R_2 = \frac{R_aR_c}{R_a+R_b+R_c}").scale(.75).next_to(r1_eq, DOWN, buff=.2)
        self.play(FadeIn(r2_eq))
        r3_eq = MathTex(r"R_3 = \frac{R_bR_c}{R_a+R_b+R_c}").scale(.75).next_to(r2_eq, DOWN, buff=.2)
        self.play(FadeIn(r3_eq))

        '''
        SLIDE 5
        '''
        self.next_slide()

        self.play(FadeIn(known_vals))
        r1_val = MathTex(r"R_1 = \frac{4k*4k}{4k+4k+2k} = \frac{16M}{10k}\Omega = 1.6k\Omega").scale(.75).next_to(r3_eq, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(r1_val))
        
        '''
        SLIDE 6
        '''
        self.next_slide()

        r2_val = MathTex(r"R_2 = \frac{4k*2k}{4k+4k+2k} = \frac{8M}{10k}\Omega = 0.8k\Omega").scale(.75).next_to(r1_val, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(r2_val))
        r3_val = MathTex(r"R_3 = \frac{4k*2k}{4k+4k+2k} = \frac{8M}{10k}\Omega = 0.8k\Omega").scale(.75).next_to(r2_val, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(r3_val))

        '''
        SLIDE 7
        '''
        self.next_slide()

        wye = WyeCreate().to_corner(DR)
        self.play(FadeOut(delta))
        self.play(FadeIn(wye))

        '''
        SLIDE 8
        '''
        self.next_slide()

        fadeout = VGroup()
        fadeout.add(r1_eq, r2_eq, r3_eq, r1_val, r2_val, r3_val, known_vals)
        self.play(FadeOut(fadeout))
        r2702 = Resistor(270).shift(LEFT * 3.5 + UP*4)
        r12 = Resistor("1.6k", direction=LEFT).rotate(270*DEGREES).shift(LEFT*1.75 + UP*3)
        r22 = (
            Resistor("800", direction=LEFT)
            .rotate(45 * DEGREES)
            .shift(LEFT * 2.5 + UP * 1.5)
        )
        r32 = Resistor("800", direction=LEFT).rotate(135 * DEGREES).shift(UP * 1.5 +LEFT*1)
        r11002 = Resistor("3.3k", direction=DOWN).shift(DOWN * 2 + LEFT * 1.75)
        r10k2 = Resistor("4.2k", direction=RIGHT).rotate(90 * DEGREES).shift(LEFT*3 + DOWN *.5)
        r62022 = (
            Resistor(900, direction=RIGHT)
            .rotate(90 * DEGREES)
            .shift(LEFT*.25 + DOWN *.5)
        )

        v202 = VoltageSource(20).shift(LEFT * 5+UP*.5)

        gnd2 = Ground(ground_type="ground").shift(LEFT * 5 + DOWN * 3)

        # Add Circuit components.
        circuit2 = Circuit()
        circuit2.add_components(r2702, r12, r22, r32, r11002, r10k2, r62022, v202, gnd2)

        # A much streamline and easier way to edit.
        circuit2.add_wire(gnd2.get_terminals(), v202.get_terminals("negative"))
        circuit2.add_wire(v202.get_terminals("negative"), r11002.get_terminals("left"))
       
        circuit2.add_wire(v202.get_terminals("positive"), r2702.get_terminals("left"))
        circuit2.add_wire(r2702.get_terminals("right"), r12.get_terminals("left"), invert = True)
        circuit2.add_wire(r12.get_terminals("right"), r22.get_terminals("right"))
        circuit2.add_wire(r12.get_terminals("right"), r32.get_terminals("right"))
        align10k = (r10k2.get_terminals("right") + r10k2.get_terminals("left")) / 2
        r10k2.move_to([r22.get_terminals("left")[0]+.35, align10k[1], align10k[2]])
        align6202 = (r62022.get_terminals("right") + r62022.get_terminals("left")) / 2
        r62022.move_to([r32.get_terminals("left")[0]+.35, align6202[1], align6202[2]])
        line1 = Line(start= r22.get_terminals("left"), end = r10k2.get_terminals("right"))
        line2 = Line(start = r32.get_terminals("left"), end = r62022.get_terminals("right"))
        circuit2.add_wire(r62022.get_terminals("left"), r11002.get_terminals("right"))
        circuit2.add_wire(r10k2.get_terminals("left"), r11002.get_terminals("left"))
        circuit2.add(line1, line2)
        circuit2.scale(.8).shift(DOWN*1)
        self.play(FadeIn(circuit2))

        '''
        SLIDE 9
        '''
        self.next_slide()

        self.play(FadeOut(wye))
        circuit.to_edge(RIGHT)
        self.play(FadeIn(circuit))
        
        '''
        SLIDE 10
        '''
        self.next_slide()

        self.play(FadeOut(circuit))
        eq = MathTex(r"R_{eq} = 270+1.6k + (800+4.2k)||(800+900+3.3k)").scale(.6).next_to(title, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(eq))
        
        '''
        SLIDE 11
        '''
        self.next_slide()

        eq1 = MathTex(r"R_{eq} = 1870 + 5k || 5k = 4370\Omega").scale(.6).next_to(eq, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(eq1))
        
        '''
        SLIDE 12
        '''
        self.next_slide()

        eq2 = MathTex(r"I_t = \frac{20}{4370} = \frac{2}{437} \approx 4.577mA").scale(.6).next_to(eq1, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(eq2))
        self.wait()
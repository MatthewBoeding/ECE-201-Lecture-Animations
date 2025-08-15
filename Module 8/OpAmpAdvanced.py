from manim import *
from manim_circuit import *
from manim_slides import Slide

class OpAmpAdvanced(Slide):
    def construct(self):
        title = Tex(r"Difference Amplifier").to_edge(UP)
        self.add(title)
        triangle = Triangle(color=WHITE).scale(1.5)
        ri = Resistor().scale(.5).shift(LEFT*.5)
        ri.remove(ri.label)
        leads = triangle.get_bottom()*[0,1,1]
        noninv = Line(leads+(ri.get_terminals("left")*[1,0,0]), leads+(ri.get_terminals("left")*[1,0,0])+[0,-.5,0])
        inv = Line(leads+(ri.get_terminals("right")*[1,0,0]), leads+(ri.get_terminals("right")*[1,0,0])+[0,-.5,0])
        opamp = VGroup().add(triangle, noninv, inv)
        opamp.rotate(DEGREES*-90)
        vout = Tex("$V_o$").scale(.5).move_to(triangle.get_right()+[.15,-.25,0])
        ri.rotate(-90*DEGREES).shift(LEFT*.25)
        noninv.shift(DOWN * (abs(noninv.get_center()-ri.get_terminals("left")))[1])
        noninvlabel = Tex(r'$-$').scale(.5).next_to(noninv, UP, buff=.2)
        inv.shift(DOWN * (abs(inv.get_center()-ri.get_terminals("right")))[1])
        invlabel = Tex(r'$+$').scale(.5).next_to(inv, DOWN, buff=.2)
        opamp.add(noninvlabel, invlabel, vout)
        noninvleadloc = triangle.get_left()*[1,0,1] + noninvlabel.get_center()*[0,1,0]
        invleadloc = triangle.get_left()*[1,0,1] + invlabel.get_center()*[0,1,0]
        noninvgnd = Ground().move_to(inv.get_center()+[-4,-1.5,0])
        vs = VoltageSource(dependent=False).scale(.75).shift(LEFT*2.5)
        vs.remove(vs.label)
  
        vs.move_to(inv.get_center()+[-4,-.75,0])
        vslab = Tex(r"$V_1$").scale(.6).next_to(vs, LEFT, buff=.2)

        r1 = Resistor().scale(.75).next_to(vs, UP, buff=.5)
        r1.move_to(noninv.get_start() + [-1.5,0,0])
        r1lab = Tex(r"$R_1$").scale(.75).next_to(r1,UP,buff=.2)
        
        r2 = Resistor().scale(.75).next_to(triangle, UP, buff=.5)
        r2lab = Tex(r"$R_2$").scale(.75).next_to(r2,UP,buff=.2)

        r3 = Resistor().scale(.75)
        r3.move_to(inv.get_start() + [-1.5,0,0])
        r3lab = Tex(r"$R_3$").scale(.75).next_to(r3,DOWN,buff=.2)

        r4 = Resistor().scale(.75).rotate(DEGREES*-90).move_to(r3.get_terminals("right")+[0,-1,0])
        r4lab = Tex(r"$R_4$").scale(.75).next_to(r4,LEFT,buff=.2)
        r4gnd = Ground().next_to(r4, DOWN, buff=.2)

        v2 = VoltageSource(dependent=False).scale(.75).next_to(vs, RIGHT, buff=.2).shift(DOWN*.5)
        v2.remove(v2.label)
        v2lab = Tex(r"$V_2$").scale(.6).next_to(v2, UP, buff=.2).shift(RIGHT*.2)
        v2gnd = Ground().next_to(v2, DOWN, buff=.2)
        invcirc = Circuit().add(noninvgnd, vs,  vslab, r1, r2, r1lab, r2lab, r3, r3lab, r4, r4lab, r4gnd, v2, v2lab, v2gnd)
        invcirc.add_wire(vs.get_terminals("negative"), noninvgnd.get_terminals())
        invcirc.add_wire(vs.get_terminals("positive"), r1.get_terminals("left"))
        invcirc.add_wire(r1.get_terminals("right"), noninv.get_start())
        invcirc.add_wire(r1.get_terminals("right"), r2.get_terminals("left"))
        invcirc.add_wire(r2.get_terminals("right"), triangle.get_right()+[.5,0,0], invert = True)
        invcirc.add_wire(triangle.get_right(), triangle.get_right()+[.5,0,0])
        invcirc.add_wire(v2.get_terminals("positive"), r3.get_terminals("left"))
        invcirc.add_wire(r3.get_terminals("right"), inv.get_start())
        invcirc.add_wire(r4.get_terminals("left"), r3.get_terminals("right"))
        invcirc.add_wire(r4.get_terminals("right"), r4gnd.get_terminals())
        invcirc.add_wire(v2.get_terminals("negative"), v2gnd.get_terminals())
        vgrp = VGroup().add(opamp, invcirc)
        
        self.play(Create(opamp), Create(invcirc))

        self.next_slide()

        

        # Step 1: Apply KCL at the non-inverting input node
        self.play(vgrp.animate.scale(.75))
        self.play(vgrp.animate.to_edge(LEFT))
        step1 = MathTex(
            r"\frac{V_2 - V_+}{R_3} = \frac{V_+}{R_4}",
            font_size=36
        ).next_to(title, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(step1))
        self.next_slide()

        # Step 2: Solve for V_+ from KCL
        step2 = MathTex(
            r"V_+ = V_2 \cdot \frac{R_4}{R_3 + R_4}",
            font_size=36
        ).next_to(step1, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(step2))
        self.next_slide()

        # Step 3: Apply KCL at the inverting input node
        step3 = MathTex(
            r"\frac{V_1 - V_-}{R_1} = \frac{V_- - V_o}{R_2}",
            font_size=34
        ).next_to(step2, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(step3))
        self.next_slide()

        # Step 4: Solve for V_- from KCL
        step4 = MathTex(
            r"V_- = \frac{R_2 V_1 + R_1 V_o}{R_1 + R_2}",
            font_size=32
        ).next_to(step3, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(step4))
        self.next_slide()

        # Step 5: Equate V_+ and V_- (ideal op-amp assumption)
        step5 = MathTex(
            r"\frac{R_2 V_1 + R_1 V_o}{R_1 + R_2} = V_2 \cdot \frac{R_4}{R_3 + R_4}",
            font_size=32
        ).next_to(step4, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(step5))
        self.next_slide()

        # Step 6: Solve for V_o
        step6 = MathTex(
            r"V_o = \left( V_2 \cdot \frac{R_4}{R_3 + R_4} - \frac{R_2}{R_1 + R_2} V_1 \right) \cdot \frac{R_1 + R_2}{R_1}",
            font_size=32
        ).next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(FadeOut(vgrp))
        self.wait()
        self.play(Write(step6))
        self.next_slide()

        # Final slide
        final = Tex("This is the expression for $V_o$ using KCL!", font_size=36)
        
        # Add a box around step6
        box = SurroundingRectangle(step6, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.play( Write(final))
        self.next_slide()


from manim import *
from manim_slides import Slide
from manim_circuit import *

class KirchoffsOverview(Slide):
    def construct(self):
        vo = VoltageSource(label=" ")
        vo.remove(vo.label)
        r2 = Resistor(label=" ").rotate(90*DEGREES).next_to(vo, RIGHT, buff=0.5).shift(RIGHT*3)
        r2.remove(r2.label)
        r1 = Resistor(label = " ").next_to(vo, UP, buff=0.5).shift(RIGHT*2)
        r1.remove(r1.label)
        r1_lab = Tex(r"$R_1$").next_to(r1, UP, buff=0.2)
        r2_lab = Tex(r"$R_2$").next_to(r2, RIGHT, buff=.2)
        vo_lab = Tex(r"$V_s$").next_to(vo, LEFT, buff=.2)
        circuit = Circuit().add(vo,r1,r2,r1_lab,r2_lab,vo_lab).scale(.8).to_edge(RIGHT)
        circuit.add_wire(vo.get_terminals("positive"), r1.get_terminals("left"))
        circuit.add_wire(r1.get_terminals("right"), r2.get_terminals("right"), invert = True)
        circuit.add_wire(r2.get_terminals("left"), r2.get_terminals("left")+(0,-.5,0))
        endpoint = vo.get_terminals("negative") * (1,0,1)  +  (r2.get_terminals("left")+(0,-.5,0))*(0,1,0)
        circuit.add_wire(vo.get_terminals("negative"), endpoint)
        circuit.add_wire(endpoint, r2.get_terminals("left")+(0,-.5,0))
        title = Tex(r"Kirchoff's Voltage Law (Loop Law)").to_corner(UL)
        self.add(title)
        self.play(FadeIn(circuit))

        self.next_slide()
        start = vo.get_terminals("negative")+(1,0,0)
        end = vo.get_terminals("negative")+(1.4,0,0)
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
        arrow = VGroup(arc, tip).next_to(vo, RIGHT, buff=.8)

        self.play(Create(arrow))
       
        pos1 = Tex(r"$+$").move_to(r1.get_terminals("left")+(0,.5,0))
        pos2 = Tex(r"$+$").move_to(r2.get_terminals("right")+(0.5,0,0))
        neg1 = Tex(r"$-$").move_to(r1.get_terminals("right")+(0,.5,0))
        neg2 = Tex(r"$-$").move_to(r2.get_terminals("left")+(0.5,0,0))
        vgrp = VGroup().add(pos1,pos2,neg1,neg2)
        self.play(Create(vgrp))

        items = [
            "Builds on conservation of energy",
            "Sum of voltages around an independent loop is zero",
            r"$\sum_j V_j = 0$"
        ]

        # Create each item with a bullet
        bullets = VGroup(*[
            Tex(rf"$\bullet$ {item}", font_size=36) for item in items
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        bullets.next_to(title, DOWN, buff=.2).to_edge(LEFT)

        self.play(FadeIn(bullets, shift=RIGHT))
        self.wait()
        self.next_slide()
        math = Tex(r"$-V_s + V_{R_1} + V_{R_2} = 0$").next_to(bullets, DOWN, buff=0.2)
        self.play(Write(math))
        self.next_slide()
        self.play(FadeOut(bullets))
        self.play(math.animate.next_to(title,DOWN,buff=.2))
        exp = Tex(r"Passive Sign Convention!\\Positive to negative terminal is positive!").next_to(math, DOWN, buff=0.2).to_edge(LEFT)
        self.play(Write(exp))
        self.next_slide()
        exp2 = Tex(r"Active Sign Convention flips signs").next_to(exp, DOWN, buff=0.2)
        self.play(Write(exp2))
        math2 = Tex(r"$V_s - V_{R_1} - V_{R_2} = 0$").next_to(exp2, DOWN, buff=0.2)
        self.play(Write(math2))

        self.next_slide()
        self.clear()
        title = Tex(r"Kirchoffs Current Law (Node Law)").to_corner(UL)
        self.play(Write(title))
        ra = Resistor(" ")
        rb = Resistor(" ").next_to(ra, RIGHT, buff=1)

        ra.remove(ra.label)
        rb.remove(rb.label)
        line1 = Line(start = ra.get_terminals("left") + [-.5, 0 , 0], end = ra.get_terminals("left"))
        line2 = Line(start = rb.get_terminals("right"), end = [.5,0,0]+rb.get_terminals("right"))
        
        node1 = Dot(point = line1.get_end()+[-.5,0,0])
        node2 = Dot(point = ra.get_terminals("right")+[.5,0,0]) 
        node3 = Dot(point = line2.get_end())
        
        rc = Resistor(" ").rotate(90*DEGREES).next_to(node2, DOWN, buff=0.2)
        rc.remove(rc.label)
        node4 = Dot(point = rc.get_terminals('left'))
        rc.shift(node2.get_center() - rc.get_terminals("right"))
        line3 = Line(start = rc.get_terminals("right"), end = node2.get_center())
        ra_lab = Tex("$R_1$").next_to(ra, UP,buff=.2)
        rb_lab = Tex("$R_2$").next_to(rb, UP,buff=.2)
        rc_lab = Tex("$R_3$").next_to(rc, LEFT, buff=0.2)
        line4 = Line(start=rc.get_terminals("left"), end = node4.get_center())
        n1 = Tex(r"$a$").next_to(node1, UP, buff=.2)
        n2 = Tex(r"$b$").next_to(node2, UP, buff=.2)
        n3 = Tex(r"$c$").next_to(node3, UP, buff=.2)
        circuit = Circuit().add(ra,rb,rc, line3,line1,line2,line4, node1,node2,node3,node4,ra_lab,rb_lab,rc_lab, n1,n2,n3).center().to_edge(RIGHT)
        circuit.add_wire(ra.get_terminals("right"), rb.get_terminals("left"))
        self.play(FadeIn(circuit))

        self.next_slide()
        kcl = Tex(r"Consider currents at node $b$").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(kcl))
        ira = Arrow(start=node1.get_center(), end=node2.get_center(), tip_length=0.1).scale(.5).next_to(ra, UP, buff=.2)
        irb = Arrow(start=node3.get_center(), end=node2.get_center(), tip_length=0.1).scale(.5).next_to(rb, UP, buff=.2)
        irc = Arrow(start=node4.get_center(), end=node2.get_center(), tip_length=0.1).scale(.5).next_to(rc, RIGHT, buff=.2)
        ira_lab = Tex(r"$I_{R_1}$").scale(.6).next_to(ira, UP, buff=.2)
        irb_lab = Tex(r"$I_{R_2}$").scale(.6).next_to(irb, UP, buff=.2)
        irc_lab = Tex(r"$I_{R_3}$").scale(.6).next_to(irc, RIGHT, buff = .2)
        grp = VGroup().add(ira,irb,irc,ira_lab,irb_lab,irc_lab)
        self.play(FadeOut(ra_lab),FadeOut(rb_lab),FadeOut(rc_lab))
        self.play(Create(grp))
        self.next_slide()

        eq = Tex(r"$\sum_j I_j = 0$").next_to(kcl, DOWN, buff=.2)
        eq2 = Tex(r"$I_{R_1} + I_{R_2} + I_{R_3} = 0$").next_to(eq, DOWN, buff=.2)
        self.play(Write(eq))
        self.play(Write(eq2))
        self.next_slide()
        self.play(Write(Tex(r"A current must be negative!").next_to(eq2, DOWN, buff = 0.2).to_edge(LEFT)))


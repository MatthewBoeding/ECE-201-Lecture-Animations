from manim import *
from manim_slides import Slide
from manim_circuit import *
import numpy as np


class ResistorCombinations(Slide):
    def construct(self):
        title = Tex("Series Resistors").to_edge(UP)
        ra = Resistor(" ")
        rb = Resistor(" ").next_to(ra, RIGHT, buff=1)
        ra.remove(ra.label)
        rb.remove(rb.label)
        line1 = Line(start = ra.get_terminals("left") + [-.5, 0 , 0], end = ra.get_terminals("left"))
        line2 = Line(start = rb.get_terminals("right"), end = [.5,0,0]+rb.get_terminals("right"))
        node1 = Dot(point = line1.get_end()+[-.5,0,0])
        node2 = Dot(point = ra.get_terminals("right")+[.5,0,0]) 
        node3 = Dot(point = line2.get_end())
        ra_lab = Tex("$R_1$").next_to(ra, DOWN,buff=.2)
        rb_lab = Tex("$R_2$").next_to(rb, DOWN,buff=.2)
        n1 = Tex(r"$a$").next_to(node1, UP, buff=.2)
        n2 = Tex(r"$b$").next_to(node2, UP, buff=.2)
        n3 = Tex(r"$c$").next_to(node3, UP, buff=.2)
        circuit = Circuit().add(ra,rb,line1,line2,node1,node2,node3,ra_lab,rb_lab,n1,n2,n3).center()
        circuit.add_wire(ra.get_terminals("right"), rb.get_terminals("left"))
        self.add(title)
        self.wait()
        self.play(FadeIn(circuit))

        '''
        SLIDE 2
        '''
        self.next_slide()

        blist1 = Tex(r"$\bullet$ Share 1 node").scale(.8).next_to(title, DOWN, buff=.2).to_edge(LEFT)
        blist2 = Tex(r"$\bullet$ Common Node has No Additional Branches").scale(.8).next_to(blist1, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(blist1))
        self.play(Write(blist2))

        '''
        SLIDE 3
        '''
        self.next_slide()

        kcl = Tex(r"KCL at $b$ \\ $\sum_{j=0}^n i_j = 0$").next_to(title, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(kcl))
        ira = Arrow(start=node1.get_center(), end=node2.get_center(), tip_length=0.1).scale(.5).next_to(ra, UP, buff=.2)
        irb = Arrow(start=node2.get_center(), end=node3.get_center(), tip_length=0.1).scale(.5).next_to(rb, UP, buff=.2)
        ira_lab = Tex(r"$I_{R_1}$").scale(.6).next_to(ira, UP, buff=.2)
        irb_lab = Tex(r"$I_{R_2}$").scale(.6).next_to(irb, UP, buff=.2)
        grp = VGroup().add(ira,irb,ira_lab,irb_lab)
        self.play(FadeIn(grp))
        circuit.add(grp)
        
        '''
        SLIDE 4
        '''
        self.next_slide()

        self.play(circuit.animate.to_edge(LEFT))
        kcl2 = Tex(r"$I_{R_1} = I_{R_2}$").next_to(kcl, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(kcl2))
        voltages = Tex(r"$V_{ac} = V_{ab}+V_{bc}$").next_to(kcl2, DOWN, buff=.2).to_edge(RIGHT)
        vab = Tex(r"$V_{ab} = I_{R_1}R_1$\\$V_{bc} = I_{R_2}R_2$").next_to(voltages, DOWN, buff=.2).to_edge(RIGHT)
        vac = Tex(r"$V_{ac} = IR_1 + IR_2$\\$V_{ac} = I(R_1+R_2)$").next_to(vab, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(voltages))
        self.play(Write(vab))
        self.play(Write(vac))

        '''
        SLIDE 5
        '''
        self.next_slide()

        grp2 = VGroup().add(kcl, kcl2, voltages, vab, vac)
        self.play(FadeOut(grp2))
        vac = Tex(r"$V_{ac} = I(R_1+R_2)$").next_to(title, DOWN, buff=.2).to_edge(RIGHT)
        self.play(FadeIn(vac))

        rac = Resistor(" ")
        rac.remove(rac.label)
        req = Tex(r"$R_{eq}$").next_to(rac, UP, buff=.2)
        na = Dot(point=rac.get_terminals("left")+[-.25,0,0])
        nc = Dot(point=rac.get_terminals("right")+[.25,0,0])
        na_lab = Tex(r"$a$").next_to(na, UP, buff=.2)
        nc_lab = Tex(r"$c$").next_to(nc, UP, buff=.2)
        circuit2 = Circuit().add(rac,req,na,nc, na_lab, nc_lab).next_to(vac, DOWN, buff=.2).to_edge(RIGHT)
        circuit.add_wire(rac.get_terminals("left"), na.get_center())
        circuit.add_wire(rac.get_terminals("right"), nc.get_center())

        self.play(FadeIn(circuit2))

        '''
        SLIDE 6'''
        self.next_slide()

        reqlab = Tex(r"$R_{eq} = R_1 + R_2$").next_to(circuit2, DOWN, buff = .5).to_edge(RIGHT)
        self.play(Write(reqlab))


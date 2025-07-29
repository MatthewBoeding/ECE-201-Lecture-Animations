from manim import *
from manim_slides import Slide
from manim_circuit import *


class CircuitOverview(Slide):
    def construct(self):
        title = Tex(r"DC Circuit Overview").to_edge(UP)
        charge = Tex(r"Electric Charge $\rightarrow$ Coulomb ($q$)").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        current = Tex(r"Electrical Current $\rightarrow i(t)=\frac{dq(t)}{dt}$").next_to(charge, DOWN, buff=.2).to_edge(LEFT)
        currsolv = Tex(r"$q(t) = \int_\infty^t i(\tau)d\tau$").next_to(current, DOWN, buff=.2) 
        direction = Tex(r"Current flow has direction").next_to(currsolv, DOWN, buff=.2).to_edge(LEFT)
        resistor = Resistor("").next_to(direction, RIGHT, buff=.2).shift(RIGHT*1+DOWN+.5)
        resistor.remove(resistor.label)
        nodea = Dot(resistor.get_terminals("left")+[-.2,0,0])
        linea = Line(resistor.get_terminals("left"), nodea.get_center())
        nodeb = Dot(resistor.get_terminals("right")+[.2,0,0])
        lineb = Line(resistor.get_terminals("right"), nodeb.get_center())
        alab = Tex(r"$a$").scale(.6).next_to(nodea, UP, buff=.1)
        blab = Tex(r"$b$").scale(.6).next_to(nodeb, UP, buff=.1)
        curra = Arrow(start=resistor.get_center()+[0,.25,0], end=resistor.get_center()+[1.25,.25,0], tip_length=0.1).scale(.5)
        curra.set_z_index(1)
        ia_lab = Tex(r"$I_{ab}$").scale(.75).next_to(curra, UP, buff = .2).shift(RIGHT*.5)
        curra.next_to(ia_lab, DOWN, buff=.1)
        self.play(Write(title))
        self.play(Write(charge))
        self.play(Write(current))
        self.play(Write(currsolv))
        self.play(Write(direction))

        self.next_slide()

        self.play(FadeIn(resistor),FadeIn(nodea),FadeIn(nodeb),FadeIn(linea),FadeIn(lineb),FadeIn(alab),FadeIn(blab),FadeIn(curra),FadeIn(ia_lab))
        currb =  Arrow(start=resistor.get_center()+[0,-.25,0], end=resistor.get_center()+[-1.25,-.25,0], tip_length=0.1).scale(.5)
        currb.set_z_index(1)
        ib_lab = Tex(r"$-I_{ab}$").scale(.75).next_to(currb, DOWN, buff = .2)
        dir2 = Tex(r"Arrow is only a reference!").next_to(direction, DOWN, buff=.2).to_edge(LEFT)

        self.next_slide()

        self.play(FadeIn(currb), FadeIn(ib_lab))
        self.play(Write(dir2))

        self.next_slide()

        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        volt = Tex(r"Voltage and Power").to_edge(UP)
        self.play(FadeIn(volt))
        energy = Tex(r"Energy (W) $\rightarrow$ Joule (Newton Meter)").scale(.8).next_to(volt, DOWN, buff=.2)
        voltage = Tex(r"Voltage $(V) = \frac{dW(t)}{dq}$").scale(.8).next_to(energy, DOWN, buff=.2)
        power = Tex(r"Power $\rightarrow$ Energy over time").scale(.8).next_to(voltage, DOWN, buff=.2)
        pow2 = Tex(r"$p(t) = \frac{dW(t)}{dt} \rightarrow W(t) = \int^t_{-\infty} p(\tau)d\tau$").scale(.8).next_to(power, DOWN, buff=.2)
        pow3 = Tex(r"$p(t) = \frac{dW(t)}{dq}\frac{dq(t)}{dt} = v(t) i(t)$").scale(.8).next_to(pow2, DOWN, buff=.2)

        self.play(Write(energy), Write(voltage), Write(power), Write(pow2), Write(pow3))
        
        self.next_slide()

        self.play(*[FadeOut(mob)for mob in self.mobjects])
        term = Tex(r"Terminology").to_edge(UP)
        self.play(Write(term))
        
        terminals = Tex(r"Terminals: connection points for an element").scale(.8).next_to(term,DOWN,buff=.2).to_edge(LEFT)
        node = Tex(r"Node: point of connection between 2 elements").scale(.8).next_to(terminals,DOWN,buff=.2).to_edge(LEFT)
        branch = Tex(r"Branch: single element between 2 nodes").scale(.8).next_to(node,DOWN,buff=.2).to_edge(LEFT)
        path = Tex(r"Path: a combination of branches that doesn't repeat").scale(.8).next_to(branch,DOWN,buff=.2).to_edge(LEFT)
        loop = Tex(r"Loop: a closed path").scale(.8).next_to(path,DOWN,buff=.2).to_edge(LEFT)
        self.play(Write(terminals))
        self.wait()
        self.play(Write(node))
        self.wait()
        self.play(Write(branch))
        self.wait()
        self.play(Write(path))
        self.wait()
        self.play(Write(loop))
        self.wait()
        dota = Dot()
        dotb = Dot().shift(RIGHT)
        linea = Line(dota.get_center(), dotb.get_center())
        vgrp = VGroup().add(dota, dotb, linea).next_to(loop, DOWN, buff=.25)
        self.play(FadeIn(vgrp)
        self.next_slide()
        
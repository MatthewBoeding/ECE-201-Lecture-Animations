from manim import *
from manim_slides import Slide
from manim_circuit import *


class OhmsLaw(Slide):
    def construct(self):
        title = Tex(r"Ohm's Law").to_edge(UP)
        voltage = Tex(r"$\bullet \quad V=\frac{Joule}{Coulomb}$").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        current = Tex(r"$\bullet \quad I=\frac{Coulomb}{Second}$").next_to(voltage, RIGHT, buff=.2)
        power = Tex(r"$\bullet \quad P = \frac{Joule}{second} = VI$").next_to(voltage, DOWN, buff=.2).to_edge(LEFT)
        self.add(title)
        self.play(Write(voltage))
        self.play(Write(current))
        self.play(Write(power))
        self.next_slide()
        vo = VoltageSource(label = " ")
        vo.remove(vo.label)
        
        nodea = Dot(vo.get_terminals("positive"))
        nodeb = Dot(vo.get_terminals("negative"))
        y_dist = (nodea.get_center() - nodeb.get_center())[1]
        rect = Rectangle(height = y_dist / 1.5, width = .5).shift(RIGHT*1)
        text = Tex("X").move_to(rect.get_center())
        line1 = Line(nodea.get_center(), (rect.get_center() * [ 1,0,1]+ nodea.get_center()*[0,1,0]))
        line2 = Line((rect.get_center() * [ 1,0,1]+ nodea.get_center()*[0,1,0]), rect.get_center() + [0,y_dist/3,0])
        line3 = Line(nodeb.get_center(), (rect.get_center() * [ 1,0,1]+ nodeb.get_center()*[0,1,0]))
        line4 = Line((rect.get_center() * [ 1,0,1]+ nodeb.get_center()*[0,1,0]), rect.get_center() + [0,-y_dist/3,0])
        self.add(nodea, nodeb, rect, text, line1, line2, line3, line4)
        self.wait()
        self.next_slide()
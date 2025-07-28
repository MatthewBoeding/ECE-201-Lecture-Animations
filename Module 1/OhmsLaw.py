from manim import *
from manim_slides import Slide
from manim_circuit import *


class OhmsLaw(Slide):
    def construct(self):
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
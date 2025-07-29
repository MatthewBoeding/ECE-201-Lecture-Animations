from manim import *
from manim_slides import Slide
from manim_circuit import *


class OhmsLaw(Slide):
    def construct(self):
        title = Tex(r"Ohm's Law").to_edge(UP)
        voltage = Tex(r"$\bullet \quad V=\frac{Joule}{Coulomb}$").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        current = Tex(r"$\bullet \quad I=\frac{Coulomb}{Second}$").next_to(voltage, RIGHT, buff=.2)
        power = Tex(r"$\bullet \quad P = \frac{Joule}{second} = VI$").next_to(current, RIGHT, buff=.2)

        self.add(title)
        self.play(Write(voltage))
        self.play(Write(current))
        self.play(Write(power))
        self.next_slide()
        vo = VoltageSource(label = " ")
        vo.remove(vo.label)
        
        nodea = Dot(vo.get_terminals("positive"))
        nodeb = Dot(vo.get_terminals("negative"))
        vx = Tex(r"$V_x$").scale(.55).next_to(nodea, DOWN, buff=0.1)
        irc = Arrow(start=nodea.get_center()+[0,.25,0], end=nodea.get_center()+[.5,.25,0], tip_length=0.1).scale(.5)
        irc_lab = Tex(r"$I_{X}$").scale(.6).next_to(irc, UP, buff = .2).scale(.75)

        y_dist = (nodea.get_center() - nodeb.get_center())[1]
        rect = Rectangle(height = y_dist / 1.5, width = .5).shift(RIGHT*1)
        text = Tex("X").move_to(rect.get_center())
        line1 = Line(nodea.get_center(), (rect.get_center() * [ 1,0,1]+ nodea.get_center()*[0,1,0]))
        line2 = Line((rect.get_center() * [ 1,0,1]+ nodea.get_center()*[0,1,0]), rect.get_center() + [0,y_dist/3,0])
        line3 = Line(nodeb.get_center(), (rect.get_center() * [ 1,0,1]+ nodeb.get_center()*[0,1,0]))
        line4 = Line((rect.get_center() * [ 1,0,1]+ nodeb.get_center()*[0,1,0]), rect.get_center() + [0,-y_dist/3,0])
        vgrp = VGroup().add(nodea, nodeb, rect, text, line1, line2, line3, line4, vx, irc, irc_lab).to_edge(RIGHT).shift(LEFT*1.5)
        self.play(FadeIn(vgrp))
        self.wait()
        self.next_slide()

        ohms = Tex(r"Ohm's Law: There is a linear relationship between Voltage and\\current passing through an electrical element").scale(.75).next_to(voltage, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(ohms))

        vir = Tex(r"$V=IR \quad \quad \quad R=\frac{V}{I}\quad \quad \quad I = \frac{V}{R}$").next_to(ohms, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(vir))

        vix = Tex(r"$R_x = \frac{V_x}{I_x}$").scale(.75).next_to(vgrp, LEFT, buff=.2)
        self.play(Write(vix))
        self.next_slide()

        self.play( *[FadeOut(mob)for mob in self.mobjects])
        title = Tex(r"Ohm's Law Examples").to_edge(UP)
        self.play(Write(title))

        vo = VoltageSource(12).to_edge(LEFT)
        r1 = Resistor("2k", direction=RIGHT).rotate(DEGREES *-90).next_to(vo, RIGHT, buff=.2).shift(RIGHT*1)
        gnd = Ground().move_to(vo.get_terminals("negative")).shift(DOWN*.75)
        circuit = Circuit().add(vo,r1)
        circuit.add_wire(vo.get_terminals("positive"), r1.get_terminals("left"))
        circuit.add_wire(vo.get_terminals("negative"), gnd.get_terminals())
        circuit.add_wire(gnd.get_terminals(), r1.get_terminals("right"), invert = True)
        self.play(FadeIn(circuit))

        v1 = VoltageSource().to_edge(RIGHT)
        v1.remove(v1.label)
        vs = Tex(r"$V_s$").scale(.75).next_to(v1, LEFT, buff=.1)
        r2 = Resistor("16k", direction=LEFT).rotate(DEGREES *-90).next_to(v1, LEFT, buff=.2).shift(LEFT*1+DOWN*.25)
        pw = Tex(r"$P=3.6mW$").scale(.5).next_to(r2, LEFT, buff=.2).shift(DOWN*.5+RIGHT*.5)
        gnd = Ground().next_to(v1, DOWN, buff=.75)
        circuit2 = Circuit().add(v1,r2,vs,pw)
        circuit2.add_wire(v1.get_terminals("positive"), r2.get_terminals("left"), invert = True)
        circuit2.add_wire(v1.get_terminals("negative"), gnd.get_terminals())
        circuit.add_wire(gnd.get_terminals(), r2.get_terminals("right"), invert = True)
        self.play(FadeIn(circuit2))

        self.next_slide()
        ix = Tex(r"$I = \frac{V}{R}$\\$I_T = \frac{12V}{2k\Omega} = 6mA$").scale(.75).next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(ix))

        self.next_slide()
        vs = Tex(r"$P = VI \rightarrow P = V(\frac{V}{R})$").scale(.75).next_to(title, DOWN, buff=.2).to_edge(RIGHT)
        vs2 = Tex(r"$V^2 = PR = 3.6mW * 16k\Omega = 36V^2$\\$V = 6V \quad I = .6mA$").scale(.75).next_to(vs, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(vs))
        self.play(Write(vs2))

        self.next_slide()
        self.play( *[FadeOut(mob)for mob in self.mobjects])
        title = Tex(r"Resistors").to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": WHITE}
        ).scale(.75)
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        line = axes.plot(lambda x: x, color=RED)  # y = x line
        point_line1 = Line(
            start=axes.c2p(1.5, 1.5),
            end=axes.c2p(1.5, 1),
            color=WHITE
        )

        point_line2 = Line(
            start=axes.c2p(1, 1),
            end=axes.c2p(1.5, 1),
            color=WHITE
        )

        Lab = Tex(r"$\frac{1}{R}$").scale(.75).next_to(point_line1, RIGHT, buff=.2)

        self.play(Create(axes), Create(line), Create(point_line1), Create(point_line2), Write(Lab), Write(x_label), Write(y_label))
        
        desc = Tex(r"Resistors are linear!\\Power is absorbed, not supplied!").scale(.75).next_to(title,DOWN,buff=.2).to_edge(RIGHT)
        self.play(Write(desc))

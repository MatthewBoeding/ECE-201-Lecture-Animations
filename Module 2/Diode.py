from manim import *
from manim_slides import Slide
from manim_circuit import *
import numpy as np


class DiodeLecture(Slide):
    def construct(self):
        title = Tex(r"Diodes - Nonlinear Solid State Devices").to_corner(UL)
        title2 = Tex(r"Linear Devices - Resistors").scale(.5)
        r1= Resistor().rotate(90*DEGREES).scale(.8)
        r1.remove(r1.label)
        
        diode = VGroup()
        diode.add(Triangle(color=WHITE).scale(.8).rotate(DEGREES*60))
        diode.add(Line(start = [0,0,0], end = [1,0,0]).next_to(diode[0], DOWN, buff=0))
        diode.add(Line(start = [0,0,0], end = [0,1,0]).next_to(diode[0], DOWN, buff=0))
        diode.add(Line(start = [0,0,0], end = [0,1,0]).next_to(diode[0], UP, buff=0))
        diode.scale(.8)

        # Define axes
        axes = Axes(
            x_range=[-0.2, 0.8, 0.1],
            y_range=[-1, 12, 2],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True},
            tips=False,
        )
        axes.scale(.6)
        axes_labels = axes.get_axis_labels(x_label="V", y_label="I")
        
        # Physical constants for the real diode model
        Is = 1e-12  # Saturation current
        Vt = 0.0259 # Thermal voltage (approx. at room temp)

        V_vals = np.linspace(-0.2, 0.8, 500)
        I_vals = np.empty(shape = (500,))
        idx = 0
        for V in V_vals:
            if V < 0:
                I_vals[idx] = -Is
            else:
                I_guess = Is * np.exp(V / Vt)
                I_vals[idx] = I_guess
                if I_guess > 12:
                    break
            idx = idx + 1


        # Scale data to match axes
        graph = axes.plot_line_graph(
            x_values=V_vals[:idx],
            y_values=I_vals[:idx],
            line_color=RED,
            add_vertex_dots=False
        )


        
        h_line = axes.plot(lambda x: 0, x_range=[0, 0.7], color=BLUE)
        
        start = axes.c2p(0.7, 0)
        end = axes.c2p(0.7, 12)
        v_line = Line(start, end, color=BLUE)
        # Vertical line at x = 0.7 for y > 0 (say y from 0 to 1.5)

        vf_label = MathTex("V_F").scale(0.5).next_to(v_line, UP)
        r_graph = axes.plot(lambda x: 20*x, color=GREEN)
        slope_line1 = Line(start = axes.c2p(.1, 2),  end = axes.c2p(.2, 2))
        slope_line2 = Line(start = axes.c2p(.2,2), end = axes.c2p(.2,4))
        slope_label = Tex(r"$\frac{1}{R}$").scale(.8).next_to(slope_line2, RIGHT, buff=.2)
        check_valve_line1 = Line(start=[-2,1,0], end = [2,1,0])
        check_valve_line2 = Line(start=[-2,-1,0], end = [2,-1,0])
        valve_line1 = Line(start=[0,1,0], end=[0,0,0])
        valve_line2 = Line(start=[0,-1,0], end = [0,0,0])
        valve = VGroup().add(check_valve_line1,check_valve_line2,valve_line1, valve_line2)
        dot1 = Dot(point=[-1,0,0],radius=.25,color=YELLOW)
        dot2 = Dot(point=[-1,0,0],radius=.1,color=YELLOW)
        dot3 = Dot(point=[1,0,0],radius=.4,color=YELLOW)
        #==========================================ANIMATIONS===============================================
        self.add(title, diode)
        self.wait()

        '''
        SLIDE 2
        '''
        self.next_slide()
    
        self.play(FadeOut(diode))
        diode.to_corner(UL).scale(.7)
        title2 = Tex(r"Check Valve Analogy:").next_to(diode, RIGHT, buff=.5)
        self.play(FadeIn(diode), FadeIn(title2))
        self.play(FadeIn(valve))
        self.play(FadeIn(dot1))

        '''
        SLIDE 3
        '''
        self.next_slide()
        
        title3 = Tex(r"Uni-Directional Flow").next_to(title2, DOWN, buff=.2)
        self.play(FadeIn(title3))
        self.play(dot1.animate.shift(RIGHT*.75))
        self.play(Rotate(valve_line1, angle = 45*DEGREES, about_point = [0,1,0]), Rotate(valve_line2, angle = -45*DEGREES, about_point = [0,-1,0]),
                  MoveAlongPath(dot1, Line(start = [-.25,0,0], end = [.8,0,0])))
        
        '''
        SLIDE 4
        '''
        self.next_slide()

        self.play(Rotate(valve_line1, angle = -45*DEGREES, about_point = [0,1,0]), Rotate(valve_line2, angle = 45*DEGREES, about_point = [0,-1,0]),
                  MoveAlongPath(dot1, Line(start=[0.8,0,0],end=[1.5,0,0])))

        '''
        SLIDE 5
        '''
        self.next_slide()

        self.play(FadeOut(title3))
        title3 = Tex(r"Not Enough Volume").next_to(title2, DOWN, buff=.2)
        self.play(FadeIn(title3))
        self.play(FadeOut(dot1))
        self.play(FadeIn(dot2))
        self.play(dot2.animate.shift(RIGHT*.9))
        self.play(dot2.animate.shift(LEFT*.1))
        self.play(dot2.animate.shift(RIGHT*.1))
        self.play(dot2.animate.shift(LEFT*.1))
        self.play(dot2.animate.shift(RIGHT*.1))
        self.play(dot2.animate.shift(LEFT*.1))
        self.play(dot2.animate.shift(RIGHT*.1))

        '''
        SLIDE 6
        '''
        self.next_slide()

        self.play(FadeOut(title3))
        title3 = Tex(r"Incorrect Direction").next_to(title2, DOWN, buff=.2)
        self.play(FadeIn(title3), FadeOut(title2))
        self.play(FadeOut(dot2), FadeIn(dot3))
        self.play(dot3.animate.shift(LEFT*.6))
        self.play(dot3.animate.shift(RIGHT*.1))
        self.play(dot3.animate.shift(LEFT*.1))
        self.play(dot3.animate.shift(RIGHT*.1))
        self.play(dot3.animate.shift(LEFT*.1))
        self.play(dot3.animate.shift(RIGHT*.1))

        '''
        SLIDE 7
        '''
        self.next_slide()

        title2 = Tex(r"Linear Devices - Resistors").scale(.5)
        self.play(FadeOut(valve), FadeOut(dot3), FadeOut(title3))
        title2.next_to(diode, DOWN, buff=.2).to_edge(LEFT)
        r1.next_to(title2, DOWN,buff=.2)
        self.play(FadeIn(title2),FadeIn(r1))
        self.play(r1.animate.to_edge(LEFT))
        

        # Add all elements to scene
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(r_graph))
        self.play(Create(slope_line1), Create(slope_line2), Write(slope_label))

        rline = Line(start = [0,0,0], end = [0,.5,0], color = GREEN).rotate(DEGREES*90).next_to(r1, DOWN, buff=.2).to_edge(LEFT)
        dline = Line(start = [0,0,0], end = [0,.5,0], color = BLUE).rotate(DEGREES*90).next_to(rline, DOWN, buff=.2).to_edge(LEFT)
        diline = Line(start = [0,0,0], end = [0,.5,0], color = RED).rotate(DEGREES*90).next_to(dline, DOWN, buff=.2).to_edge(LEFT)
        rlabel = Tex(r"Resistor - Ideal").scale(.4).next_to(rline, RIGHT, buff=.2)
        dlab = Tex(r'Diode - Ideal').scale(.4).next_to(dline,RIGHT,buff=.2)
        dilab = Tex(r'Diode - Actual').scale(.4).next_to(diline,RIGHT,buff=.2)
        self.play(FadeIn(rline), FadeIn(rlabel))

        '''
        SLIDE 8
        '''
        self.next_slide()

        self.play(Create(h_line), Create(v_line))
        self.play(Write(vf_label))
        self.play(FadeIn(dline), FadeIn(dlab))

        '''
        SLIDE 9
        '''
        self.next_slide()

        self.play(Create(graph))
        self.play(FadeIn(diline), FadeIn(dilab))
        self.wait(2)

        '''
        SLIDE 10
        '''
        self.next_slide()

        title3 = Tex(r"Linear Representation in Circuit Analysis").scale(.5).next_to(title, DOWN, buff=.2).to_edge(LEFT)
        group = VGroup()
        group.add(h_line, v_line, vf_label, rline, rlabel, slope_line1, slope_line2, slope_label, axes, axes_labels, r_graph,r1, title2, dlab, dline)
        self.play(FadeOut(graph), FadeOut(diline), FadeOut(dilab), FadeOut(diode), FadeOut(group))
        vo = VoltageSource(value = " ",label=False, dependent = False).shift(LEFT * 3)
        vo.remove(vo.label)
        ri = Resistor(" ")
        ri.remove(ri.label)
        ri.shift(UP*1+LEFT*.5)
        diode.next_to(vo, RIGHT, buff = 0.2).shift(RIGHT*3)
        circuit = Circuit().add(ri, vo, diode)
        circuit.add_wire(vo.get_terminals("positive"),ri.get_terminals("left"))
        circuit.add_wire(ri.get_terminals("right"), diode[3].get_end())
        circuit.add_wire(diode[2].get_start(), vo.get_terminals("negative"), invert=True)

        self.play(FadeIn(circuit))

        '''
        SLIDE 11
        '''
        self.next_slide()

        self.play(circuit.animate.to_edge(LEFT))
        v2 = VoltageSource(value = " ",label=False, dependent = False).shift(RIGHT * 1)
        v2.remove(v2.label)
        r3 = Resistor(" ")
        r3.remove(r3.label)
        r3.shift(UP*1+RIGHT*2.5)
        v1 = VoltageSource(value = " ",label=False, dependent = False).next_to(v2, RIGHT, buff=.2).shift(RIGHT*2.75+UP*.5).scale(.6)
        v1.remove(v1.label)
        r2 = Resistor(" ").scale(.5).rotate(90*DEGREES).next_to(v1, DOWN, buff=0.25)
        r2.remove(r2.label)
        vf = Tex(r"$V_F$").scale(.8).next_to(r2, RIGHT, buff=.2)
        circuit2 = Circuit().add(v2,r3,v1,r2)
        circuit2.add_wire(v2.get_terminals("positive"),r3.get_terminals("left"))
        circuit2.add_wire(r2.get_terminals("right"), v1.get_terminals("negative"))
        circuit2.add_wire(r3.get_terminals("right"), v1.get_terminals("positive"), invert = True)
        circuit2.add_wire(r2.get_terminals("left"), v2.get_terminals("negative"), invert = True)
        circuit2.add(vf)
        circuit2.to_edge(RIGHT)
        
        self.play(FadeIn(circuit2))

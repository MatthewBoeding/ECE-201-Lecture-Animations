from manim import *
from manim_slides import Slide
from manim_circuit import *

class Resistor(VMobject):
    def __init__(self, label=None, direction=DOWN, **kwargs):
        # initialize the vmobject
        super().__init__(**kwargs)
        self._direction = direction
 
        # Less points, more cleaner!
        self.main_body = VMobject()
        points = [
            [-2.5, 0, 0],
            [-2.2438, 0, 0],
            [-1.39324, 0, 0],
            [-0.54268, 1, 0],
            [0.30788, -1, 0],
            [1.15843, 1, 0],
            [2.00899, -1, 0],
            [2.85954, 1, 0],
            [3.7101, -1, 0],
            [4.13537, 0, 0],
            [4.98593, 0, 0]
        ]
        self.main_body.start_new_path(points[0])
        for i in points[1:]:
            self.main_body.add_line_to(np.array(i))
        self.main_body.scale(0.25).center()
 
        self.add(self.main_body)
 
        # check if lebel is present.
        if not label is None:
            self.label = (
                Tex(str(label))
                .scale(0.5)
                .next_to(self.main_body, self._direction, buff=0.1)
            )
            self.add(self.label)
        else:
            self.label = None
 
    def get_anchors(self):
        return [self.main_body.get_start(), self.main_body.get_end()]
 
    def get_terminals(self, val):
        if val == "left":
            return self.main_body.get_start()
        elif val == "right":
            return self.main_body.get_end()
 
    def center(self):
        self.shift(
            DOWN * self.main_body.get_center()[1] + LEFT * self.main_body.get_center()
        )
 
        return self
 
    def rotate(self, angle, *args, **kwargs):
        super().rotate(angle, about_point=self.main_body.get_center(), *args, **kwargs)
        if not self.label == None:
            self.label.rotate(-angle).next_to(self.main_body, self._direction, buff=0.1)
 
        return self

class WheatstoneProof(Slide):
    def construct(self):
        '''
        SLIDE 1
        '''
        bridge = VGroup()
        #Top Terminals are "right"
        title = Text(r"Wheatstone Bridge").scale(.8).to_edge(UP)
        r1 = Resistor("$R_1$", direction=LEFT).rotate(45 * DEGREES).shift(LEFT * .75 + UP * .75)
        r2 = Resistor("$R_2$", direction=RIGHT).rotate(135 * DEGREES).shift(UP * .75 + RIGHT * .75)
        r3 = Resistor("$R_3$", direction=LEFT).rotate(135 * DEGREES).shift(LEFT * .75 + DOWN*.75)
        r4 = Resistor("$R_4$", direction=RIGHT).rotate(45 * DEGREES).shift(DOWN * .75 + RIGHT * .75)
        vo = VoltageSource(value = " ",label=False, dependent = False).shift(LEFT * 3)
        circuit = Circuit().add(r1,r2,r3,r4,vo)
        circuit.add_wire(vo.get_terminals("positive"),r1.get_terminals("right"))
        circuit.add_wire(r1.get_terminals("right"),r2.get_terminals("right"))
        circuit.add_wire(r1.get_terminals("left"), r3.get_terminals("right"), invert = True)
        circuit.add_wire(r2.get_terminals("left"), r4.get_terminals("right"), invert = True)
        circuit.add_wire(r3.get_terminals("left"), vo.get_terminals("negative"), invert = True)
        circuit.add_wire(r4.get_terminals("left"), vo.get_terminals("negative"), invert = True)
        circle = Circle(radius=.25, color=WHITE)
        circuit.add(circle)
        circuit.scale(1.2).to_edge(LEFT)
        
        r1_terms = r1.get_terminals("left")
        r2_terms = r2.get_terminals("left")
        circ_cent = circle.get_center()
        dot_left = Dot(point = [r1_terms[0], circ_cent[1], r1_terms[2]], color=WHITE)
        dot_right = Dot(point= [r2_terms[0], circ_cent[1], r2_terms[2]], color=WHITE)
        line1 = Line(start=[r1_terms[0], circ_cent[1], r1_terms[2]] , end = circ_cent-[.25,0,0])
        line2 = Line(start=[r2_terms[0], circ_cent[1], r2_terms[2]], end = circ_cent+[.25,0,0])
        # Create the text
        text = Text("A", font_size=24)

        # Move the text to the center of the circle
        text.move_to(circ_cent)
        bridge.add(circuit, circle, text, line1, line2, dot_left, dot_right)
        self.add(bridge, title)
        self.wait()

        '''
        SLIDE 2
        '''
        self.next_slide()
        balance = Text(r"A Bridge is called balanced when").scale(.6).next_to(title, DOWN, buff=0.2).to_edge(RIGHT)
        balance2 = Text(r"Ammeter reads 0 Amps").scale(.6).next_to(balance, DOWN, buff=0.2).to_edge(RIGHT)
        self.play(Write(balance), Write(balance2))


        '''
        SLIDE 3
        '''
        self.next_slide()

        self.play(FadeOut(bridge[1], bridge[2], bridge[3], bridge[4]))
        linex = Line(start = dot_left.get_center(), end = dot_right.get_center())

        self.play(FadeIn(linex))
        va = MathTex("a").scale(.5).next_to(dot_left, LEFT, buff=0.2)
        vb = MathTex(r"b").scale(.5).next_to(dot_right, RIGHT, buff=0.2)
        self.play(Write(va), Write(vb))
        
        arr = Arrow(start=dot_left.get_center()+[.5,0.2,0], end=dot_right.get_center()-[.5,-.2,0], tip_length=0.1).scale(.3)
        arrlab = MathTex(r"I_A").scale(.6).next_to(arr, UP, buff=0.2)
        self.play(FadeIn(arr), FadeIn(arrlab))

        '''
        SLIDE 4
        '''
        self.next_slide()
        self.play(FadeOut(balance), FadeOut(balance2))
        kcla3 = Tex(r"If $I_A = 0$, then $V_a = V_b$!").scale(.6).next_to(title, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(kcla3))

        '''
        SLIDE 5
        '''
        self.next_slide()

        vat = Tex(r"$V_a = \frac{R_1}{R_1+R_3}V$").scale(.6).next_to(kcla3, DOWN, buff=.2).to_edge(RIGHT)
        vbt = Tex(r"$V_b = \frac{R_2}{R_2+R_4}V$").scale(.6).next_to(vat, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(vat))
        self.play(Write(vbt))
        vab = Tex(r"$\frac{R_1}{R_1+R_3}V = \frac{R_2}{R_2+R_4}V$").scale(.6).next_to(vbt, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(vab))

        '''
        SLIDE 6
        '''
        self.next_slide()

        r4t = Tex(r"Simplify:").scale(.6).next_to(vab, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(r4t))
        r4t2 = MathTex(r"\frac{R_3}{R_1} = \frac{R_4}{R_2}").scale(.6).next_to(r4t, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(r4t2))

        '''
        SLIDE 7
        '''
        self.next_slide()

        rx = Tex(r"We can find one unkown resistor value!").scale(.6).next_to(r4t2, DOWN, buff=.2).to_edge(RIGHT)
        rx2 = Tex(r"Originally used in Ohm-meters.").scale(.6).next_to(rx, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(rx),Write(rx2))

        '''
        SLIDE 8
        '''
        self.next_slide()

        self.play(FadeOut(kcla3), FadeOut(vat), FadeOut(vbt), FadeOut(vab), FadeOut(r4t), FadeOut(r4t2), FadeOut(arr), FadeOut(arrlab), FadeOut(linex))
        self.play(FadeOut(rx), FadeOut(rx2))
        Vlab = Tex(r"$V_{ab}$").scale(.5).next_to(bridge[3], RIGHT, buff=0.05)
        self.play(FadeIn(bridge[3], bridge[4]))
        self.play(FadeIn(Vlab))
        circuit.remove(circle)

        '''
        SLIDE 9
        '''
        self.next_slide()

        vo.remove(vo.label)
        vo.label = Tex(r"15V").scale(.5).next_to(vo, LEFT, buff=.2)
        vo.add(vo.label)
        r1.remove(r1.label)
        r1.label = Tex(r"540$\Omega$").scale(.5).next_to(r1, LEFT, buff=.2)
        r1.add(r1.label)
        r2.remove(r2.label)
        r2.label = Tex(r"2k$\Omega$").scale(.5).next_to(r2, RIGHT, buff=.2)
        r2.add(r2.label)
        r3.remove(r3.label)
        r3.label = Tex(r"270$\Omega$").scale(.5).next_to(r3, LEFT, buff=.2)
        r3.add(r3.label)
        self.remove(circuit)
        self.add(circuit)
        app = Tex(r"What if we have a variable resistor? $R_4$").scale(.6).next_to(title, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app))

        '''
        SLIDE 10
        '''
        self.next_slide()

        app2 = Tex(r"For the circuit to be balanced:").scale(.6).next_to(app, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app2))
        app3 = MathTex(r"\frac{R_3}{R_1} = \frac{R_4}{R_2}").scale(.6).next_to(app2, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app3))
        app4 = MathTex(r"\frac{270}{540} = \frac{R_4}{2k} \rightarrow R_4 = 1k\Omega").scale(.6).next_to(app3, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app4))
        app5 = MathTex(r"V_a = 15V\frac{540}{540+270} = 10V").scale(.6).next_to(app4, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app5))

        '''
        SLIDE 11
        '''
        self.next_slide()
        
        self.play(FadeOut(app2), FadeOut(app3), FadeOut(app4), FadeOut(app5))
        app2 = Tex(r"$V_a = 10V$").scale(.6).next_to(app, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app2))
        app3 = Tex(r"What if $V_{ab} = 1V$?").scale(.6).next_to(app2, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app3))
        app4 = MathTex(r"V_{ab}=V_a-V_b ").scale(.6).next_to(app3, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app4))
        app5 = MathTex(r"1V = 10V - V_b").scale(.6).next_to(app4, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app5))
        app6 = MathTex(r"V_b = 9V = \frac{2k}{2k+R_4}15V").scale(.6).next_to(app5, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app6))

        '''
        SLIDE 12
        '''
        self.next_slide()

        app7 = MathTex(r"R_4 = \frac{15V}{9V}2k\Omega-2k\Omega").scale(.6).next_to(app6, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app7))
        app8 = MathTex(r"R_4 = \frac{4}{3}k\Omega").scale(.6).next_to(app7, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(app8))
        self.wait()
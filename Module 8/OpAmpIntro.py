from manim import *
from manim_circuit import *
from manim_slides import Slide

class OpAmpIntro(Slide):
    def construct(self):
        title = Tex("Operational Amplifier Introduction").to_edge(UP)
        self.add(title)
        triangle = Triangle(color=WHITE).scale(1.5)
        ri = Resistor().scale(.5).shift(LEFT*.5)
        ri.remove(ri.label)
        leads = triangle.get_bottom()*[0,1,1]
        noninv = Line(leads+(ri.get_terminals("left")*[1,0,0]), leads+(ri.get_terminals("left")*[1,0,0])+[0,-.5,0])
        inv = Line(leads+(ri.get_terminals("right")*[1,0,0]), leads+(ri.get_terminals("right")*[1,0,0])+[0,-.5,0])
        opamp = VGroup().add(triangle, noninv, inv)
        opamp.rotate(DEGREES*-90)
        vout = Tex("$V_o$").scale(.5).move_to(triangle.get_right()+[.15,0,0])
        ri.rotate(-90*DEGREES).shift(LEFT*.25)
        noninv.shift(DOWN * (abs(noninv.get_center()-ri.get_terminals("left")))[1])
        noninvlabel = Tex(r'$+$').scale(.5).next_to(noninv, UP, buff=.2)
        inv.shift(DOWN * (abs(inv.get_center()-ri.get_terminals("right")))[1])
        invlabel = Tex(r'$-$').scale(.5).next_to(inv, DOWN, buff=.2)
        opamp.add(noninvlabel, invlabel, vout)
        self.play(Create(opamp))


        self.next_slide()

        self.play(opamp.animate.scale(2))
        rilab = Tex("$R_i$").scale(.5).next_to(ri, RIGHT, buff=.2)
        riLeadLeft = Line(ri.get_terminals("left"), ri.get_terminals("left")*[1,0,1]+noninv.get_center()*[0,1,0])
        riLL2 = Line(noninv.get_center(), ri.get_terminals("left")*[1,0,1]+noninv.get_center()*[0,1,0])
        riLeadRight = Line(ri.get_terminals("right"), ri.get_terminals("right")*[1,0,1]+inv.get_center()*[0,1,0])
        riLR2  = Line(inv.get_center(), ri.get_terminals("right")*[1,0,1]+inv.get_center()*[0,1,0])
        vo = VoltageSource("", dependent=True).scale(.5).shift(RIGHT*.25)
        vo.shift((vo.get_terminals("positive")-triangle.get_right())*[0,-1,0])
        vo.remove(vo.label)
        volab = Tex("$A(v_p-v_n)$").scale(.5).next_to(vo, RIGHT, buff=.2).shift(LEFT*.1+DOWN*.1)
        gnd = Ground().scale(.6).move_to(vo.get_terminals("negative")).shift(DOWN*.25)
        lgnd = Line(gnd.get_terminals(), vo.get_terminals("negative"))
        ro = Resistor().scale(.5).move_to(vo.get_terminals("positive")).shift(RIGHT*.5)
        ro.remove(ro.label)
        rolab = Tex("$R_o$").scale(.5).next_to(ro, UP, buff=.2)
        lout = Line(ro.get_terminals("right"), triangle.get_right())
        lout2 = Line(vo.get_terminals("positive"), ro.get_terminals("left")+[.01,0,0])
        linearModel = VGroup().add(ri, rilab, riLeadLeft, riLeadRight, vo, volab, ro, rolab, lout, lout2, riLL2, riLR2, gnd, lgnd)
        self.play(Create(linearModel))

        self.next_slide()
        vs = VoltageSource(dependent=False).scale(.75)
        vs.remove(vs.label)
        vslab = Tex(r"$V_s$").scale(.6).next_to(vs, RIGHT, buff=.2)
        vs.move_to(inv.get_center()+[-1.5,.75,0])
        rl = Resistor().scale(.4).rotate(-90*DEGREES)
        rl.shift(lout.get_end()-rl.get_terminals('left'))
        rllab = Tex(r"$R_L$").scale(.5).next_to(rl, RIGHT, buff=.2)
        circuit = Circuit().add(vs)
        circuit.add_wire(vs.get_terminals("positive"), noninv.get_center())
        circuit.add_wire(vs.get_terminals("negative"), inv.get_center())
        
        self.play(Create(circuit))

        self.next_slide()

        circuit.add_wire(ri.get_terminals("right"), gnd.get_terminals())
        self.play(FadeOut(triangle), FadeOut(noninvlabel), FadeOut(invlabel), FadeOut(vout))
        self.play(Create(rl), Create(rllab))
        lint = Line(gnd.get_terminals(), rl.get_terminals("right")*[1,0,1]+gnd.get_terminals()*[0,1,0])
        lint2 = Line(rl.get_terminals("right")*[1,0,1]+gnd.get_terminals()*[0,1,0], rl.get_terminals("right"))
        self.play(FadeIn(lint), FadeIn(lint2))

        self.next_slide()

        allcirc = VGroup().add(mob for mob in self.mobjects)
        self.play(allcirc.animate.to_edge(LEFT))
        self.play(Transform(volab, Tex(r"$A(V_{R_i}$").scale(.6).move_to(volab.get_center())))
        vieq = Tex(r"$V_{R_i} = \frac{R_i}{R_i+R_s}V_s$").scale(.75).next_to(title, DOWN, buff=.2).to_edge(RIGHT)
        voeq = Tex(r"$V_{R_L} = AV_{R_i}\frac{R_L}{R_L+R_o}$").scale(.75).next_to(vieq, DOWN, buff=.2).to_edge(RIGHT)
        voeq2 = Tex(r"$V_{R_L} = A \frac{R_i}{R_i+R_s}V_s\frac{R_L}{R_L+R_o}$").scale(.75).next_to(voeq, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(vieq))
        self.wait()
        self.play(Write(voeq))
        self.wait()
        self.play(Write(voeq2))
        self.wait()
        self.next_slide()
        consider = Tex("Consider $R_i >> R_s$ and $R_o << R_L$:").scale(.75).next_to(voeq2, DOWN, buff=.2).to_edge(RIGHT)
        then = Tex("$V_{R_L} = A(1)V_s(1) = AV_s$").scale(.75).next_to(consider, DOWN, buff=.2).to_edge(RIGHT)
        self.play(Write(consider))
        self.wait()
        self.play(Write(then))
        self.wait()

        self.next_slide()

        self.play(Transform(vieq, Tex(r"$V_{R_L} = AV_s$").scale(.75).move_to(vieq)))
        gone = [voeq, voeq2, consider, then]
        self.play(*[FadeOut(mob) for mob in gone])
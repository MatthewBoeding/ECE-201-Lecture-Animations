from manim import *
from manim_circuit import *
from manim_slides import Slide


class TheveninNorton(Slide):
    def construct(self):
        vo = VoltageSource("48", dependent = False)
        r1 = Resistor("12k").shift(UP*1.5+RIGHT*1.25)
        r2 = Resistor("4k", LEFT).rotate(DEGREES*-90).shift(RIGHT*2.5)
        r3 = Resistor("8k").shift(UP*1.5+RIGHT*3.75)
        r4 = Resistor(" ").rotate(DEGREES*-90).shift(RIGHT*5)
        r4arr = Arrow(start=r4.get_terminals("right")+[-.5,-.3,0], end=r4.get_terminals("left")+[.5,.3,0])
        r4.remove(r4.label)
        r4lab = Tex(r"$R_L$").scale(.6).next_to(r4, RIGHT,buff=.2)

        circ = Circuit().add(vo,r1,r2,r3,r4,r4arr,r4lab)
        circ.add_wire(vo.get_terminals("positive"),r1.get_terminals("left"))
        circ.add_wire(r1.get_terminals("right"),r3.get_terminals("left"))
        circ.add_wire(r3.get_terminals("right"),r4.get_terminals("left"), invert=True)
        circ.add_wire(r2.get_terminals("left"), r3.get_terminals("left"))
        yval = (vo.get_terminals("negative")+[0,-.5,0])*[0,1,0]
        circ.add_wire(vo.get_terminals("negative"), vo.get_terminals("negative")+[0,-.5,0])
        circ.add_wire(r2.get_terminals("right"), (r2.get_terminals("right")*[1,0,1])+yval)
        circ.add_wire(r4.get_terminals("right"), (r4.get_terminals("right")*[1,0,1])+yval)
        circ.add_wire(vo.get_terminals("negative")+[0,-.5,0], (r4.get_terminals("right")*[1,0,1])+yval)
        title = Tex(r"Thevenin and Norton Equivalents").to_edge(UP)
        self.add(title)
        circ.scale(.8).to_edge(LEFT)
        self.play(Create(circ))

        self.wait()
        self.next_slide()

        text2 = Tex(r"Based off same properties of linearity:").scale(.8).next_to(title,DOWN, buff=.2)
        self.play(Write(text2))
        self.wait()
        circ2 = Circuit()
        v2 = VoltageSource(" ", dependent = False)
        v2.remove(v2.label)
        v2lab = Tex(r"$V_{TH}$").scale(.6).next_to(v2, LEFT, buff=.2)
        rth = Resistor(" ").shift(UP*1.5+RIGHT*1)
        rth.remove(rth.label)
        rthlab = Tex(r"$R_{TH}$").scale(.6).next_to(rth, UP, buff=.2)
        rl = Resistor(" ").rotate(DEGREES*-90).shift(RIGHT*2)
        rlarr = Arrow(start=rl.get_terminals("right")+[-.5,-.3,0], end=rl.get_terminals("left")+[.5,.3,0])
        rl.remove(rl.label)
        rllab = Tex(r"$R_L$").scale(.6).next_to(rl, RIGHT,buff=.2)

        circ2.add(v2, v2lab, rth, rthlab, rl, rlarr, rllab)
        
        circ2.add_wire(v2.get_terminals("positive"), rth.get_terminals("left"))
        circ2.add_wire(rl.get_terminals("left"), rth.get_terminals("right"))
        yval = (v2.get_terminals("negative")+[0,-.5,0])*[0,1,0]
        circ2.add_wire(v2.get_terminals("negative"), v2.get_terminals("negative")+[0,-.5,0])
        circ2.add_wire(rl.get_terminals("right"), (rl.get_terminals("right")*[1,0,1])+yval)
        circ2.add_wire(v2.get_terminals("negative")+[0,-.5,0], (rl.get_terminals("right")*[1,0,1])+yval)
        circ2.scale(.8).to_edge(RIGHT)
        arr = Arrow(start = [0,0,0], end = [3,0,0]).next_to(circ, RIGHT, buff=.5)
        self.play(Create(arr), Create(circ2))

        self.next_slide()

        self.play(FadeOut(arr), FadeOut(circ2), circ.animate.to_edge(RIGHT))
        self.wait()
        self.play(Transform(text2, Tex(r"1. Find Thevenin Resistance").scale(.8).next_to(title,DOWN,buff=.2).to_edge(LEFT)))
        texta = Tex(r"a. Turn off independent sources.").scale(.7).next_to(text2, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(texta))
        self.wait()
        lin = Line(vo.get_terminals("positive"), vo.get_terminals("negative"))
        self.play(FadeOut(vo), FadeIn(lin))

        self.next_slide()
        textb = Tex(r"b. Determine resistance seen at $R_L$").scale(.7).next_to(texta, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(textb))
        self.wait()
        arr2 = Arrow(r4.get_center()-[.5,0,0], r4.get_center()+[.5,0,0])
        arr2.set_z_index(1)
        rthlab2 = Tex(r"$R_{TH}$").scale(.6).next_to(arr2, UP, buff=.2)
        self.play(Create(arr2), Create(rthlab2), Create(arr2), FadeOut(r4), FadeOut(r4arr), FadeOut(r4lab))
        self.next_slide()
        
        rthval = Tex(r"$8k + (12k \vert \vert 4k) = 11k\Omega$").scale(.7).next_to(textb,DOWN,buff=.2)
        self.play(Write(rthval))
        
        self.next_slide()

        self.play(Transform(text2, Tex(r"$R_{TH} = 11k\Omega$").scale(.7).next_to(title,DOWN,buff=.2).to_edge(LEFT)),FadeOut(texta), FadeOut(textb), FadeOut(rthval))
        self.wait()
        texta = Tex(r"Find Open Circuit Voltage").scale(.8).next_to(text2, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(texta))
        self.play(Transform(rthlab2, Tex(r"$V_{OC}$").scale(.6).next_to(arr2, UP, buff=.2)), FadeOut(lin), FadeIn(vo))

        self.next_slide()

        textb = Tex(r"$V_{OC} = V_{4k}$\\$V_{4k} = 48V\frac{4k}{4k+12k} = 12V$").scale(.7).next_to(texta,DOWN,buff=.2).to_edge(LEFT)
        self.play(Write(textb))
        
        self.next_slide()
        self.play(Transform(texta, Tex(r"$V_{4k} = 48V\frac{4k}{4k+12k} = 12V$").move_to(texta.get_center())), FadeOut(textb))
        self.wait()
        self.play(FadeOut(circ), FadeOut(rthlab2), FadeOut(arr2))
        self.play(FadeIn(circ2))
        self.play(Transform(v2lab, Tex(r"$12V$").scale(.6).next_to(v2, LEFT, buff=.2)))
        self.play(Transform(rthlab, Tex(r"$11k\Omega$").scale(.6).next_to(rth, UP, buff=.2)))
        
        self.next_slide()
        self.play(FadeOut(texta), FadeOut(textb), FadeOut(text2))
        textq = Tex(r"$R_{TH} = \frac{V_{OC}}{I_N}$").next_to(title,DOWN,buff=.2).to_edge(LEFT)
        self.play(Write(textq))

        circ3 = Circuit()
        io = CurrentSource(" ", dependent=False)
        io.remove(io.label)
        iolab = Tex(r"$I_N$").scale(.6).next_to(io, RIGHT, buff=.2)
        rn = Resistor(" ").rotate(DEGREES*-90).shift(RIGHT*1.5)
        rn.remove(rn.label)
        rnlab = Tex(r"$R_{TH}$").scale(.6).next_to(rn, RIGHT, buff=.2)
        rln = Resistor(" ").rotate(DEGREES*-90).shift(RIGHT*3)
        rln.remove(rln.label)
        rlnlab = Tex(r"$R_{L}$").scale(.6).next_to(rln, RIGHT, buff=.2)

        circ3.add(io,rn,rln,rnlab,rlnlab).to_edge(LEFT)

        circ3.add_wire(io.get_terminals("positive"), rn.get_terminals("left"))
        circ3.add_wire(io.get_terminals("positive"),rln.get_terminals("left"))
        circ3.add_wire(rln.get_terminals("right"), io.get_terminals("negative"), invert = True)

        self.play(Create(circ3))

        q = Tex(r"$I_N = \frac{12}{11}mA$").next_to(textq, DOWN, buff=.2)
        self.play(Write(q))

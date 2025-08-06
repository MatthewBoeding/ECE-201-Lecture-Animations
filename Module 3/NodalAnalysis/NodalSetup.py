from manim import *
from manim_circuit import *
from manim_slides import Slide

class NodalSetup(Slide):
    def construct(self):
        title = Tex(r"Nodal Analysis").to_edge(UP)
        step1 = Tex(r"$\bullet$ Identify all nodes and reference node (ground)").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        step2 = Tex(r"$\bullet$ Count remaining nodes (N)").next_to(step1, DOWN, buff=.2).to_edge(LEFT)
        step3 = Tex(r"$\bullet$ Count Voltage Sources (M)").next_to(step2, DOWN, buff=.2).to_edge(LEFT)
        step4 = Tex(r"$\bullet$ Complexity C = N-M").next_to(step3, DOWN, buff=.2).to_edge(LEFT)
        step5 = Tex(r"$\bullet$ Solve C simulatneous equations").next_to(step4, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(title))
        self.next_slide()
        self.play(Write(step1))
        self.play(Write(step2))
        self.play(Write(step3))
        self.play(Write(step4))
        self.play(Write(step5))
        self.next_slide()
        self.play(FadeOut(step1),FadeOut(step2),FadeOut(step3),FadeOut(step4),FadeOut(step5))
        # Place the components down first. Then, connect with wires later.
        r9k = Resistor("9k").shift(LEFT * 3.25 + UP)
        r10k = (
            Resistor("10k", direction=RIGHT)
            .rotate(-90 * DEGREES)
            .shift(LEFT * 1.75 + DOWN * 0.5)
        )
        r4k = (
            Resistor("4k", direction=RIGHT)
            .rotate(-90 * DEGREES)
            .shift(RIGHT * 1.25 + DOWN * 0.5)
        )
        r9k = Resistor("9k").shift(RIGHT * 2.75 + UP)

        v12 = VoltageSource(12).shift(LEFT * 5 + DOWN * 0.5)

        # You can rotate the voltage sources and move them.
        r3k1 = Resistor("3k", direction=UP).shift(UP)
        r3k2 = Resistor("3k", direction=LEFT).rotate(-90 * DEGREES).shift(RIGHT * 4 + DOWN * 0.5)
        gnd = Ground(ground_type="ground").shift(LEFT * 5 + DOWN * 2)

        # Add Circuit components.
        circuit = Circuit()
        circuit.add_components(r9k, r10k, r4k, r9k, v12, r3k1, r3k2)
        # A much streamline and easier way to edit.
        
        circuit.add_wire(v12.get_terminals("positive"), r3k1.get_terminals("left"))
        circuit.add_wire(r3k1.get_terminals("left"), r10k.get_terminals("left"), invert = True)
        circuit.add_wire(r3k1.get_terminals("right"), r9k.get_terminals("left"))
        circuit.add_wire(r3k1.get_terminals("right"), r4k.get_terminals("left"), invert = True)
        circuit.add_wire(r9k.get_terminals("right"), r3k2.get_terminals("left"), invert = True)
        circuit.add_wire(r3k2.get_terminals("right"), gnd.get_terminals())
        circuit.add_wire(r4k.get_terminals("right"), gnd.get_terminals())
        circuit.add_wire(r10k.get_terminals("right"), gnd.get_terminals())
        circuit.add_wire(gnd.get_terminals(), v12.get_terminals("negative"))

        self.add(circuit)
        self.wait()
        
        self.next_slide()
        self.play(Write(step1))

        # Automatic node detection
        for node, color in zip(
            circuit.node_list, [GREEN, RED, GREEN, RED]
        ):
            self.play(node.animate.set_color(color))
        self.wait()
        self.play(FadeIn(gnd))
        circuit.node_list[3].set_color(WHITE)
        
        self.next_slide()
        step2.next_to(title,DOWN,buff=.2)
        self.play(FadeOut(step1))
        self.play(Write(step2))
        self.wait()
        nodea = Tex(r"$a$").move_to(r9k.get_terminals("right")+[.75,.5,0])
        nodeb = Tex(r"$b$").move_to(r9k.get_terminals("left")+[-.75,.5,0])
        nodec = Tex(r"$c$").move_to(r3k1.get_terminals("left")+[-1.5,.5,0])
        self.play(Create(nodea), Create(nodeb), Create(nodec))
        
        self.next_slide()
        self.play(FadeOut(step2))
        step3.next_to(title,DOWN,buff=.2)
        self.play(Write(step3))
        vc = Tex(r"$V_c = 12V$").scale(.75).move_to(r3k1.get_terminals("left")+[-1.5,.5,0])
        self.play(Transform(nodec, vc))
        
        self.next_slide()
        circuit.add(gnd)
        grp = VGroup().add(circuit, nodea, nodeb, nodec)
        self.play(grp.animate.scale(.6))
        self.play(grp.animate.to_edge(RIGHT))
        step4.next_to(title,DOWN,buff=0.2)
        self.play(Transform(step3, step4))
        queue = Tex(r"C=3-1=2").next_to(step3, DOWN, buff=0.2).to_edge(LEFT)
        self.play(Write(queue))
        
        self.next_slide()
        step5.next_to(title,DOWN,buff=.2)
        self.play(Transform(step3,step5), FadeOut(queue))
        kcla = Tex(r"KCL Node $V_a$").next_to(step3, DOWN, buff=.2).to_edge(LEFT)
        kcleq = Tex(r"$\frac{V_a - V_b}{9k}+\frac{V_a}{3k} = 0$").scale(.75).next_to(kcla, DOWN, buff=.2).to_edge(LEFT)
        kclaeq = Tex(r"$\frac{V_a - V_b}{9k}+\frac{3V_a}{9k} = 0$").scale(.75).next_to(kcleq, DOWN, buff=.2).to_edge(LEFT)
        kclaeq2 = Tex(r"$4V_a = V_b$").scale(.75).next_to(kclaeq, DOWN, buff=.2).to_edge(LEFT)

        self.play(Write(kcla))
        self.play(Write(kcleq))
        self.play(Write(kclaeq))
        self.play(Write(kclaeq2))

        self.next_slide()
        self.play(FadeOut(kcla),FadeOut(kcleq),FadeOut(kclaeq))
        self.play(kclaeq2.animate.next_to(kcla,DOWN,buff=-0.5))
        kclb = Tex(r"KCL Node $V_b$").next_to(kclaeq2, DOWN, buff=.2).to_edge(LEFT)
        kcleq2 = Tex(r"$\frac{V_b - 12v}{3k}+\frac{V_b-V_a}{9k} + \frac{V_b}{4k} = 0$").scale(.75).next_to(kclb, DOWN, buff=.2).to_edge(LEFT)
        kcleq3 = Tex(r"$\frac{12V_b - 144v}{36k}+\frac{4V_b-4V_a}{36k} + \frac{9V_b}{36k} = 0$").scale(.75).next_to(kcleq2, DOWN, buff=.2).to_edge(LEFT)
        kcleq4 = Tex(r"$12V_b + 9V_b + 4V_b-4V_a = 144v$").scale(.75).next_to(kcleq3, DOWN, buff=.2).to_edge(LEFT)
        kcleq5 = MathTex(r"24V_b = 144V \implies V_b = 6V").scale(.75).next_to(kcleq4, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(kclb))
        self.play(Write(kcleq2))
        self.play(Write(kcleq3))
        self.play(Write(kcleq4))
        self.play(Write(kcleq5))

        self.next_slide()
        self.play( *[FadeOut(mob)for mob in self.mobjects])
        # Place the components down first. Then, connect with wires later.
        title = Tex(r"Supernodes").to_edge(UP)
        self.play(Write(title))

        r270 = Resistor("2.5k").shift(LEFT * 3.25 + UP)
        r10000 = (
            Resistor("10k", direction=RIGHT)
            .rotate(90 * DEGREES)
            .shift(LEFT * 1.75 + DOWN * 0.5)
        )
        r1100 = Resistor("1k", direction=DOWN).shift(DOWN * 2 + LEFT * 0.25)
        r620 = (
            Resistor("5k", direction=RIGHT)
            .rotate(90 * DEGREES)
            .shift(RIGHT * 1.25 + DOWN * 0.5)
        )
        r430 = Resistor("2.5k").shift(RIGHT * 2.75 + UP)
        r360 = (
            Resistor("1.25k", direction=LEFT)
            .shift(RIGHT * 6 + DOWN * 0.5)
            .rotate(90 * DEGREES)
        )
        r5600 = Resistor("5k").shift(UP * 3)
        v20 = VoltageSource(20).shift(LEFT * 5 + DOWN * 0.5)

        # You can rotate the voltage sources and move them.
        v10 = VoltageSource(10, direction=UP).rotate(-90 * DEGREES).shift(UP)
        v16 = VoltageSource(16, direction=LEFT).shift(RIGHT * 4 + DOWN * 0.5)
        gnd = Ground(ground_type="ground").shift(LEFT * 5 + DOWN * 2)

        # Add Circuit components.
        circuit = Circuit()
        circuit.add_components(v20, v16, v10, r270, r10000, r1100, r620, r430, r360, r5600,gnd)

        # A much streamline and easier way to edit.
        circuit.add_wire(gnd.get_terminals(), v20.get_terminals("negative"))
        circuit.add_wire(v20.get_terminals("negative"), r1100.get_terminals("left"))
        circuit.add_wire(r10000.get_terminals("left"), r1100.get_terminals("left"))
        circuit.add_wire(v20.get_terminals("positive"), r5600.get_terminals("left"))
        circuit.add_wire(v20.get_terminals("positive"), r270.get_terminals("left"))
        circuit.add_wire(r10000.get_terminals("right"), r270.get_terminals("right"))
        circuit.add_wire(r10000.get_terminals("right"), v10.get_terminals("negative"))
        circuit.add_wire(r620.get_terminals("right"), v10.get_terminals("positive"))

        # you can invert the direction of the wire. Vertical first, or horizontal first.
        circuit.add_wire(r430.get_terminals("left"), r620.get_terminals("right"), invert=True)
        circuit.add_wire(r1100.get_terminals("right"),r360.get_terminals("left"), invert=True)
        circuit.add_wire(v16.get_terminals("negative"),r1100.get_terminals("right"))

        # You can also custom define wires to have better control with how the junctions are generated
        circuit.add_wire(r620.get_terminals("left"), r620.get_terminals("left") + DOWN*(r620.get_terminals("left")[1] - r1100.get_terminals("right")), invert=True)

        # The order in which the wires are added matters.
        circuit.add_wire(r5600.get_terminals("right"), r360.get_terminals("right"), invert=True)
        circuit.add_wire(r430.get_terminals("right"), r360.get_terminals("right"), invert=True)
        circuit.add_wire(v16.get_terminals("positive"), r430.get_terminals("right"))
        circuit.scale(.8)

        self.play(FadeIn(circuit),FadeOut(gnd))
        self.wait()

        self.next_slide()
        # Automatic node detection
        for node, color in zip(
            circuit.node_list, [BLUE, RED, ORANGE, YELLOW, GREEN, PURPLE]
        ):
            self.play(node.animate.set_color(color))
        self.wait()

        self.next_slide()
        coords = gnd.get_terminals()
        gnd = Ground(ground_type="ground").scale(.8).move_to(coords+[0,-.5,0])
        lin = Line(gnd.get_terminals(), v20.get_terminals("negative"))
        self.play(FadeIn(gnd),FadeIn(lin))
        self.play(circuit.node_list[0].animate.set_color(WHITE))
        circuit.add(gnd, lin)

        self.next_slide()
        self.play(circuit.animate.scale(.75))
        self.play(circuit.animate.to_edge(RIGHT))
        step1 = Tex(r"$\bullet$ Identify all nodes and reference node (ground)").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(step1))
        nodea = Tex(r"$a$").scale(.65).next_to(r270, UP, buff = .02).shift(LEFT*1.5)
        nodeb = Tex(r"$b$").scale(.65).next_to(r270, UP, buff = .02).shift(RIGHT*.75)
        nodec = Tex(r"$c$").scale(.65).next_to(r430, UP, buff = .02).shift(LEFT*.75)
        noded = Tex(r"$d$").scale(.65).next_to(r430, UP, buff = .02).shift(RIGHT*.75)
        nodee = Tex(r"$e$").scale(.65).next_to(r1100, UP, buff = .02).shift(RIGHT*1.5)
        self.next_slide()

        

        step2 = Tex(r"$\bullet$ Count remaining nodes (N)").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(Transform(step1, step2))
        self.play(Create(nodea), Create(nodeb),Create(nodec),Create(noded),Create(nodee))
        nodes = Tex(r"$N=5$").next_to(step2, DOWN, buff = .2).to_edge(LEFT)
        self.play(Write(nodes))

        self.next_slide()

        step3 = Tex(r"$\bullet$ Count Voltage Sources (M)").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(Transform(step1, step3))
        supps = Tex(r"$M=3$").next_to(nodes, DOWN, buff = .2).to_edge(LEFT)
        self.play(Write(supps))

        self.next_slide()
        step4 = Tex(r"$\bullet$ Complexity C = N-M").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(Transform(step1, step4))
        comp = Tex(r"$ C = 5-3 = 2$").next_to(supps, DOWN, buff = .2).to_edge(LEFT)
        self.play(Write(comp))
        
        self.next_slide()

        step5 = Tex(r"$\bullet$ Solve C simulatneous equations").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        self.play(Transform(step1, step5))
        self.play(Transform(nodea, Tex(r"$V_a=20V$").scale(.5).move_to(nodea.get_center()+[-.5,0,0])))
        self.play(FadeOut(nodes), FadeOut(supps), comp.animate.next_to(step1, DOWN, buff=.2))
        for node, color in zip(
            circuit.node_list, [BLUE, RED, ORANGE, YELLOW, GREEN, PURPLE]
        ):
           node.set_color(WHITE)
        
        dist = v10.get_terminals("negative") - v10.get_terminals("positive")
        cent = v10.get_center()
        circ = Circle(radius=dist[0]).move_to(cent)
        dist16 = v16.get_terminals("positive") - v16.get_terminals("negative")
        cent16 = v16.get_center()
        circ16 = Circle(radius=dist16[1]).move_to(cent16)

        self.play(Create(circ), Create(circ16))
        self.next_slide()

        supernode = Tex(r"Supernodes! Source between 2\\ nodes without reference").scale(.6).next_to(comp, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(supernode))
        vc = Tex(r"$V_{cb} = 10V$").scale(.75).next_to(supernode, DOWN, buff=.2).to_edge(LEFT)
        vc2 = Tex(r"$V_c - V_b = 10V$").scale(.75).next_to(vc, DOWN, buff=.2).to_edge(LEFT)
        vc3 = Tex(r"$V_c = V_b + 10V$").scale(.75).next_to(vc2, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(vc))
        self.play(Write(vc2))
        self.play(Write(vc3))

        self.next_slide()
        self.play(Transform(nodec, Tex(r"$V_b + 10V$").scale(.5).move_to(nodec.get_center()+[.25,.25,0])), FadeOut(circ))

        self.next_slide()
        vd = Tex(r"Likewise: $V_d = V_e + 16V$").scale(.75).next_to(vc3, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(vd))
        self.play(Transform(noded, Tex(r"$V_e + 16V$").scale(.5).move_to(noded.get_center()+[.5,.25,0])), FadeOut(circ16))

        self.next_slide()
        self.play(FadeOut(step1), FadeOut(comp),FadeOut(vd), FadeOut(vc), FadeOut(vc2), FadeOut(vc3), FadeOut(supernode))
        snode1 = Tex(r"KCL at Supernode $b$:").next_to(title, DOWN, buff=.2).to_edge(LEFT)
        snode2 = Tex(r"$\frac{V_b-20V}{2.5k} + \frac{V_b}{10k} + \frac{V_b+10V-V_e}{5k} + \frac{V_b+10V - (V_e+16V)}{2.5k}=0$").scale(.5).next_to(snode1, DOWN, buff=.2).to_edge(LEFT)
        snode3 = Tex(r"$11V_b - 6V_e = -84V$").scale(.6).next_to(snode2, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(snode1))
        self.play(Write(snode2))
        self.play(Write(snode3))
        
        self.next_slide()
        self.play(FadeOut(snode1), FadeOut(snode2), snode3.animate.move_to(snode1.get_center()))
        enode =  Tex(r"KCL at Supernode $e$:").next_to(snode3, DOWN, buff=.2).to_edge(LEFT)
        enode2 = Tex(r"$\frac{V_e+16V-20V}{5k} + \frac{V_e+16V - (V_b+10V)}{2.5k} + \frac{V_e+16V-V_e}{1.25k} + \frac{V_e}{1k} = 0 $").scale(.5).next_to(enode, DOWN, buff=.2).to_edge(LEFT)
        enode3 = Tex(r"$8V_e - 2V_b = -72V$").scale(.6).next_to(enode2, DOWN, buff=.2).to_edge(LEFT)
        self.play(Write(enode))
        self.play(Write(enode2))
        self.play(Write(enode3))

        self.next_slide()
        self.play(FadeOut(enode), FadeOut(enode2), enode3.animate.move_to(enode.get_center()))
        self.play(Write(Tex(r"$V_b = \frac{276}{19}V \quad V_e = \frac{240}{19}V$").scale(.75).next_to(enode3, DOWN, buff=.2).to_edge(LEFT)))

        
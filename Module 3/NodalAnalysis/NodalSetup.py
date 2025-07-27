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
        self.add(title)
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
        grp = VGroup().add(circuit, nodea, nodeb, nodec).scale(.6).to_edge(RIGHT)
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

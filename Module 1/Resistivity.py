from manim import *
from manim_slides import Slide

class Resistivity(Slide):
    def construct(self):
        # === Slide 1: Title and Equation ===
        title = Tex("Resistivity", color=YELLOW).scale(1.2).to_edge(UP)
        self.play(Write(title))

        equation = MathTex(r"R = \rho \cdot \frac{L}{A}").scale(1).next_to(title, DOWN, buff=1)
        self.play(Write(equation))
        self.wait()

        desc = VGroup(
            Tex(r"$R$: Resistance (Ohms)").scale(0.6),
            Tex(r"$\rho$: Resistivity of material").scale(0.6),
            Tex(r"$L$: Length of conductor").scale(0.6),
            Tex(r"$A$: Cross-sectional area").scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(equation, DOWN, buff=1)

        self.play(LaggedStartMap(Write, desc, lag_ratio=0.2))
        self.wait()
        self.next_slide()

        # === Slide 2: Visualize a conductor ===
        # Draw a rectangular conductor
        conductor = Rectangle(width=4, height=1, color=WHITE).shift(LEFT * 2)
        label_L = MathTex("L").scale(0.6).next_to(conductor, DOWN)
        label_A = MathTex("A").scale(0.6).rotate(PI/2).next_to(conductor, LEFT)

        self.play(Create(conductor), Write(label_L), Write(label_A))

        # Arrows showing length and area
        arrow_L = DoubleArrow(conductor.get_left() + DOWN * 0.8, conductor.get_right() + DOWN * 0.8, buff=0)
        arrow_A = DoubleArrow(conductor.get_left() + LEFT * 0.4 + DOWN * 0.5,
                              conductor.get_left() + LEFT * 0.4 + UP * 0.5, buff=0)
        self.play(GrowArrow(arrow_L), GrowArrow(arrow_A))
        self.wait()

        # Add text: "Same material, longer wire => higher resistance"
        example1 = Tex("Longer wire → higher $R$").scale(0.5).to_corner(UR)
        self.play(Write(example1))
        self.wait()

        # Change length
        long_conductor = Rectangle(width=6, height=1, color=WHITE).shift(LEFT * 2)
        self.play(Transform(conductor, long_conductor), Transform(arrow_L, DoubleArrow(
            long_conductor.get_left() + DOWN * 0.8,
            long_conductor.get_right() + DOWN * 0.8, buff=0)))
        self.wait()

        self.next_slide()

        # === Slide 3: Area effect ===
        # Reset to short but wide conductor
        short_wide_conductor = Rectangle(width=4, height=2, color=WHITE).shift(LEFT * 2)
        self.play(Transform(conductor, short_wide_conductor))

        new_arrow_A = DoubleArrow(
            short_wide_conductor.get_left() + LEFT * 0.4 + DOWN,
            short_wide_conductor.get_left() + LEFT * 0.4 + UP, buff=0)
        self.play(Transform(arrow_A, new_arrow_A))

        # Update annotation
        self.play(FadeOut(example1))
        example2 = Tex("Larger area → lower $R$").scale(0.5).to_corner(UR)
        self.play(Write(example2))
        self.wait()

        self.next_slide()

        # === Final Summary Slide ===
        summary_box = VGroup(
            Tex("Summary:").scale(0.8).set_color(YELLOW),
            Tex(r"$R = \rho \cdot \frac{L}{A}$").scale(0.8),
            Tex("↑ Length → ↑ Resistance").scale(0.6),
            Tex("↑ Area → ↓ Resistance").scale(0.6),
            Tex("Depends on material via $\\rho$").scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)

        self.play(FadeOut(conductor, arrow_L, arrow_A, label_L, label_A, example2))
        self.play(Write(summary_box))
        self.wait(2)
        self.show_real_world_example()

    def show_real_world_example(self):
        # === Title ===
        title = Tex("Real-World Example: Copper vs Nichrome").scale(0.8).to_edge(UP)
        self.play(Write(title))

        # === Two wires ===
        copper_wire = Rectangle(width=3, height=0.5, fill_color=BLUE_E, fill_opacity=0.6).shift(LEFT * 3)
        nichrome_wire = Rectangle(width=3, height=0.5, fill_color=RED_E, fill_opacity=0.6).shift(RIGHT * 3)

        copper_label = Tex("Copper").scale(0.5).next_to(copper_wire, DOWN)
        nichrome_label = Tex("Nichrome").scale(0.5).next_to(nichrome_wire, DOWN)

        self.play(FadeIn(copper_wire, nichrome_wire), Write(copper_label), Write(nichrome_label))

        # === Annotate resistivity values ===
        rho_cu = Tex(r"$\rho_{Cu} \approx 1.7 \times 10^{-8} \, \Omega \cdot m$").scale(0.5).next_to(copper_wire, UP)
        rho_n = Tex(r"$\rho_{Nichrome} \approx 1.1 \times 10^{-6} \, \Omega \cdot m$").scale(0.5).next_to(nichrome_wire, UP)

        self.play(Write(rho_cu), Write(rho_n))
        self.wait(1)

        # === Resistance arrows ===
        r_cu = Arrow(start=copper_wire.get_right(), end=copper_wire.get_right() + RIGHT * 1, color=BLUE)
        r_n = Arrow(start=nichrome_wire.get_right(), end=nichrome_wire.get_right() + RIGHT * 3, color=RED)

        r_cu_label = Tex("Low $R$").scale(0.5).next_to(r_cu, RIGHT)
        r_n_label = Tex("High $R$").scale(0.5).next_to(r_n, RIGHT)

        self.play(GrowArrow(r_cu), GrowArrow(r_n), Write(r_cu_label), Write(r_n_label))

        # === Usage examples ===
        usage_text = VGroup(
            Tex("Copper: used for electrical wiring").scale(0.5),
            Tex("Nichrome: used in heating elements").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(DOWN)

        self.play(Write(usage_text))
        self.wait(2)

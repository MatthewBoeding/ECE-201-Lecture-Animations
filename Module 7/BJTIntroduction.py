from manim import *
from manim_slides import Slide
class BJTIntroduction(Slide):
    def construct(self):
        self.show_npn()
        self.next_slide()

        self.show_npn_carrier_flow()
        self.next_slide()

        self.clear()
        self.show_pnp()
        self.next_slide()

        self.show_pnp_carrier_flow()
        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.show_npn_beta_slider()

    def show_npn(self):
        title = Tex(r"NPN BJT").to_edge(UP)
        self.play(Write(title))
        self.next_slide()
        # === Internal Layers ===
        n_left = Rectangle(width=1.2, height=1.5, color=WHITE, fill_color=GRAY, fill_opacity=0.5).shift(LEFT * 2)
        p_mid = Rectangle(width=1.2, height=1.5, color=WHITE, fill_color=RED, fill_opacity=0.5).next_to(n_left, RIGHT, buff=0)
        n_right = Rectangle(width=1.2, height=1.5, color=WHITE, fill_color=GRAY, fill_opacity=0.5).next_to(p_mid, RIGHT, buff=0)

        emitter_label = Tex("Collector").scale(0.5).next_to(n_left, LEFT)
        collector_label = Tex("Emitter").scale(0.5).next_to(n_right, RIGHT)
        base_label = Tex("Base").scale(0.5).next_to(p_mid, DOWN)

        letters = VGroup(
            Tex("N").move_to(n_left.get_center()),
            Tex("P").move_to(p_mid.get_center()),
            Tex("N").move_to(n_right.get_center())
        )

        layers = VGroup(n_left, p_mid, n_right, emitter_label, collector_label, base_label, letters).shift(LEFT * 2)

        # === NPN Symbol ===
        circle = Circle(radius=0.8).shift(RIGHT * 3)
        base = Line(circle.get_left(), circle.get_center()-[.4,0,0])
        lin = Line(circle.get_center()-[.4,.5,0], circle.get_center()-[.4,-.5,0])
        collector = Line(circle.get_top()-[0,.1,0], circle.get_center()-[.4,-.25,0])
        col2 = Line(circle.get_top()-[0,.1,0], circle.get_top())
        emitter = Line(circle.get_bottom()+[0,.1,0], circle.get_center()-[.4,.25,0])
        em2 = Line(circle.get_bottom()+[0,.1,0], circle.get_bottom())
        arrow = Arrow(start=emitter.get_end(), end=emitter.get_start(), buff=0, stroke_width=2).scale(0.8)

        symbol_labels = VGroup(
            Tex("Base").scale(0.4).next_to(base.get_start(), LEFT),
            Tex("Collector").scale(0.4).next_to(collector.get_start(), UP),
            Tex("Emitter").scale(0.4).next_to(emitter.get_start(), DOWN),
            Tex("NPN").scale(0.5).move_to(circle.get_center())
        )

        npn_symbol = VGroup(circle, base, collector, emitter, arrow, symbol_labels, lin, col2, em2)

        # === Description ===
        desc = Tex(
            r"An NPN transistor consists of a P-doped semiconductor",
            r"between two N-doped layers."
        ).scale(0.5).next_to(title, DOWN, buff=.2)

        # === Show ===
        self.play(FadeIn(layers), FadeIn(npn_symbol), Write(desc))

    def show_pnp(self):
        title = Tex(r"PNP BJT").to_edge(UP)
        self.play(Write(title))
        # === Internal Layers ===
        p_left = Rectangle(width=1.2, height=1.5, color=WHITE, fill_color=RED, fill_opacity=0.5).shift(LEFT * 2)
        n_mid = Rectangle(width=1.2, height=1.5, color=WHITE, fill_color=GRAY, fill_opacity=0.5).next_to(p_left, RIGHT, buff=0)
        p_right = Rectangle(width=1.2, height=1.5, color=WHITE, fill_color=RED, fill_opacity=0.5).next_to(n_mid, RIGHT, buff=0)

        emitter_label = Tex("Emitter").scale(0.5).next_to(p_left, LEFT)
        collector_label = Tex("Collector").scale(0.5).next_to(p_right, RIGHT)
        base_label = Tex("Base").scale(0.5).next_to(n_mid, DOWN)

        letters = VGroup(
            Tex("P").move_to(p_left.get_center()),
            Tex("N").move_to(n_mid.get_center()),
            Tex("P").move_to(p_right.get_center())
        )

        layers = VGroup(p_left, n_mid, p_right, emitter_label, collector_label, base_label, letters).shift(LEFT * 2)

        # === PNP Symbol ===
        circle = Circle(radius=0.8).shift(RIGHT * 3)
        base = Line(circle.get_left(), circle.get_center()-[.4,0,0])
        lin = Line(circle.get_center()-[.4,.5,0], circle.get_center()-[.4,-.5,0])
        emitter = Line(circle.get_top()-[0,.1,0], circle.get_center()-[.4,-.25,0])
        em2 = Line(circle.get_top()-[0,.1,0], circle.get_top())
        collector = Line(circle.get_bottom()+[0,.1,0], circle.get_center()-[.4,.25,0])
        col2 = Line(circle.get_bottom()+[0,.1,0], circle.get_bottom())
        arrow = Arrow(start=emitter.get_start(), end=emitter.get_end(), buff=0, stroke_width=2).scale(0.8)

        symbol_labels = VGroup(
            Tex("Base").scale(0.4).next_to(base.get_start(), LEFT),
            Tex("Collector").scale(0.4).next_to(collector.get_end(), DOWN, buff=.75),
            Tex("Emitter").scale(0.4).next_to(emitter.get_end(), UP, buff=.75),
            Tex("PNP").scale(0.5).move_to(circle.get_center())
        )

        pnp_symbol = VGroup(circle, base, collector, emitter, arrow, symbol_labels, col2, em2, lin)

        # === Description ===
        desc = Tex(
            r"A PNP transistor contains an N-doped layer",
            r"between two layers of P-doped material."
        ).scale(0.5).next_to(title, DOWN, buff=.2)

        # === Show ===
        self.play(FadeIn(layers), FadeIn(pnp_symbol), Write(desc))
    def show_npn_carrier_flow(self):
        # === NPN structure again ===
        n_left = Rectangle(width=1.2, height=1.5, fill_color=GRAY, fill_opacity=0.5).shift(LEFT * 2)
        p_mid = Rectangle(width=1.2, height=1.5, fill_color=RED, fill_opacity=0.5).next_to(n_left, RIGHT, buff=0)
        n_right = Rectangle(width=1.2, height=1.5, fill_color=GRAY, fill_opacity=0.5).next_to(p_mid, RIGHT, buff=0)

        # Depletion regions
        depletion1 = Rectangle(width=0.2, height=1.5, fill_color=YELLOW, fill_opacity=0.3, stroke_opacity=0).move_to(n_left.get_right() + RIGHT * 0.1)
        depletion2 = Rectangle(width=0.2, height=1.5, fill_color=YELLOW, fill_opacity=0.3, stroke_opacity=0).move_to(p_mid.get_right() + RIGHT * 0.1)

        structure = VGroup(n_left, p_mid, n_right, depletion1, depletion2).shift(LEFT * 2)

        self.play(FadeIn(structure))

        # === Electrons ===
        electrons = VGroup()
        for y in np.linspace(-0.6, 0.6, 5):
            dot = Dot(color=BLUE).scale(0.3).move_to(n_left.get_left() + RIGHT * 0.3 + UP * y)
            electrons.add(dot)

        self.play(FadeIn(electrons))

        # === Animate electrons across layers ===
        self.play(*[dot.animate.shift(RIGHT * 2.5) for dot in electrons], run_time=1.5)

        self.wait(1)

    def show_pnp_carrier_flow(self):
        # === PNP structure again ===
        p_left = Rectangle(width=1.2, height=1.5, fill_color=RED, fill_opacity=0.5).shift(LEFT * 2)
        n_mid = Rectangle(width=1.2, height=1.5, fill_color=GRAY, fill_opacity=0.5).next_to(p_left, RIGHT, buff=0)
        p_right = Rectangle(width=1.2, height=1.5, fill_color=RED, fill_opacity=0.5).next_to(n_mid, RIGHT, buff=0)

        # Depletion regions
        depletion1 = Rectangle(width=0.2, height=1.5, fill_color=YELLOW, fill_opacity=0.3, stroke_opacity=0).move_to(p_left.get_right() + RIGHT * 0.1)
        depletion2 = Rectangle(width=0.2, height=1.5, fill_color=YELLOW, fill_opacity=0.3, stroke_opacity=0).move_to(n_mid.get_right() + RIGHT * 0.1)

        structure = VGroup(p_left, n_mid, p_right, depletion1, depletion2).shift(LEFT * 2)

        self.play(FadeIn(structure))

        # === Holes ===
        holes = VGroup()
        for y in np.linspace(-0.6, 0.6, 5):
            dot = Dot(color=RED).scale(0.3).move_to(p_left.get_left() + RIGHT * 0.3 + UP * y)
            holes.add(dot)

        self.play(FadeIn(holes))

        self.play(*[dot.animate.shift(RIGHT * 2.5) for dot in holes], run_time=1.5)

        self.wait(1)

    def show_npn_beta_slider(self):
        # === NPN simplified structure ===
        title = Tex(r"BJT Current Gain").to_edge(UP)
        self.play(Write(title))
        emitter = Rectangle(width=1.5, height=1.5, fill_color=GRAY, fill_opacity=0.5).shift(LEFT * 3)
        base = Rectangle(width=0.8, height=1.5, fill_color=RED, fill_opacity=0.5).next_to(emitter, RIGHT, buff=0)
        collector = Rectangle(width=1.5, height=1.5, fill_color=GRAY, fill_opacity=0.5).next_to(base, RIGHT, buff=0)
        letters = VGroup(
            Tex("N").move_to(emitter.get_center()),
            Tex("P").move_to(base.get_center()),
            Tex("N").move_to(collector.get_center())
        )
        structure = VGroup(emitter, base, collector, letters)
        self.play(FadeIn(structure))

        # === β Tracker ===
        beta_tracker = ValueTracker(20)

        # === Base current arrow (fixed) ===
        ib_arrow = Arrow(UP, DOWN, color=YELLOW).scale(0.6).next_to(base, UP, buff=0.2)
        ib_label = MathTex("I_b").scale(0.6).next_to(ib_arrow, LEFT)
        ib_group = VGroup(ib_arrow, ib_label)

        # === Collector current arrow (dynamic) ===
        def get_ic_arrow():
            height = 0.6 + beta_tracker.get_value() / 40  # scales with beta
            return Arrow(LEFT, RIGHT, color=BLUE).scale(height).next_to(base, DOWN, buff=0.2)

        ic_arrow = always_redraw(get_ic_arrow)
        ic_label = always_redraw(lambda: MathTex("I_c").scale(0.6).next_to(ic_arrow, DOWN))
        ic_group = VGroup(ic_arrow, ic_label)

        self.play(GrowArrow(ib_arrow), Write(ib_label))
        self.play(FadeIn(ic_arrow), Write(ic_label))

        # === Equation ===
        eq = MathTex(r"\beta = \frac{I_c}{I_b}").scale(0.75).next_to(title, DOWN, buff=.2)
        self.play(Write(eq))

        # === Slider components ===
        slider_line = Line(LEFT * 1.25, RIGHT * 2).scale(0.5).to_edge(DOWN).shift(UP * 1.5)
        slider_dot = always_redraw(lambda: Dot().move_to(
            slider_line.point_from_proportion((beta_tracker.get_value() - 20) / 80)
        ))
        beta_value_label = always_redraw(lambda: Tex(
            f"\\(\\beta = {int(beta_tracker.get_value())}\\)"
        ).scale(0.6).next_to(slider_line, UP))

        self.play(Create(slider_line), FadeIn(slider_dot), Write(beta_value_label))

        # === Animate changing beta ===
        self.play(beta_tracker.animate.set_value(100), run_time=4, rate_func=linear)
        self.wait()

        # === NEXT SLIDE: Show disappearance of Ib and Ic
        self.next_slide()

        self.play(FadeOut(ib_group))
        self.wait(0.5)
        self.play(FadeOut(ic_group))
        self.wait()

        # Optional conclusion text
        conclusion = Tex(r"No base current $\Rightarrow$ no collector current").scale(0.6).next_to(eq, DOWN, buff=.2)
        self.play(Write(conclusion))
        self.wait(2)


    '''def construct(self):
 # === Regions: Emitter, Base, Collector ===
        emitter = Rectangle(width=2, height=2, color=BLUE).shift(LEFT * 3)
        base = Rectangle(width=1, height=2, color=WHITE).next_to(emitter, RIGHT, buff=0)
        collector = Rectangle(width=2, height=2, color=BLUE).next_to(base, RIGHT, buff=0)

        emitter_label = Tex("Emitter (N)").scale(0.5).next_to(emitter, DOWN)
        base_label = Tex("Base (P)").scale(0.5).next_to(base, DOWN)
        collector_label = Tex("Collector (N)").scale(0.5).next_to(collector, DOWN)

        self.play(FadeIn(emitter, base, collector))
        self.play(Write(emitter_label), Write(base_label), Write(collector_label))

        # === Depletion Regions ===
        depletion_left = Rectangle(width=0.2, height=2, fill_opacity=0.3, fill_color=YELLOW).move_to(emitter.get_right() + RIGHT * 0.1)
        depletion_right = Rectangle(width=0.2, height=2, fill_opacity=0.3, fill_color=YELLOW).move_to(collector.get_left() + LEFT * 0.1)

        self.play(FadeIn(depletion_left, depletion_right))

        # === Electric Field Arrows in Base ===
        field_arrows = VGroup()
        for y in np.linspace(-0.8, 0.8, 5):
            arrow = Arrow(start=LEFT, end=RIGHT, color=WHITE, buff=0).scale(0.3)
            arrow.move_to(base.get_center() + UP * y)
            field_arrows.add(arrow)

        self.play(LaggedStartMap(GrowArrow, field_arrows, lag_ratio=0.1))
        self.wait(1)

        # === Electron Movement from Emitter → Collector ===
        electrons = VGroup()
        for y in np.linspace(-0.8, 0.8, 6):
            e = Dot(radius=0.07, color=BLUE).move_to(emitter.get_left() + RIGHT * 0.2 + UP * y)
            electrons.add(e)

        self.play(FadeIn(electrons))

        # Animate movement through base to collector
        self.play(*[e.animate.shift(RIGHT * 4.5) for e in electrons], run_time=2)
        self.wait(1)

        # === Add title/annotation ===
        note = Tex(r"NPN BJT: Electrons flow from Emitter to Collector through Base").scale(0.6).to_edge(UP)
        self.play(Write(note))
        self.wait(2)
        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        # === Transistor Regions ===
        emitter = Rectangle(width=2, height=2, color=RED).shift(LEFT * 3)
        base = Rectangle(width=1, height=2, color=WHITE).next_to(emitter, RIGHT, buff=0)
        collector = Rectangle(width=2, height=2, color=RED).next_to(base, RIGHT, buff=0)

        self.play(FadeIn(emitter, base, collector))

        # === Labels ===
        self.play(LaggedStart(
            Write(Tex("Emitter (P)").scale(0.5).next_to(emitter, DOWN)),
            Write(Tex("Base (N)").scale(0.5).next_to(base, DOWN)),
            Write(Tex("Collector (P)").scale(0.5).next_to(collector, DOWN)),
            lag_ratio=0.2
        ))

        # === Current Arrows (initial state) ===
        ib_arrow = Arrow(DOWN, UP, color=YELLOW).scale(0.5).next_to(base, UP, buff=0.1)
        ib_label = MathTex("I_b").scale(0.6).next_to(ib_arrow, LEFT, buff=0.1)
        beta_tracker = ValueTracker(20)
        ic_arrow = always_redraw(lambda: Arrow(
            start=collector.get_top(),
            end=collector.get_top() + UP * self.get_ic_length(beta_tracker.get_value()),
            color=BLUE
        ).scale(1).set_stroke(width=4))

        ic_label = always_redraw(lambda: MathTex("I_c").scale(0.6).next_to(ic_arrow, RIGHT, buff=0.1))

        self.play(GrowArrow(ib_arrow), Write(ib_label))
        self.play(FadeIn(ic_arrow), Write(ic_label))

        # === Equation Display ===
        eq = MathTex("I_c = \\beta \\cdot I_b").scale(0.8).to_edge(UP)
        self.play(Write(eq))

        # === Beta Value Tracker + Slider Display ===
        

        beta_text = always_redraw(lambda: Tex(
            f"\\(\\beta = {int(beta_tracker.get_value())}\\)"
        ).scale(0.7).next_to(eq, DOWN))

        self.play(FadeIn(beta_text))

        # === Slider Bar (static visual)
        slider_bar = Line(LEFT * 2, RIGHT * 2).scale(0.5).to_edge(DOWN).shift(UP * 0.5)
        slider_knob = always_redraw(lambda: Dot(color=WHITE).move_to(
            slider_bar.point_from_proportion(
                (beta_tracker.get_value() - 20) / 100  # assuming beta from 20 to 100
            )
        ))

        self.play(Create(slider_bar), FadeIn(slider_knob))

        # === Animate Beta Increase ===
        self.play(beta_tracker.animate.set_value(100), run_time=4, rate_func=linear)
        self.wait(2)



        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])

         # === Emitter, Base, Collector Blocks ===
        emitter = Rectangle(width=2, height=2, color=BLUE).shift(LEFT * 3)
        base = Rectangle(width=1, height=2, color=WHITE).next_to(emitter, RIGHT, buff=0)
        collector = Rectangle(width=2, height=2, color=BLUE).next_to(base, RIGHT, buff=0)

        self.play(FadeIn(emitter, base, collector))
        self.wait(0.5)

        # === Labels ===
        labels = VGroup(
            Tex("Emitter (N)").scale(0.5).next_to(emitter, DOWN),
            Tex("Base (P)").scale(0.5).next_to(base, DOWN),
            Tex("Collector (N)").scale(0.5).next_to(collector, DOWN),
        )
        self.play(Write(labels))

        # === Current Arrows ===
        ib_arrow = Arrow(start=UP, end=DOWN, color=YELLOW).scale(0.5)
        ib_arrow.next_to(base, UP, buff=0.1).shift(LEFT * 0.2)
        ib_label = Tex(r"$I_b$").scale(0.6).next_to(ib_arrow, LEFT, buff=0.1)

        ic_arrow = Arrow(start=UP, end=DOWN, color=BLUE).scale(1.2)
        ic_arrow.next_to(collector, UP, buff=0.1)
        ic_label = Tex(r"$I_c$").scale(0.6).next_to(ic_arrow, RIGHT, buff=0.1)

        self.play(GrowArrow(ib_arrow), Write(ib_label))
        self.wait(0.5)
        self.play(GrowArrow(ic_arrow), Write(ic_label))
        self.wait(1)

        # === Equation: Ic = β * Ib ===
        gain_eq = Tex(r"$I_c = \beta \cdot I_b$").scale(0.9).to_edge(UP)
        self.play(Write(gain_eq))
        self.wait(1)

        # === Show current gain visually ===
        gain_factor = 5
        base_current_dots = VGroup()
        for i in range(1):
            dot = Dot(color=YELLOW).move_to(ib_arrow.get_start())
            base_current_dots.add(dot)

        collector_current_dots = VGroup()
        for i in range(gain_factor):
            dot = Dot(color=BLUE).move_to(ic_arrow.get_start() + DOWN * 0.15 * i)
            collector_current_dots.add(dot)

        self.play(FadeIn(base_current_dots), FadeIn(collector_current_dots))
        self.wait(1)

        # === Animate flow of current dots ===
        self.play(*[dot.animate.shift(DOWN * 1.2) for dot in base_current_dots], run_time=1.5)
        self.play(*[dot.animate.shift(DOWN * 2) for dot in collector_current_dots], run_time=1.5)
        self.wait(1)

        # === Final note ===
        note = Tex(r"A small $I_b$ controls a large $I_c$: this is the current gain of a BJT").scale(0.6).to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)

    def get_ic_length(self, beta):
        # Scale collector current length based on beta
        base_current_length = 0.5  # fixed base current arrow size
        return base_current_length * beta / 50  # normalize for visualization
    '''
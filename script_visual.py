from manim import *
from visuals import RLine
from visuals import CustomTable
from visuals import CustomKey
from visuals import CustomIcon

class S1(Scene):
    def construct(self):
        ### Logo
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.scale(0.5)

        logo_anim = []
        logo_del = []
        for i in range(4):
            logo_anim.append(Create(logo[i]))
        for i in range(4):
            logo_del.append(Uncreate(logo[i]))

        ### End logo

        thanks = Text("Special thanks to Manim for the programmatic animations", font_size=16)
        thanks.shift(RIGHT*3, UP*2)
        logo.next_to(thanks, DOWN*3)

        name_intro = Text("John Isaac Delgado", font_size=32)
        name_intro.shift(LEFT*3)

        self.play(Write(name_intro))
        self.play(Write(thanks), *logo_anim)
        self.wait(3)

        self.play(Unwrite(name_intro), Unwrite(thanks), *logo_del)
        self.wait(2)

        jargon = Text("Jargon", font_size=36)
        jargon.shift(LEFT*4)

        j1 = Text("Relationship Optionality/Cardinality", font_size=28, color=BLUE_B)
        j2 = Text("Attribute Icons", font_size=28, color=BLUE_B)

        j1.shift(UP*0.5, RIGHT*3)
        j2.next_to(j1, DOWN*2)

        self.play(Write(jargon), Write(j1), Write(j2))
        self.wait(3)

        self.play(Unwrite(jargon), Unwrite(j1), Unwrite(j2))
        self.wait(3)


class S1A(Scene):
    def construct(self):
        r = RLine()
        card = Text("Cardinality", font_size=28)
        hwr = Text("-how many relationships", font_size=20)
        otm = Text("one-to-many", font_size=20)

        otm.next_to(r, UP)

        self.play(FadeIn(card, shift=RIGHT))
        self.wait(2)
        self.play(card.animate.scale(0.8).shift(UP*3))
        self.wait(2)

        hwr.next_to(card, DOWN)
        self.play(FadeIn(hwr))

        self.wait(1)
        self.play(*r.get_animations(), FadeIn(otm))

        self.wait(2)
        self.play(FadeOut(card, shift=LEFT), Unwrite(card), FadeOut(hwr), *r.remove_anim(), FadeOut(otm))

        self.wait(1)

        opt = Text("Optionality", font_size=28)
        ron = Text("-required or not", font_size=20)

        self.play(FadeIn(opt, shift=RIGHT))

        ron.next_to(opt, DOWN)
        self.play(FadeIn(ron))
        self.wait(2)

        self.play(FadeOut(ron), FadeOut(opt))
        self.wait(3)

class S1B(Scene):
    def construct(self):
        key = CustomKey(True, YELLOW, 0.5)
        key.set_fill(YELLOW, opacity=0.5)
        desc = Text("- uniquely identifies a record", font_size=24)
        self.play(Create(key))
        self.wait(2)

        self.play(key.animate.shift(LEFT*2))
        desc.next_to(key, RIGHT)
        self.play(Write(desc))

        self.wait(3)
        self.play(Uncreate(key), FadeOut(desc))
        self.wait(3)

        i1 = CustomIcon(True, 0.5)
        i2 = CustomIcon(True, 0.5)
        i3 = CustomIcon(True, 0.5)
        i4 = CustomIcon(True, 0.5)

        i1.set_fill(BLUE, opacity=1)
        i2.set_stroke(BLUE)
        i3.set_fill(RED, opacity=1)
        i4.set_stroke(RED)

        i1.shift(UP, LEFT)
        i2.next_to(i1, RIGHT)
        i3.next_to(i1, DOWN)
        i4.next_to(i3, RIGHT)

        f = Text("Foreign", font_size=20)
        i = Text("Inherent", font_size=20)
        n = Text("Null", font_size=20)
        nn = Text("Not null", font_size=20)

        f.next_to(i3, LEFT)
        i.next_to(i1, LEFT)
        n.next_to(i2, UP)
        nn.next_to(i1, UP)

        self.play(Create(i1), Create(i2), Create(i3), Create(i4), Create(f), Create(i), Create(nn), Create(n))
        self.wait(3)
        self.play(Uncreate(i1), Uncreate(i2), Uncreate(i3), Uncreate(i4), Uncreate(i), Uncreate(f), Uncreate(n), Uncreate(nn))
        self.wait(3)

class S2(Scene):
    def construct(self):
        erd = Text("ERD", font_size=40)

        self.play(Write(erd))
        self.wait(2)
        self.play(erd.animate.shift(UP))

        o = Text("Orders", font_size=28)
        po = Text("Purchase orders", font_size=28)
        e = Text("Employee", font_size=28)
        it = Text("Inventory Transactions", font_size=28)
        p = Text("Products", font_size=28)

        po.next_to(erd, DOWN)
        o.next_to(po, LEFT*2)
        e.next_to(po, RIGHT*2)
        it.next_to(po, DOWN*2)
        p.next_to(it, DOWN*2)

        self.wait(3)
        self.play(Write(po), Write(p), Write(it), Write(e), Write(o))
        self.wait(3)
        self.play(Unwrite(po), Unwrite(p), Unwrite(it), Unwrite(e), Unwrite(o), Unwrite(erd))


class S2A(Scene):
    def construct(self):
        pass

class S2B(Scene):
    def construct(self):
        pass

class S2C(Scene):
    def construct(self):
        pass

class S2D(Scene):
    def construct(self):
        pass

class S2E(Scene):
    def construct(self):
        pass

class S3(Scene):
    def construct(self):
        pass

class S3A(Scene):
    def construct(self):
        pass

class S3B(Scene):
    def construct(self):
        pass

class S3C(Scene):
    def construct(self):
        pass

class S4(Scene):
    def construct(self):
        pass

class TestTable(Scene):
    def construct(self):
        table = CustomTable("Test", [
            ["key", "yellow", "INT", False, "ID"],
            ["icon", "blue", "VARCHAR(50)", False, "name"],
            ["icon", "blue", "VARCHAR(50)", False, "name"],
            ["icon", "red", "VARCHAR(50)", False, "name"],
            ["icon", "red", "VARCHAR(50)", False, "name"],
            ["icon", "red", "VARCHAR(50)", False, "name"],
            ["icon", "blue", "VARCHAR(50)", False, "name"],
            ["icon", "red", "INT", True, "fuck"]
        ], 3.5)
        table.to_edge(UP)

        # self.play(FadeIn(test, shift=LEFT))
        self.play(AnimationGroup(*table.get_animations(), lag_ratio=0.1))
        self.play(AnimationGroup(*table.remove_table(), lag_ratio=0.1))
        self.wait(2)
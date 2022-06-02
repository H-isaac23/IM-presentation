from manim import *
from colour import Color

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

class TestRLine(Scene):
    def construct(self):
        r = RLine()
        self.play(*r.get_animations())
        self.wait(2)

class CustomKey(Polygon):
    def __init__(self, scaled=False, color: Color = YELLOW, scale_factor=0.08, **kwargs):
        super().__init__(
            [-0.7, 1.8, 0],
            [0, 2.5, 0],
            [0.7, 1.8, 0],
            [0.5, 1, 0],
            [0.5, -0.75, 0],
            [-0.5, 0, 0],
            [-0.5, 1, 0],
            color=color,
            **kwargs
        )
        if(scaled == True):
            self.scale(scale_factor)

class CustomIcon(Square):
    def __init__(self, scaled=False, scale_factor=0.08, **kwargs):
        super().__init__(**kwargs)
        self.rotate(PI/4)
        if scaled:
            self.scale(scale_factor)

class Column(VGroup):
    def __init__(self, icon, icon_color, data_type, icon_filled=False, name="Test"):
        self.icon_color = icon_color

        name = Text(name, font_size=12)
        if icon == "key":
            column_icon = CustomKey(scaled=True)
            column_icon.set_stroke(YELLOW)
            column_icon.stroke_width = 1.5
            column_icon.set_fill(YELLOW, opacity=0.5)
        else:
            column_icon = CustomIcon(scaled=True)

        if icon_color == "blue":
            column_icon.set_stroke(BLUE, opacity=0.7)
        elif icon_color == "red":
            column_icon.set_stroke(RED, opacity=0.7)

        if icon_filled:
            if icon_color == "blue":
                column_icon.set_fill(BLUE, opacity=1)
            elif icon_color == "red":
                column_icon.set_fill(RED, opacity=1)

        name.next_to(column_icon, RIGHT)

        data_type = Text(data_type, font_size=12)
        data_type.next_to(name, RIGHT)

        super().__init__(name, column_icon, data_type)

# For animating the table, use animation group

class CustomTable(VGroup):
    def __init__(self, table_name, columns, width):
        self.lencol = len(columns)

        height = 0.475*self.lencol+0.1
        rect = Rectangle(width=width, height=height)
        header = Text(table_name, font_size=16)
        rect.next_to(header, DOWN, buff=0.1)
        rect.stroke_width = 2

        v_columns = []
        for i in range(len(columns)):
            v_columns.append(Column(columns[i][0], columns[i][1], columns[i][2], columns[i][3], columns[i][4]))
            if i == 0:
                v_columns[i].next_to(header, DOWN)
            else:
                v_columns[i].next_to(v_columns[i-1], DOWN)

        super().__init__(header, *v_columns, rect)

    def get_animations(self):
        animations = []
        for i in range(len(self)-1):
            animations.append(FadeIn(self[i], shift=RIGHT))
        animations.append(Create(self[-1]))
        return animations

    def remove_table(self):
        animations = []
        for i in range(len(self)):
            animations.append(FadeOut(self[i], shift=LEFT))
        animations.append(Uncreate(self[-1]))
        return animations

class RLine(VGroup):
    def __init__(self):
        main = DashedLine([-2, 0, 0], [2, 0, 0], dash_length=0.1)
        op1 = Line([-1.9, 0.15, 0], [-1.9, -0.15, 0])
        op2 = Line([-1.8, 0.15, 0], [-1.8, -0.15, 0])
        f1 = Line([2, 0, 0], [2.2, 0.2, 0])
        f2 = Line([2, 0, 0], [2.2, 0, 0])
        f3 = Line([2, 0, 0], [2.2, -0.2, 0])
        f4 = Line([2, 0.15, 0], [2, -0.15, 0])

        super().__init__(main, op1, op2, f1, f2, f3, f4)

    def get_animations(self):
        animations = []
        for an in self:
            animations.append(Create(an))
        return animations

    def remove_anim(self):
        anim = []
        for an in self:
            anim.append(Uncreate(an))
        return anim

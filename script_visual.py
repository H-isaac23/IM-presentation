from manim import *
from visuals import RLine
from visuals import CustomTable
from visuals import CustomKey
from visuals import CustomIcon
from visuals import TInstance
from visuals import Count

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

        thanks = Text("Special thanks to Manim for the programmatic animations", font_size=20)
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

        self.wait(1)
        self.play(Write(po), Write(p), Write(it), Write(e), Write(o))
        self.wait(3)
        self.play(Unwrite(po), Unwrite(p), Unwrite(it), Unwrite(e), Unwrite(o), Unwrite(erd))
        self.wait(2)

class S2A(Scene):
    def construct(self):
        order_normal = CustomTable("Test", [
            ["key", "yellow", "INT", False, "id"],
            ["icon", "blue", "Datetime", False, "shipped_date"],
            ["icon", "blue", "Datetime", False, "order_date"],
            ["icon", "blue", "VARCHAR(50)", False, "ship_name"],
            ["icon", "blue", "LONGTEXT", False, "ship_address"],
            ["icon", "blue", "VARCHAR(50)", False, "ship_city"],
            ["icon", "blue", "VARCHAR(50)", False, "ship_state_province"],
            ["icon", "blue", "VARCHAR(50)", False, "ship_zip_postal_code"],
            ["icon", "blue", "VARCHAR(50)", False, "ship_country_region"],
            ["icon", "blue", "DECIMAL(19,4)", False, "shipping_fee"],
            ["icon", "blue", "DECIMAL(19,4)", False, "taxes"],
            ["icon", "blue", "VARCHAR(50)", False, "payment_type"],
            ["icon", "blue", "Datetime", False, "paid_date"],
            ["icon", "blue", "LONGTEXT", False, "notes"],
            ["icon", "blue", "DOUBLE", False, "tax_rate"]
        ], 3.5)
        order_normal.to_edge(UP*-0.75)

        self.play(*order_normal.get_animations())
        self.wait(2)
        self.play(order_normal.animate.to_edge(LEFT))

        one = Text("1", font_size=30)
        a = Text("A16", font_size=30, color=RED)

        one.next_to(order_normal, RIGHT*3)
        a.next_to(order_normal, RIGHT*3)

        self.play(Write(one))
        self.wait(1)
        self.play(Unwrite(one))
        self.wait(1)
        self.play(Write(a))
        self.wait(1)
        self.play(Unwrite(a))
        self.wait(1)

        varchar = Text("Varchar and longtext", font_size=30)
        sl = Text("- String of letters", font_size=20)
        long = Text("- Longtext is basically a longer varchar", font_size=20)

        varchar.next_to(order_normal, RIGHT*3)
        sl.next_to(varchar, DOWN)
        long.next_to(sl, DOWN)

        self.play(Write(varchar), Write(long), Write(sl))
        self.wait(2)
        self.play(Unwrite(varchar), Unwrite(long), Unwrite(sl), *order_normal.remove_table())
        self.wait(2)

        order_foreign = CustomTable("orders", [
            ["icon", "red", "INT", False, "employee_id"],
            ["icon", "red", "Datetime", False, "customer_id"],
            ["icon", "red", "Datetime", False, "shipper_id"],
            ["icon", "red", "VARCHAR(50)", False, "tax_status_id"],
            ["icon", "red", "LONGTEXT", False, "status_id"]
        ], 3.5)

        ots = CustomTable("orders_tax_status", [
            ["key", "yellow", "TINYINT(4)", False, "id"],
            ["icon", "red", "VARCHAR(50)", False, "tax_status_name"]
        ], 3.5)

        r = RLine()
        r.rotate(PI)
        r.shift(DOWN*0.5)

        self.play(*order_foreign.get_animations())
        self.play(order_foreign.animate.to_edge(LEFT).shift(UP*0.5))
        self.wait(3)

        r1 = SurroundingRectangle(order_foreign[4], color=RED)
        self.play(Create(r1))
        self.wait(2)
        self.play(Uncreate(r1))

        self.play(*ots.get_animations())
        self.play(ots.animate.to_edge(RIGHT))
        self.wait(2)

        self.play(*r.get_animations())
        self.wait(3)

        self.play(*ots.remove_table())
        self.wait(3)

        self.play(r.animate.shift(LEFT*1.5))
        self.play(r.animate.scale(0.75))
        self.wait(2)

        os = CustomTable("orders_status", [
            ["key", "yellow", "TINYINT(4)", False, "id"],
            ["icon", "red", "VARCHAR(50)", False, "status_name"]
        ], 3.5)
        os.next_to(r, RIGHT)

        r2 = SurroundingRectangle(order_foreign[5], color=RED)
        self.play(Create(r2))
        self.wait(2)
        self.play(Uncreate(r2))

        self.play(*os.get_animations())
        self.wait(3)
        self.play(*os.remove_table())
        self.wait(1.5)

        r3 = SurroundingRectangle(order_foreign[3], color=RED)

        s1 = CustomTable("Shippers", [
            ["key", "yellow", "INT", False, "id"],
            ["icon", "blue", "VARCHAR(50)", False, "company"],
            ["icon", "blue", "VARCHAR(50)", False, "last_name"],
            ["icon", "blue", "VARCHAR(50)", False, "first_name"],
            ["icon", "blue", "VARCHAR(50)", False, "email_address"],
            ["icon", "blue", "VARCHAR(50)", False, "job_title"],
            ["icon", "blue", "VARCHAR(25)", False, "business_phone"],
            ["icon", "blue", "VARCHAR(25)", False, "home_phone"],
            ["icon", "blue", "VARCHAR(25)", False, "mobile_phone"],
            ["icon", "blue", "VARCHAR(25)", False, "fax_number"],
            ["icon", "blue", "LONGTEXT", False, "address"],
            ["icon", "blue", "VARCHAR(50)", False, "city"]
        ], 3)

        s2 = CustomTable("Shippers", [
            ["icon", "blue", "VARCHAR(50)", False, "state_province"],
            ["icon", "blue", "VARCHAR(15)", False, "zip_postal_code"],
            ["icon", "blue", "VARCHAR(50)", False, "country_region"],
            ["icon", "blue", "LONGTEXT", False, "web_page"],
            ["icon", "blue", "LONGTEXT", False, "notes"],
            ["icon", "blue", "LONGBLOB", False, "attachments"]
        ], 3)

        s1.next_to(r, RIGHT)
        s2.next_to(s1, RIGHT)

        self.play(Create(r3))
        self.wait(2)
        self.play(Uncreate(r3))

        self.play(*s1.get_animations(), *s2.get_animations())
        self.wait(3)

        self.play(*s1.remove_table(), *s2.remove_table())
        self.wait(1.5)

        cust = Text("Customer table = Shipper table", font_size=30)
        cust.next_to(r, RIGHT)

        self.play(Write(cust))
        self.wait(3)
        self.play(Unwrite(cust))
        self.wait(1.5)

        iv = CustomTable("invoices", [
            ["key", "yellow", "INT", False, "id"],
            ["icon", "red", "INT", False, "order_id"],
            ["icon", "blue", "Datetime", False, "invoice_date"],
            ["icon", "blue", "Datetime", False, "due_date"],
            ["icon", "blue", "DECIMAL(19,4)", False, "shipping"],
            ["icon", "blue", "DECIMAL(19,4)", False, "tax"],
            ["icon", "blue", "DECIMAL(19,4)", False, "amount_due"]
        ], 3)

        iv.next_to(r, RIGHT)
        self.play(*iv.get_animations(), r.animate.rotate(PI))
        self.wait(3)
        self.play(*iv.remove_table())
        self.wait(1.5)

        od = CustomTable("order_details", [
            ["key", "yellow", "INT", False, "id"],
            ["icon", "red", "INT", True, "order_id"],
            ["icon", "red", "INT", False, "product_id"],
            ["icon", "red", "INT", False, "status_id"],
            ["icon", "blue", "DECIMAL(19,4)", True, "quantity"],
            ["icon", "blue", "DECIMAL(19,4)", False, "unit_price"],
            ["icon", "blue", "Datetime", False, "date_allocated"],
            ["icon", "blue", "DOUBLE", True, "discount"],
            ["icon", "blue", "INT", False, "purchase_order_id"],
            ["icon", "blue", "INT", False, "inventory_id"]
        ], 3)
        od.next_to(r, RIGHT)

        self.play(*od.get_animations())
        self.wait(3)
        self.play(*order_foreign.remove_table(), od.animate.next_to(r, LEFT))
        self.wait(1.5)

        ods = CustomTable("order_details_status", [
            ["key", "yellow", "TINYINT(4)", False, "id"],
            ["icon", "blue", "VARCHAR(50)", False, "status_name"]
        ], 3)
        ods.next_to(r, RIGHT)

        r4 = SurroundingRectangle(od[4], color=RED)

        self.play(Create(r4))
        self.wait(3)
        self.play(Uncreate(r4))

        self.play(*ods.get_animations(), r.animate.rotate(PI))
        self.wait(3)
        self.play(*od.remove_table(), *ods.remove_table(), *r.remove_anim())
        self.wait(1.5)

class S2B(Scene):
    def construct(self):
        sim = Text("Employee table is the same as customer table...", font_size=30)
        self.play(Write(sim))
        self.wait(2)
        self.play(Unwrite(sim))
        self.wait(2)

        ep = CustomTable("employee_privileges", [
            ["key", "red", "INT", True, "employee_id"],
            ["key", "red", "INT", True, "privilege_id"]
        ], 3)

        p = CustomTable("privileges", [
            ["key", "yellow", "INT", False, "id"],
            ["icon", "blue", "VARCHAR(50)", False, "privilege_name"]
        ], 3)

        r = RLine()
        r.shift(DOWN*0.5)
        r.rotate(PI)

        self.play(*p.get_animations())
        self.play(p.animate.to_edge(LEFT).shift(UP))
        r.next_to(p, RIGHT)
        ep.next_to(r, RIGHT)
        self.play(*r.get_animations())
        self.wait(2)
        self.play(*ep.get_animations())
        self.wait(2)
        self.play(*r.remove_anim(), *p.remove_table(), *ep.remove_table())
        self.wait(2)

class S2C(Scene):
    def construct(self):
        po = CustomTable("purchase_orders", [
            ["key", "yellow", "INT", False, "id"],
            ["icon", "blue", "Datetime", False, "submitted_date"],
            ["icon", "blue", "Datetime", False, "creation_date"],
            ["icon", "blue", "Datetime", False, "expected_date"],
            ["icon", "blue", "DECIMAL(19,4)", False, "shipping_fee"],
            ["icon", "blue", "DECIMAL(19,4)", False, "taxes"],
            ["icon", "blue", "Datetime", False, "payment_date"],
            ["icon", "blue", "DECIMAL(19,4)", False, "payment_amount"],
            ["icon", "blue", "VARCHAR(50)", False, "payment_method"],
            ["icon", "blue", "LONGTEXT", False, "notes"],
            ["icon", "blue", "INT", False, "approved_by"],
            ["icon", "blue", "Datetime", False, "approved_date"]
        ], 3.5)

        po2 = CustomTable("purchase_orders", [
            ["icon", "red", "INT", False, "supplier_id"],
            ["icon", "red", "INT", False, "created_by"],
            ["icon", "red", "INT", False, "status_id"],
        ], 3)

        r = RLine()
        r.shift(DOWN*0.5)

        po.to_edge(UP)
        po.to_edge(LEFT)
        po2.next_to(po, RIGHT)
        self.play(*po.get_animations(), *po2.get_animations())
        self.wait(2)
        self.play(*po.remove_table())
        self.wait(1)
        self.play(po2.animate.to_edge(LEFT))
        self.wait(1)
        r.next_to(po2, RIGHT)
        r.rotate(PI)
        self.play(*r.get_animations())
        self.wait(2)

        pos = CustomTable("purchase_order_status", [
            ["key", "yellow", "INT", True, "id"],
            ["icon", "blue", "VARCHAR(50)", True, "status"]
        ], 3)
        pos.next_to(r, RIGHT)

        r1 = SurroundingRectangle(po2[3], color=RED)

        self.play(Create(r1))
        self.wait(2)
        self.play(Uncreate(r1))

        self.play(*pos.get_animations())
        self.wait(2)
        self.play(*pos.remove_table())
        self.wait(1)

        supp = Text("Supplier table = customer table...", font_size=24)
        supp.next_to(r, RIGHT)
        self.play(Write(supp))
        self.wait(2)
        self.play(Unwrite(supp))

        emp = Text("Employee table was already explained...", font_size=24)
        emp.next_to(r, RIGHT)
        self.play(Write(emp))
        self.wait(2)
        self.play(Unwrite(emp))
        self.wait(2)

        pod = CustomTable("purchase_order_details", [
            ["key", "yellow", "INT", False, "id"],
            ["icon", "red", "INT", True, "purchase_order_id"],
            ["icon", "red", "INT", False, "product_id"],
            ["icon", "red", "INT", False, "inventory_id"],
            ["icon", "blue", "DECIMAL(19,4)", True, "quantity"],
            ["icon", "blue", "DECIMAL(19,4)", True, "unit_cost"],
            ["icon", "blue", "Datetime", False, "date_received"],
            ["icon", "blue", "TINYINT(1)", True, "posted_to_inventory"]
        ], 3.5)
        pod.next_to(r, RIGHT)

        self.play(*pod.get_animations(), r.animate.rotate(PI))
        self.wait(2)
        self.play(*pod.remove_table(), *r.remove_anim())
        self.wait(5)
        self.play(*po2.remove_table())
        self.wait(2)

class S2D(Scene):
    def construct(self):
        p = CustomTable("products", [
            ["key", "yellow", "INT", False, "id"],
            ["icon", "blue", "VARCHAR(50)", False, "product_code"],
            ["icon", "blue", "VARCHAR(25)", False, "product_name"],
            ["icon", "blue", "LONGTEXT", False, "Description"],
            ["icon", "blue", "DECIMAL(19,4)", False, "standard_cost"],
            ["icon", "blue", "DECIMAL(19,4)", True, "list_price"],
            ["icon", "blue", "INT", False, "reorder_level"],
            ["icon", "blue", "INT", False, "target_level"],
            ["icon", "blue", "VARCHAR(50)", False, "quantity_per_unit"],
            ["icon", "blue", "TINYINT(1)", True, "discontinued"],
            ["icon", "blue", "INT", False, "minimum_reorder_quantity"],
            ["icon", "blue", "VARCHAR(50)", False, "category"]
        ], 3.5)
        p.to_edge(UP)

        self.play(*p.get_animations())
        self.wait(3)
        self.play(*p.remove_table())
        self.wait(2)

class S2E(Scene):
    def construct(self):
        it = CustomTable("inventory_transactions", [
            ["key", "yellow", "INT", False, "id"],
            ["icon", "red", "TINYINT(4)", True, "transaction_type"],
            ["icon", "red", "INT", True, "product_id"],
            ["icon", "red", "INT", False, "purchase_order_id"],
            ["icon", "red", "INT", False, "customer_order_id"],
            ["icon", "blue", "Datetime", False, "transaction_created_date"],
            ["icon", "blue", "Datetime", False, "transaction_modified_date"],
            ["icon", "blue", "INT", True, "quantity"],
            ["icon", "blue", "VARCHAR(255)", False, "comments"]
        ], 3.75)
        it.shift(UP*1.5)

        self.play(*it.get_animations())
        self.wait(2)
        self.play(it.animate.to_edge(LEFT))
        self.wait(2)

        r1 = SurroundingRectangle(it[2], color=RED)

        self.play(Create(r1))
        self.wait(1)
        self.play(Uncreate(r1))
        self.wait(2)

        r = RLine()
        r.next_to(it, RIGHT)

        itt = CustomTable("inventory_transaction_types", [
            ["key", "yellow", "INT", True, "id"],
            ["icon", "blue", "VARCHAR(50)", True, "type"]
        ], 3)
        itt.next_to(r, RIGHT)

        self.play(*itt.get_animations(), *r.get_animations())
        self.wait(3)
        self.play(*itt.remove_table(), *it.remove_table(), *r.remove_anim())

class S3(Scene):
    def construct(self):
        cool = Text("This is cool...", font_size=30)
        but = Text("...but is there anything else?", font_size=30)

        cool.shift(UP)
        but.next_to(cool, DOWN)

        self.play(Write(cool))
        self.wait(2)
        self.play(Write(but))
        self.wait(2)
        self.play(Unwrite(cool), Unwrite(but))
        self.wait(0.5)

        rep = Text("3 report examples", font_size=30)
        self.play(Write(rep))
        self.wait(2)
        self.play(Unwrite(rep))
        self.wait(2)

class S3A(Scene):
    def construct(self):
        sr = CustomTable("sales_report", [
            ["key", "yellow", "INT", True, "id"],
            ["icon", "blue", "VARCHAR(50)", True, "revenue"],
            ["icon", "blue", "VARCHAR(50)", True, "cost"],
            ["icon", "blue", "VARCHAR(50)", True, "profit"],
        ], 2.75)
        sr.shift(UP*1.25)

        self.play(*sr.get_animations())
        self.wait(1)
        self.play(sr.animate.to_edge(LEFT))
        self.wait(1)

        t1 = TInstance("Amount: P12,000")
        t2 = TInstance("Amount: P23,000")
        t3 = TInstance("Amount: P32,000")
        t4 = TInstance("Amount: P15,000")
        t5 = TInstance("Amount: P15,000")
        t1.shift(UP*1.5)
        t2.next_to(t1, DOWN)
        t3.next_to(t2, DOWN)
        t4.next_to(t3, DOWN)
        t5.next_to(t4, DOWN)

        self.play(Write(t1[0]), Create(t1[1]),
                  Write(t2[0]), Create(t2[1]),
                  Write(t3[0]), Create(t3[1]),
                  Write(t4[0]), Create(t4[1]),
                  Write(t5[0]), Create(t5[1]))
        self.wait(1)

        p = Text("P", font_size=32)
        p.shift(RIGHT*3)
        total = DecimalNumber().set_color(WHITE)
        total.next_to(p, RIGHT)
        total.add_updater(lambda total: total.next_to(p, RIGHT))

        self.play(Write(p), Write(total))
        self.wait(2)

        self.play(FadeOut(t1, target_position=total),
                  FadeOut(t2, target_position=total),
                  FadeOut(t3, target_position=total),
                  FadeOut(t4, target_position=total),
                  FadeOut(t5, target_position=total),
                  Count(total, 0, 97000),
                  runtime=0.5)
        self.wait(2)

        prod = Text("Product", font_size=32)
        reg = Text("Region", font_size=32)
        cat = Text("Category", font_size=32)

        prod.next_to(total, UP)
        reg.next_to(total, UP)
        cat.next_to(total, UP)

        self.play(FadeIn(prod, shift=UP), Count(total, 97000, 34000))
        self.wait(0.3)
        self.play(FadeOut(prod, shift=DOWN))
        self.play(FadeIn(reg, shift=UP), Count(total, 34000, 108000))
        self.wait(0.3)
        self.play(FadeOut(reg, shift=DOWN))
        self.play(FadeIn(cat, shift=UP), Count(total, 108000, 54000))
        self.wait(0.3)
        self.play(FadeOut(cat, shift=DOWN))
        self.wait(2)

        self.play(Unwrite(p), Unwrite(total), *sr.remove_table())
        self.wait(2)

class S3B(Scene):
    def construct(self):
        it = CustomTable("inventory_transactions", [
            ["key", "yellow", "INT", False, "id"],
            ["icon", "red", "TINYINT(4)", True, "transaction_type"],
            ["icon", "red", "INT", True, "product_id"],
            ["icon", "red", "INT", False, "purchase_order_id"],
            ["icon", "red", "INT", False, "customer_order_id"],
            ["icon", "blue", "Datetime", False, "transaction_created_date"],
            ["icon", "blue", "Datetime", False, "transaction_modified_date"],
            ["icon", "blue", "INT", True, "quantity"],
            ["icon", "blue", "VARCHAR(255)", False, "comments"]
        ], 3.75)
        it.shift(UP * 1.5)

        box = SurroundingRectangle(it[8], color=BLUE_B)
        self.play(*it.get_animations())
        self.wait(2)
        self.play(Create(box))
        self.wait(1)
        self.play(*it.remove_table(), Uncreate(box))
        self.wait(3)

class S3C(Scene):
    def construct(self):
        res = Text("Research report", font_size=36)
        self.play(Write(res))
        self.wait(2)
        self.play(res.animate.to_edge(UP))
        self.wait(1)

        cust = Text("Customer: ", font_size=28)
        cust.shift(LEFT*1.5)
        cust.shift(UP*1.5)

        prod = Text("Product: ", font_size=28)
        prod.next_to(cust, DOWN)

        j1 = Text("Software Engineer", font_size=28)
        j1.next_to(cust, RIGHT)

        j2 = Text("Civil Engineer", font_size=28)
        j2.next_to(cust, RIGHT)

        j3 = Text("Doctor", font_size=28)
        j3.next_to(cust, RIGHT)

        j4 = Text("President", font_size=28)
        j4.next_to(cust, RIGHT)

        p1 = Text("Mechanical Keyboard", font_size=28)
        p1.next_to(j1, DOWN)

        p2 = Text("Chocolate", font_size=28)
        p2.next_to(j2, DOWN)

        p3 = Text("Keychain", font_size=28)
        p3.next_to(j3, DOWN)

        p4 = Text("Plushie", font_size=28)
        p4.next_to(j4, DOWN)

        self.play(Write(cust), Write(prod), run_time=0.5)
        self.wait(2)
        self.play(FadeIn(j1, shift=UP), FadeIn(p1, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(j2, shift=UP), FadeIn(p2, shift=UP), FadeOut(j1, shift=UP), FadeOut(p1, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(j3, shift=UP), FadeIn(p3, shift=UP), FadeOut(j2, shift=UP), FadeOut(p2, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(j4, shift=UP), FadeIn(p4, shift=UP), FadeOut(j3, shift=UP), FadeOut(p3, shift=UP))
        self.wait(0.3)
        self.play(FadeOut(j4, shift=UP), FadeOut(p4, shift=UP))
        self.wait(0.3)

        c1 = Text("California", font_size=28)
        c1.next_to(cust, RIGHT)

        c2 = Text("New York", font_size=28)
        c2.next_to(cust, RIGHT)

        pc1 = Text("iPhone 13", font_size=28)
        pc1.next_to(c1, DOWN)

        pc2 = Text("Clothes", font_size=28)
        pc2.next_to(c2, DOWN)

        self.play(FadeIn(c1, shift=UP), FadeIn(pc1, shift=UP))
        self.wait(0.3)
        self.play(FadeIn(c2, shift=UP), FadeIn(pc2, shift=UP), FadeOut(c1, shift=UP), FadeOut(pc1, shift=UP))
        self.wait(0.3)
        self.play(FadeOut(c2, shift=UP), FadeOut(pc2, shift=UP))
        self.wait(1)
        self.play(Unwrite(cust), Unwrite(res), Unwrite(prod))
        self.wait(2)

class S4(Scene):
    def construct(self):
        db = Text("Databases are important!", font_size=32)
        t = Text("Thanks for watching!", font_size=32)

        self.play(Write(db))
        self.wait(2)
        self.play(Unwrite(db))
        self.wait(1)
        self.play(Write(t))
        self.wait(2)
        self.play(Unwrite(t))
        self.wait(1)

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
from typing import List

from manim import *


class BinarySearch(Scene):
    def construct(self):

        self.intro("Binary search")

        self.show_theory()

        list_of_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41]
        target = 31
        low, high = 0, len(list_of_numbers) - 1
        mid = (low + high) // 2

        list_of_mobjects: List[Mobject] = []
        for idx, number in enumerate(list_of_numbers):
            number_mobject = self.create_number_mobject(number)
            if idx < len(list_of_numbers) // 2:
                number_mobject.shift(UP * 2).shift(
                    (len(list_of_numbers) // 2 - idx) * 0.6 * LEFT
                )
            else:
                number_mobject.shift(UP * 2).shift(
                    (idx - len(list_of_numbers) // 2) * 0.6 * RIGHT
                )
            list_of_mobjects.append(number_mobject)

            idx_mobject = Integer(number=idx).scale(0.3).next_to(number_mobject, UP)

            self.play(FadeIn(number_mobject, idx_mobject), run_time=0.25)

        self.wait(duration=0.5)

        target_text = Text("target = " + str(target), font_size=12).next_to(
            list_of_mobjects[-1], RIGHT
        )
        target_idx_text = (
            Text("target index =", font_size=12)
            .next_to(target_text, DOWN)
            .shift(RIGHT * 0.125)
        )
        target_idx = (
            Integer(number=-1)
            .scale(0.4)
            .set_color(GREEN)
            .next_to(target_idx_text, RIGHT, buff=0.1)
        )

        self.add(target_text, target_idx_text, target_idx)

        self.wait()

        low_integer = Integer(number=low).scale(0.4)
        low_text_gr = (
            VGroup(Text("low index =", font_size=12), low_integer)
            .arrange(direction=RIGHT, buff=0.1)
            .set_color(BLUE)
        )

        mid_integer = Integer(number=low).scale(0.4)
        mid_text_gr = (
            VGroup(Text("mid index =", font_size=12), mid_integer)
            .arrange(direction=RIGHT, buff=0.1)
            .set_color(ORANGE)
        )

        high_integer = Integer(number=low).scale(0.4)
        high_text_gr = (
            VGroup(Text("high index =", font_size=12), high_integer)
            .arrange(direction=RIGHT, buff=0.1)
            .set_color(YELLOW)
        )

        low_integer.add_updater(lambda l: l.set_value(low))
        mid_integer.add_updater(lambda m: m.set_value(mid))
        high_integer.add_updater(lambda h: h.set_value(high))

        vg = (
            VGroup(low_text_gr, mid_text_gr, high_text_gr)
            .arrange(direction=DOWN, buff=0.2)
            .next_to(list_of_mobjects[0], DOWN)
            .shift(RIGHT * 0.26)
        )

        self.add(vg)

        list_of_mobjects[low].set_color(color=BLUE)
        list_of_mobjects[high].set_color(color=YELLOW)

        while low <= high:
            mid = (low + high) // 2
            list_of_mobjects[mid].set_color(color=ORANGE)
            self.wait(1.5)
            if list_of_numbers[mid] == target:
                list_of_mobjects[mid].set_color(color=GREEN)
                target_idx.set_value(mid)
                self.wait(1.5)
                break
            elif list_of_numbers[mid] < target:
                for n in list_of_mobjects[low : mid + 1]:
                    n.set_color(color=DARK_GRAY)
                low = mid + 1
                list_of_mobjects[low].set_color(color=BLUE)
                self.wait(1.5)
            else:
                for n in list_of_mobjects[mid : high + 1]:
                    n.set_color(color=DARK_GRAY)
                high = mid - 1
                list_of_mobjects[high].set_color(color=YELLOW)
                self.wait(1.5)

        self.wait(2)

    def create_number_mobject(self, value):
        square = Square(0.5)
        digit = Text(str(value)).scale(0.3)
        square.add(digit)

        return square

    def show_theory(self):
        theory = """
        Binary search

        In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array.
        
        Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array.
        
        To keep track of the range to search the target within two indices, low and high, are used. A third one tracks the middle element of the current range.
        
        Binary search runs in logarithmic time, O(log n), in the worst case, where n is the length of the array.
        """
        tex = Tex(theory).scale(0.5)
        self.play(Write(tex), run_time=2.0)
        self.wait(2)
        self.clear()

    def intro(self, subtitle):
        my_site = Text("vladflore.tech", font="Noto Sans").scale(0.75)
        self.play(Write(my_site))
        self.play(my_site.animate.shift(1.5 * UP))
        t = Text(
            "Algorithms Animated", font="Noto Sans", gradient=(RED, BLUE, GREEN)
        ).scale(1.5)
        st = Text(subtitle, font="Noto Sans", color=BLUE).scale(0.3)
        g = Group(t, st).arrange(DOWN, buff=0.8).next_to(my_site, DOWN, buff=0.8)
        self.play(FadeIn(g), run_time=2)
        self.play(FadeOut(g), run_time=2)
        self.play(my_site.animate.shift(1.5 * DOWN))
        self.play(Unwrite(my_site))

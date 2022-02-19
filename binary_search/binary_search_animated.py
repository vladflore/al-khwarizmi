from typing import List

from manim import *
from numpy import number


class BinarySearchAnimated(Scene):
    def construct(self):
        # self.intro('Binary search')

        list_of_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        target = 2
        low, high = 0, len(list_of_numbers)-1
        mid = (low+high)//2

        list_of_mobjects: List[Mobject] = []
        for idx in range(len(list_of_numbers)):
            number_mobject = self.create_number_mobject(list_of_numbers[idx])
            if idx < len(list_of_numbers)//2:
                number_mobject.shift(UP*2).shift(
                    (len(list_of_numbers)//2-idx)*0.6*LEFT)
            else:
                number_mobject.shift(
                    UP*2).shift((idx-len(list_of_numbers)//2)*0.6*RIGHT)
            list_of_mobjects.append(number_mobject)

            idx_mobject = Integer(number=idx).scale(
                0.3).next_to(number_mobject, UP)

            self.play(FadeIn(number_mobject, idx_mobject))

        self.wait()

        low_integer = Integer(number=low).scale(0.4)
        low_text = VGroup(Text(
            "low =", font_size=12), low_integer).arrange(direction=RIGHT, buff=0.1).set_color(BLUE)

        mid_integer = Integer(number=low).scale(0.4)
        mid_text = VGroup(Text(
            "mid =", font_size=12), mid_integer).arrange(direction=RIGHT, buff=0.1).set_color(ORANGE)

        high_integer = Integer(number=low).scale(0.4)
        high_text = VGroup(Text(
            "high =", font_size=12), high_integer).arrange(direction=RIGHT, buff=0.1).set_color(YELLOW)

        low_integer.add_updater(lambda l: l.set_value(low))
        mid_integer.add_updater(lambda m: m.set_value(mid))
        high_integer.add_updater(lambda h: h.set_value(high))

        vg = VGroup(low_text, mid_text, high_text).arrange(direction=DOWN, buff=0.2).next_to(
            list_of_mobjects[0], DOWN)

        self.add(vg)

        low_mobject = list_of_mobjects[low]
        low_mobject.set_color(color=BLUE)
        high_mobject = list_of_mobjects[high]
        high_mobject.set_color(color=YELLOW)

        mid_mobject = None
        while(low <= high):
            mid = (low+high)//2
            if mid_mobject is not None:
                mid_mobject.set_color(color=WHITE)
            mid_mobject = list_of_mobjects[mid]
            mid_mobject.set_color(color=ORANGE)
            self.wait()
            if list_of_numbers[mid] == target:
                low_mobject.set_color(color=WHITE)
                high_mobject.set_color(color=WHITE)
                list_of_mobjects[mid].set_color(GREEN)
                self.wait()
                break
            elif list_of_numbers[mid] < target:
                low = mid + 1
                low_mobject.set_color(color=WHITE)
                low_mobject = list_of_mobjects[low]
                low_mobject.set_color(color=BLUE)
                self.wait()
            else:
                high = mid - 1
                high_mobject.set_color(color=WHITE)
                high_mobject = list_of_mobjects[high]
                high_mobject.set_color(color=YELLOW)
                self.wait()

        self.wait()

    def create_number_mobject(self, value):
        square = Square(0.5)
        digit = Text(str(value)).scale(0.3)
        square.add(digit)

        return square

    def intro(self, subtitle):
        my_site = Text("vladflore.tech", font="Noto Sans").scale(0.75)
        self.play(Write(my_site))
        self.play(my_site.animate.shift(1.5 * UP))
        t = Text("Algoritmhs Animated", font="Noto Sans",
                 gradient=(RED, BLUE, GREEN)).scale(1.5)
        st = Text(subtitle, font="Noto Sans",
                  color=BLUE).scale(0.3)
        g = Group(t, st).arrange(DOWN, buff=.8).next_to(
            my_site, DOWN, buff=0.8)
        self.play(FadeIn(g), run_time=2)
        self.play(FadeOut(g), run_time=2)
        self.play(my_site.animate.shift(1.5 * DOWN))
        self.play(Unwrite(my_site))

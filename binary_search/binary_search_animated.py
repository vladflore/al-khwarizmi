from typing import List

from manim import *


class BinarySearchAnimated(Scene):
    def construct(self):

        self.intro('Binary search')

        self.show_theory()

        list_of_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 23, 29, 31]
        target = 11
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

            self.play(FadeIn(number_mobject, idx_mobject), run_time=0.25)

        self.wait(duration=0.5)

        target_text = Text("target = " + str(target),
                           font_size=12).next_to(list_of_mobjects[-1], RIGHT)
        target_idx_text = Text(
            "target index =", font_size=12).next_to(target_text, DOWN).shift(RIGHT*0.125)
        target_idx = Integer(
            number=-1).scale(0.4).set_color(GREEN).next_to(target_idx_text, RIGHT, buff=0.1)

        self.add(target_text, target_idx_text, target_idx)

        self.wait()

        low_integer = Integer(number=low).scale(0.4)
        low_text_gr = VGroup(Text(
            "low index =", font_size=12), low_integer).arrange(direction=RIGHT, buff=0.1).set_color(BLUE)

        mid_integer = Integer(number=low).scale(0.4)
        mid_text_gr = VGroup(Text(
            "mid index =", font_size=12), mid_integer).arrange(direction=RIGHT, buff=0.1).set_color(ORANGE)

        high_integer = Integer(number=low).scale(0.4)
        high_text_gr = VGroup(Text(
            "high index =", font_size=12), high_integer).arrange(direction=RIGHT, buff=0.1).set_color(YELLOW)

        low_integer.add_updater(lambda l: l.set_value(low))
        mid_integer.add_updater(lambda m: m.set_value(mid))
        high_integer.add_updater(lambda h: h.set_value(high))

        vg = VGroup(low_text_gr, mid_text_gr, high_text_gr).arrange(direction=DOWN, buff=0.2).next_to(
            list_of_mobjects[0], DOWN).shift(RIGHT*0.26)

        self.add(vg)

        low_mobject = list_of_mobjects[low]
        low_mobject.set_color(color=BLUE)
        high_mobject = list_of_mobjects[high]
        high_mobject.set_color(color=YELLOW)

        while(low <= high):
            mid = (low+high)//2
            mid_mobject = list_of_mobjects[mid]
            mid_mobject.set_color(color=ORANGE)
            self.wait()
            if list_of_numbers[mid] == target:
                low_mobject.set_color(color=WHITE)
                mid_mobject.set_color(color=WHITE)
                high_mobject.set_color(color=WHITE)
                list_of_mobjects[mid].set_color(GREEN)
                target_idx.set_value(mid)
                self.wait()
                break
            elif list_of_numbers[mid] < target:
                low = mid + 1
                mid_mobject.set_color(color=WHITE)
                low_mobject.set_color(color=WHITE)
                low_mobject = list_of_mobjects[low]
                low_mobject.set_color(color=BLUE)
                self.wait()
            else:
                high = mid - 1
                mid_mobject.set_color(color=WHITE)
                high_mobject.set_color(color=WHITE)
                high_mobject = list_of_mobjects[high]
                high_mobject.set_color(color=YELLOW)
                self.wait()

        self.wait(2)

    def create_number_mobject(self, value):
        square = Square(0.5)
        digit = Text(str(value)).scale(0.3)
        square.add(digit)

        return square

    def show_theory(self):
        title = MarkupText("Binary search", font="Noto Sans").shift(UP*2)
        self.play(Write(title))
        vg = VGroup()
        short_description = Text("In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop,\nis a search algorithm that finds the position of a target value within a sorted array.",
                                 font_size=14,
                                 font="Noto Sans"
                                 )
        long_description = Text("Binary search compares the target value to the middle element of the array.\nIf they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half,\nagain taking the middle element to compare to the target value, and repeating this until the target value is found.\nIf the search ends with the remaining half being empty, the target is not in the array.",
                                font_size=14,
                                font="Noto Sans"
                                )
        complexity = Text("The time complexity is: O(log n)",
                          font_size=14, font="Noto Sans")
        vg.add(short_description, long_description, complexity).arrange(
            DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        vg.next_to(title, DOWN, buff=MED_LARGE_BUFF)

        self.play(FadeIn(vg))

        self.wait(2)

        self.clear()

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

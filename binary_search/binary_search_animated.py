from typing import List

from manim import *


class BinarySearchAnimated(Scene):
    def construct(self):
        # self.intro('Binary search')

        list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 6
        low, high = 0, len(list_of_numbers)-1
        mid = (low+high)//2

        list_of_mobjects: List[Mobject] = []
        for idx in range(len(list_of_numbers)):
            number_mobject = self.create_number(list_of_numbers[idx])
            number_mobject.shift(idx*0.6*RIGHT)
            list_of_mobjects.append(number_mobject)
            self.play(FadeIn(number_mobject), run_time=0.5)

        low_number = Integer(number=list_of_numbers[low]).set_color(BLUE)
        high_number = Integer(number=list_of_numbers[high]).set_color(YELLOW)
        mid_number = Integer(number=list_of_numbers[mid]).set_color(ORANGE)

        low_number.next_to(list_of_mobjects[0], DOWN)
        high_number.next_to(low_number, DOWN)
        mid_number.next_to(high_number, DOWN)

        low_number.add_updater(lambda ln: ln.set_value(list_of_numbers[low]))
        high_number.add_updater(lambda hn: hn.set_value(list_of_numbers[high]))
        mid_number.add_updater(lambda mn: mn.set_value(list_of_numbers[mid]))

        self.add(low_number, high_number, mid_number)

        low_mobject = list_of_mobjects[low]
        low_mobject.set_color(color=BLUE)
        high_mobject = list_of_mobjects[high]
        high_mobject.set_color(color=YELLOW)

        mid_mobject = None
        while(low <= high):
            mid = (low+high)//2
            if mid_mobject is not None:
                mid_mobject.set_color(color=WHITE)
                self.wait()
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
                self.wait(2)
            else:
                high = mid - 1
                high_mobject.set_color(color=WHITE)
                high_mobject = list_of_mobjects[high]
                high_mobject.set_color(color=YELLOW)
                self.wait(2)

        self.wait()

    def create_number(self, value):
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

from manim import *


class BinarySearchAnimated(Scene):
    def construct(self):
        self.intro('Binary search')
        # tbd

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

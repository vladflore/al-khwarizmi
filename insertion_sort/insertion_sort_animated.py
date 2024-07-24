from manim import *


class InsertionSort(Scene):
    def construct(self):
        self.intro("Insertion sort")
        self.array = [10, 9, 8, 7, 6, 5, 5, 5, 4, 3, 2, 1]
        self.bars, self.labels = self.create_bars(self.array)
        self.add(*self.bars, *self.labels)
        self.insertion_sort()

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

    def create_bars(self, array):
        bars = []
        labels = []
        max_val = max(array)
        n = len(array)
        bar_width = 0.5
        bar_height_scale = 0.4  # Adjusted scaling factor for height
        spacing = 0.8  # Adjusted spacing between bars
        label_y_offset = (
            -max_val * bar_height_scale / 2 - 0.5
        )  # Fixed vertical position for labels

        for i, val in enumerate(array):
            bar = Rectangle(
                width=bar_width,
                height=val * bar_height_scale,
                fill_color=BLUE,
                fill_opacity=1,
                color=BLUE,  # border color to match fill color
            )
            bar.move_to(
                DOWN * (max_val * bar_height_scale / 2 - val * bar_height_scale / 2)
                + RIGHT * (i - n / 2) * spacing
            )
            bars.append(bar)

            label = Text(str(val), font="Noto Sans", color=WHITE).scale(0.4)
            label.next_to(bar, DOWN, buff=0.1)
            labels.append(label)

        return bars, labels

    def insertion_sort(self):
        n = len(self.array)
        max_val = max(self.array)
        bar_height_scale = 0.4  # Ensure consistency with create_bars method

        for i in range(1, n):
            key = self.array[i]
            key_bar = self.bars[i]
            key_label = self.labels[i]

            # Change the color of the bar and its label to be inserted to red
            self.play(
                key_bar.animate.set_fill(RED, opacity=1).set_color(RED),
                key_label.animate.set_color(RED),
                run_time=0.5,
            )

            # Remove the label temporarily
            self.remove(key_label)

            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                self.bars[j + 1] = self.bars[j]
                self.labels[j + 1] = self.labels[j]
                self.play(
                    self.bars[j + 1].animate.move_to(
                        self.bars[j + 1].get_center() + 0.8 * RIGHT
                    ),
                    self.labels[j + 1].animate.move_to(
                        self.labels[j + 1].get_center() + 0.8 * RIGHT
                    ),
                    run_time=0.5,
                )
                j -= 1
            self.array[j + 1] = key
            self.bars[j + 1] = key_bar
            self.labels[j + 1] = key_label
            self.play(
                self.bars[j + 1].animate.move_to(
                    DOWN * (max_val * bar_height_scale / 2 - key * bar_height_scale / 2)
                    + RIGHT * (j + 1 - n / 2) * 0.8
                ),
                run_time=0.5,
            )

            # Add the label back in the correct position
            key_label.next_to(self.bars[j + 1], DOWN, buff=0.1)
            self.add(key_label)

            # Change the color of the bar and its label back to its original color after insertion
            self.play(
                key_bar.animate.set_fill(BLUE, opacity=1).set_color(BLUE),
                key_label.animate.set_color(WHITE),
                run_time=0.5,
            )

from manim import (
    Scene,
    Square,
    Text,
    VGroup,
    Write,
    RIGHT,
    UP,
    DOWN,
    LEFT,
    Create,
    BLUE,
    RED,
    GREEN,
    Group,
)
from manim.animation.fading import FadeIn, FadeOut
from manim.animation.creation import Unwrite


class QueueUsingStacksVisualization(Scene):
    def construct(self):

        self.intro("Queue implementation using two stacks")

        # Create initial empty stacks and queue containers
        stack1_container = VGroup(
            *[Square(side_length=0.75) for _ in range(5)]
        ).arrange(UP, buff=0.1)
        stack2_container = VGroup(
            *[Square(side_length=0.75) for _ in range(5)]
        ).arrange(UP, buff=0.1)
        queue_container = VGroup(*[Square(side_length=0.75) for _ in range(5)]).arrange(
            RIGHT, buff=0.1
        )

        stack1_group = VGroup(stack1_container).shift(DOWN * 1.5 + LEFT * 3)
        stack2_group = VGroup(stack2_container).shift(DOWN * 1.5 + RIGHT * 3)
        queue_group = VGroup(queue_container).shift(UP * 2)

        # Create labels for the stacks and queue
        stack1_label = Text("s1", font_size=24).next_to(stack1_group, UP)
        stack2_label = Text("s2", font_size=24).next_to(stack2_group, UP)
        queue_label = Text("q", font_size=24).next_to(queue_group, UP)

        self.play(Create(stack1_group), Create(stack2_group), Create(queue_group))
        self.play(Write(stack1_label), Write(stack2_label), Write(queue_label))

        stack1 = []
        stack2 = []
        queue = []

        def enqueue(element):
            new_elem_square = Square(side_length=0.75, color=BLUE)
            new_elem_label = Text(f"{element}", font_size=24)
            new_elem_group = VGroup(new_elem_square, new_elem_label)
            new_elem_label.move_to(new_elem_square.get_center())

            # Show the element being added to the queue from right to left
            start_position = queue_container.get_center() + RIGHT * 3
            end_position = queue_container[0].get_center() + RIGHT * len(queue) * (
                new_elem_square.get_width() + 0.1
            )
            new_elem_group.move_to(start_position)
            self.play(new_elem_group.animate.move_to(end_position), run_time=1)
            queue.append(new_elem_group)

            # Duplicate the element for stack operations
            duplicate_elem_group = new_elem_group.copy()

            # Move elements from stack1 to stack2
            while stack1:
                elem = stack1.pop()
                target_position = stack2_container[0].get_center() + UP * len(
                    stack2
                ) * (elem[0].get_height() + 0.1)
                self.play(elem.animate.move_to(target_position), run_time=1)
                stack2.append(elem)

            # Add the new element to stack1
            start_position = stack1_group.get_center() + UP * 2
            end_position = stack1_container[0].get_center() + UP * len(stack1) * (
                duplicate_elem_group[0].get_height() + 0.1
            )
            duplicate_elem_group.move_to(start_position)
            self.play(duplicate_elem_group.animate.move_to(end_position), run_time=1)
            stack1.append(duplicate_elem_group)

            # Move elements back from stack2 to stack1
            while stack2:
                elem = stack2.pop()
                target_position = stack1_container[0].get_center() + UP * len(
                    stack1
                ) * (elem[0].get_height() + 0.1)
                self.play(elem.animate.move_to(target_position), run_time=1)
                stack1.append(elem)

        # Animate adding five elements to the queue
        elements_to_add = [1, 2, 3, 4, 5]
        for element in elements_to_add:
            enqueue(element)
            self.wait(0.5)

        self.wait(2)

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


if __name__ == "__main__":
    scene = QueueUsingStacksVisualization()
    scene.render()

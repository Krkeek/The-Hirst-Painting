import random


def random_color():
    color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
                  (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
                  (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
                  (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
    return random.choice(color_list)


class Drawer:

    def __init__(self, t):
        self.t = t

    def line_up(self):
        self.t.setheading(90)
        self.t.forward(50)
        self.t.setheading(180)
        self.t.forward(500)
        self.t.setheading(0)

    def starting_point(self):
        self.t.setheading(225)
        self.t.forward(300)
        self.t.setheading(0)

    def draw_circle(self):
        self.starting_point()
        for _ in range(10):
            for _ in range(10):
                self.t.dot(20, random_color())
                self.t.forward(50)
            self.line_up()

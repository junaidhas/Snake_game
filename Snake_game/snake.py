from turtle import Turtle

STARTING_COR = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.square_list = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_COR:
            self.add_snake(position)


    def add_snake(self, position):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.goto(position)
        new_square.color("white")
        self.square_list.append(new_square)

    def reset_snake(self):
        for box in self.square_list:
            box.goto(1000,1000)
        self.square_list.clear()
        self.create_snake()

    def extend_snake(self):
        self.add_snake(self.square_list[-1].position())

    # def extend_snake(self):
    #     self.add_segment(turtle_objects=self.square_list[-1].position())


    def move(self):
        for sq_num in range(len(self.square_list) - 1, 0, -1):
            new_x = self.square_list[sq_num - 1].xcor()
            new_y = self.square_list[sq_num - 1].ycor()
            self.square_list[sq_num].goto(new_x, new_y)
            # game_is_on=False

        self.square_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.square_list[0].heading() != DOWN:
            self.square_list[0].setheading(UP)

    def down(self):
        if self.square_list[0].heading() != UP:
            self.square_list[0].setheading(DOWN)

    def left(self):
        if self.square_list[0].heading() != RIGHT:
            self.square_list[0].setheading(LEFT)

    def right(self):
        if self.square_list[0].heading() != LEFT:
            self.square_list[0].setheading(RIGHT)
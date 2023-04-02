from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.position_snake()
        self.head = self.segments[0]
    def create_snake(self):
        starting_squares = [(0,0),(-20,0),(-40,0)]
        for square in starting_squares:
           self.add_segment(square)

    def add_segment(self,position):
        katsu = Turtle()
        katsu.shape("square")
        katsu.color("white")
        katsu.penup()
        katsu.goto(position)
        self.segments.append(katsu)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def position_snake(self):        
        for seg in range(len(self.segments)-1,0,-1):
            next_seg_x_axis = self.segments[seg-1].xcor()
            next_seg_y_axis = self.segments[seg-1].ycor()
            self.segments[seg].goto(next_seg_x_axis,next_seg_y_axis)

    def move(self):
        self.position_snake()
        self.segments[0].fd(20)

    def moveup(self):
        if self.segments[0].heading() == 0:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].right(90)
        else:
            return
    def movedown(self):
        if self.segments[0].heading() == 180:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 0:
            self.segments[0].right(90)
        else:
            return

    def moveright(self):
        if self.segments[0].heading() == 270:
            self.segments[0].left(90)
        else:
            self.segments[0].right(90)

    def moveleft(self):
        if self.segments[0].heading() == 270:
            self.segments[0].right(90)
        else:
            self.segments[0].left(90)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head =  self.segments[0]
        

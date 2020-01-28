# my_drawings
# Rectangle
from shapes import Triangle, Rectangle, Oval

rect1 = Rectangle()
rect1.set_width(100)
rect1.set_height(200)
rect1.set_color('blue')

rect1.draw()

rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color('red')
rect2.set_x(100)
rect2.set_y(100)

rect2.draw()

# Oval

oval1 = Oval()
oval1.set_color('white')
oval1.set_x(30)
oval1.set_y(90)
oval1.draw()

#Triangle

tri = Triangle()
tri.randomize()
tri.set_color('blue')
tri.draw()

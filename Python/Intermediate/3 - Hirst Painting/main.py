from turtle import Turtle, Screen, colormode

# ================================== Comment Out after extracting colours from image==============================
# import colorgram
#
#
# def extract_colour(colours, index):
#     """Extract colours from an image using the 'colorgram" module."""
#     r = colours[index].rgb.r
#     g = colours[index].rgb.g
#     b = colours[index].rgb.b
#
#     return r, g, b
#
#
# rgb_colors = []
# image = "image.jpg"
# num_of_colors = 35
#
# colors = colorgram.extract(image, num_of_colors)
# for i in range(num_of_colors):
#     rgb_colors.append(extract_colour(colors, i))
#
# print(rgb_colors)
# ================================== Comment Out after extracting colours from image==============================

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),
              (254, 194, 0)]

link = Turtle()
link.hideturtle()
link.speed(0)
colormode(255)

dot_count = 0
color_counter = 0
y_axis = 0
length = len(color_list)
color = ()

link.penup()
x_cor = -250
y_cor = -200
link.setpos(x_cor, y_cor)

while dot_count <= 10:

    if color_counter < length:
        color = color_list[color_counter]
        color_counter += 1
    else:
        color_counter = 0

    if dot_count == 10:
        dot_count = 0
        y_axis += 50
        link.setpos(x_cor, y_cor + y_axis)

        if y_axis == 500:
            break

    link.dot(20, color)
    link.forward(50)

    dot_count += 1

my_screen = Screen()
my_screen.exitonclick()

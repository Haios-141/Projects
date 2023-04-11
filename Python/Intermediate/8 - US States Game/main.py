import pandas
import turtle

FONT = ("Times New Roman", 8, "normal")
STATE_COUNT = 50

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# Get the x and y coordinates of the states on the image. Comment out after getting the coordinates.
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()

score = 0

answer_state = turtle.textinput(title="Guess the State", prompt="Enter a state name:").title()
state = data[data.state == answer_state]
while score < STATE_COUNT:
    if answer_state == "Exit":
        remaining_states = pandas.DataFrame(data.state.tolist())
        remaining_states.to_csv("states_to_learn_1.csv")
        break

    try:
        state_name = state.state.iat[0]
        x_coor = state.x.iat[0]
        y_coor = state.y.iat[0]
        data.drop(state.index, inplace=True)  # Remove the row after using it
        state_turtle.goto(x_coor, y_coor)
        state_turtle.write(f"{state_name}", font=FONT)
        score += 1
    except IndexError:
        continue
    finally:
        if score < STATE_COUNT:
            answer_state = turtle.textinput(title=f"{score}/{STATE_COUNT} States Correct",
                                            prompt="Enter another state name:").title()
            state = data[data.state == answer_state]

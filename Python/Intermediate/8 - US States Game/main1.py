import pandas
import turtle

FONT = ("Times New Roman", 8, "normal")
STATE_COUNT = 50

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# # Get the x and y coordinates of the states on the image. Comment out after getting the coordinates.
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
# guessed_states = []

answer_state = turtle.textinput(title="Guess the State", prompt="Enter a state name:").title()
state_list = data.state.to_list()

while score < STATE_COUNT:
    if answer_state == "Exit":
        remaining_states = pandas.DataFrame(state_list)
        remaining_states.to_csv("states_to_learn_2.csv")
        break

    if answer_state in state_list:
        state_list.remove(answer_state)  # Remove the state from the list after using it
        state_data = data[data.state == answer_state]
        x_coor = state_data.x.iat[0]
        y_coor = state_data.y.iat[0]
        state_turtle.goto(x_coor, y_coor)
        state_turtle.write(f"{answer_state}", font=FONT)
        score += 1

    if score < STATE_COUNT:
        answer_state = turtle.textinput(title=f"{score}/{STATE_COUNT} States Correct",
                                        prompt="Enter another state name:").title()

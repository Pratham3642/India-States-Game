import pandas
import turtle

screen = turtle.Screen()
screen.title("India States Game")
screen.addshape("india-state.gif")
turtle.shape("india-state.gif")

data = pandas.read_csv("29_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 State Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

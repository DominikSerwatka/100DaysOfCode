import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_date = data[data.state == answer_state]
        t.goto(state_date.x.iloc[0], state_date.y.iloc[0])
        t.write(state_date.state.item())

list_to_learn = []

for item in all_state:
    if item not in guessed_states:
        list_to_learn.append(item)
data_dict = {
    "states": list_to_learn,
}
data2 = pandas.DataFrame(data_dict)
data2.to_csv("states_to_learn.csv")

import turtle
import pandas
screen = turtle.Screen()
screen.title("US Sates Game")
image = r"C:\Users\mailc\Files_Practise\US_Sates_game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"C:\Users\mailc\Files_Practise\US_Sates_game\50_states.csv")
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(f"{len(guessed_states)}/50 states Correct",
                                    "What  another state name do you have?").title()
    print(answer_state)
    if answer_state =="Exit":
        missing_states =[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(r"C:\Users\mailc\Files_Practise\US_Sates_game\States_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)



import turtle
screen = turtle.Screen()
screen.title("US Sates Game")
image = r"C:\Users\mailc\Files_Practise\US_Sates_game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput("Guess the state name", "What state do you have?")
#screen.exitonclick()
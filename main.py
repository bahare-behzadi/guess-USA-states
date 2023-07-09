import turtle
import pandas
from random import randint
Font = ("Verdana", 11, "bold")

image = "1.gif"
screen = turtle.Screen()
screen.title("US states")
screen.addshape(image)
turtle.shape(image)
guess_lists = []
turtle.colormode(255)
while len(guess_lists) < 50:
    guess = turtle.textinput(title=f"{len(guess_lists)}/50 CORRECT GUESSES", prompt="Guess the next state of USA?").title()
    data_base = pandas.read_csv("50_states.csv")
    states_list = data_base["state"].to_list()
    if guess == "Exit":
        not_guess_list = []
        for each_state in states_list:
            if each_state not in guess_lists:
                not_guess_list.append(each_state)
        missing_data = pandas.DataFrame(not_guess_list)
        missing_data.to_csv("missing_states.csv")
        finish_game = turtle.Turtle()
        finish_game.hideturtle()
        finish_game.goto(-250, 0)
        finish_game.color("red")
        finish_game.write("you can find the missing states in the file named: 'missing_states.csv'", "left", font=Font)
        break
    if guess in states_list:
        guess_lists.append(guess)
        x = int(data_base[data_base["state"] == guess]["x"])
        y = int(data_base[data_base["state"] == guess]["y"])
        turtle.penup()
        state_place = turtle.Turtle()
        state_place.shape("circle")
        r = randint(0, 255)
        b = randint(0, 255)
        g = randint(0, 255)
        state_place.color(r, b, g)
        state_place.shapesize(stretch_len=0.2, stretch_wid=0.2)
        state_place.penup()
        state_place.goto(x, y)
        state_place.write(arg=guess)




screen.exitonclick()


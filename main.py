import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game.")
image = "blank_states_img.gif"
# screen.addshape(image) This also works
turtle.addshape(image)  # adds the shape into the current shapes of the turtle class
turtle.shape(image)
ctr = 0  # score
# hello

def create_turtle(x_cord, y_cord, state):
    tur = turtle.Turtle()
    tur.penup()
    tur.goto(x_cord, y_cord)
    tur.write(arg=state, font=('Arial', 8, 'normal'))
# hello

states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()
print(states_data)

while ctr != 50:
    data = screen.textinput(title="Guess the answer.",prompt="What's the another state's name?")
    if data=="Exit":
        break
    for index, i in enumerate(states_list):
        if data == i:
            ctr += 1
            states = states_data[states_data["state"] == data]
            x = list(states.x)[0]
            y = list(states.y)[0]
            states_list.remove(i)
            create_turtle(x, y, data)

print("States not guessed are:")
print(states_list)
dicti = {"states": states_list}
df = pandas.DataFrame(dicti)
df.to_csv("not_guessed.csv")

screen.exitonclick()

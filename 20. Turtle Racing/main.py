from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
userBet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

turtleColorList = ["black", "blue", "red", "green", "purple", "yellow"]

if userBet not in turtleColorList:
    turtleColorList.append(userBet)

y_positions = [160, 120, 80, 40, 0, -40, -80, -120, -160]
turtObjects = []
differentMoveSpeeds = [1, 5, 10, 15, 20]

def generateTurtles():
    for i in range(len(turtleColorList)):
        turt = Turtle()
        turt.shape("turtle")
        turt.color(turtleColorList[i])
        turt.up()
        turt.setposition(x=-230, y=y_positions[i])
        turtObjects.append(turt)

generateTurtles()

def turtleSpeeds():
    for i in range(len(turtObjects)):
        turtObjects[i].forward(differentMoveSpeeds[random.randint(0,4)])
        if turtObjects[i].xcor() >= 100:
            print(f"{turtObjects[i].color()[0].title()} turtle won the race!")
            return True  # Return True if a turtle has won

while not turtleSpeeds():  # Exit the loop when a turtle wins the race
    pass

screen.exitonclick()
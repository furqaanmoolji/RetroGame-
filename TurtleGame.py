import turtle;
import math;
import random;
from playsound import playsound

#Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("bgpic.gif")
wn.tracer(3)

#Draw Border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.color("white")
mypen.pensize(3)
for side in range(4):
	mypen.forward(600)
	mypen.left(90)
mypen.hideturtle()




#Create a turtle
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)

#Create Goals
MaxGoals = 10
goals = []


score = 0;




#Create Goal
for count in range (MaxGoals):
	goals.append(turtle.Turtle())
	goals[count].color("red")
	goals[count].shape("square")
	goals[count].penup()
	goals[count].speed(0)
	goals[count].setposition(random.randint(-300,300), random.randint(-300,300))



speed=1

def turnleft():

   player.left(30)
   
   
   
def turnright():
	player.right(30)
	
	
def increaseSpeed():
	global speed
	speed=speed+1


def isCollison(t1,t2):
	d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2)) 
	if d<20:
		return True
	else:
		return False
	
	






#AddKeybindings
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increaseSpeed,"Up")


while True:
	player.forward(speed)
	#BoundaryChecking 
	if player.xcor()>300 or player.xcor()<-300:
		player.right(180)
	if player.ycor()>300 or player.ycor()<-300:
		player.right(180)
		
	#Collision Checking
	
		
		
	for count in range(MaxGoals):
		goals[count].forward(0.5)
		if goals[count].xcor()>290 or goals[count].xcor()<-290:
			goals[count].right(180)
		if goals[count].ycor()>290 or goals[count].ycor()<-290:
			goals[count].right(180)
		if isCollison(player,goals[count]):
			goals[count].setposition(random.randint(-300,300), random.randint(-300,300)) 
			goals[count].right(random.randint(0,360))
			score+=1
			#Draw the score on the screen
			mypen.undo()
			mypen.penup()
			mypen.hideturtle()
			
			mypen.setposition(-290,310)
			scorestring = "Score is: %s" %score
			mypen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
			
		

	
		
	
	
		
		
	












delay = input("Press Enter to finish")

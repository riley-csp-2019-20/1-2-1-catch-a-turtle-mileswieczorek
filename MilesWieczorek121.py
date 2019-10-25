# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
trtlshape = "turtle"
turtlesize = 5
trtlcolor = "red"

score = 0
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
miles = trtl.Turtle(shape = trtlshape)
miles.color(trtlcolor)
miles.shapesize(turtlesize)
miles.speed(0)



scorewriter = trtl.Turtle()
scorewriter.ht()
scorewriter.penup()
scorewriter.goto(-350,300)

font_setup = ("Arial", 30, "bold" )
scorewriter.write(score, font = font_setup)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(275,300)







#-----game functions--------
def miles_clicked (x,y):
    print("miles got clicked")
    change_position()
    update_score()
    write()
    countdown()

def change_position():
    miles.penup()
    miles.ht()
    if not timer_up:
      milesx = random.randint(-400,400)
      milesy = random.randint(-300,300)
      miles.goto(milesx,milesy)
      miles.st()

def update_score():
    global score
    score += 1
    print(score)
    scorewriter.clear()
    scorewriter.write(score, font = font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("GAME OVER", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------





wn = trtl.Screen()
wn.bgcolor("green")
miles.onclick(miles_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
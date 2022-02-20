import turtle
import random

#Part A
window = turtle.Screen()
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. 
michelangelo.speed(1)
leonardo.speed(1)
distance = random.randrange(1,101)
michelangelo.forward(distance)
distance = random.randrange(1,101)
leonardo.forward(distance)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(1,11):
  distance1 = random.randrange(0,11)
  distance2 = random.randrange(0,11)
  michelangelo.forward(distance1)
  leonardo.forward(distance2)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#Part B
michelangelo.goto(-25,50)
michelangelo.down()
for i in range(1,4):
  michelangelo.forward(100)
  michelangelo.right(360/3)
michelangelo.clear()
michelangelo.up()

michelangelo.goto(-25,50)
michelangelo.down()
for i in range(1,5):
  michelangelo.forward(100)
  michelangelo.right(360/4)
michelangelo.clear()
michelangelo.up()

michelangelo.goto(-25,50)
michelangelo.down()
for i in range(1,7):
  michelangelo.forward(75)
  michelangelo.right(360/6)
michelangelo.clear()
michelangelo.up()

michelangelo.goto(-25,50)
michelangelo.down()
for i in range(1,10):
  michelangelo.forward(50)
  michelangelo.right(360/9)
michelangelo.clear()
michelangelo.up()

michelangelo.goto(-25,50)
michelangelo.down()
for i in range(1,13):
  michelangelo.forward(35)
  michelangelo.right(360/12)
michelangelo.clear()
michelangelo.up()

window.exitonclick()
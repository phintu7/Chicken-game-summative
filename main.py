from turtle import *
from random import *

colormode(255)
red = randint(0, 255)
green = randint(0, 255)
blue = randint(0, 255)
color(red, green, blue)
shape("turtle")

def randomplace(x, y):
    penup()
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)
    goto(x, y)
    pendown()

# Explicitly set up the screen object
screen = Screen()
screen.listen()
screen.onscreenclick(randomplace)
def draw():
  
    # Dictionary of letters and their encoded shape
    code = {
        'a': ['shape 3', 150, 'pink'],
        'b': ['shape 3', 50, 'yellow'],
        'c': ['shape 2', 75, 'astronaut'],
        'd': ['shape 2', 80, 'astropi'],
        'e': ['shape 1', 20, 'orange'],
        'f': ['shape 2', 80, 'satellite'],
        'g': ['shape 1', 10, 'purple'],
        'h': ['shape 1', 300, 'green'],
        'i': ['shape 1', 200, 'orange'],
        'j': ['shape 2', 90, 'astropi'],
        'k': ['shape 1', 12, 'purple'],
        'l': ['shape 3', 43, 'pink'],
        'm': ['shape 1', 93, 'orange'],
        'n': ['shape 1', 64, 'green'],
        'o': ['shape 3', 85, 'blue'],
        'p': ['shape 2', 10, 'astropi'],
        'q': ['shape 3', 45, 'blue'],
        'r': ['shape 1', 70, 'purple'],
        's': ['shape 1', 36, 'orange'],
        't': ['shape 2', 74, 'astronaut'],
        'u': ['shape 1', 58, 'grey'],
        'v': ['shape 3', 78, 'yellow'],
        'w': ['shape 1', 24, 'orange'],
        'x': ['shape 2', 14, 'astropi'],
        'y': ['shape 1', 67, 'purple'],
        'z': ['shape 2', 70, 'astropi'],
        ' ': ['shape 3', 25, 'pink'],
    }
  

   
    no_stroke()
    draw_background()

    name = name.lower() # Change the input to lowercase

    message = [] # Initialise the message list

    for letter in name:
        message.append(code[letter]) # Encode each letter with a shape and add it to a list

    for item in message: # For each letter in the message, draw a shape
        if item[0] == 'shape 1':
            shape_1(item[1], item[2])
        elif item[0] == 'shape 2':
            shape_2(item[1], item[2])
        elif item[0] == 'shape 3':
            shape_3(item[1], item[2])

print('Enter your name to make some encoded artwork:')
name = input()


mainloop()
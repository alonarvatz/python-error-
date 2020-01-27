import turtle
import random
import time


c = ["red","yellow","blue","white","orange","green","purple"]
r = random.choice(c)


ts = turtle.Screen()
ts.title("random bgcolor")
ts.bgcolor(r)
ts.setup(width=800, height=600)
ts.tracer(0)

#game exit code
globals
game = True

# Functions
def randombg():
    r = random.choice(c)

def exitcode():
    globals
    game = False
   
# Keyboard bindings
ts.onkeypress(randombg, "r")
ts.onkeypress(exitcode, "exit")
# Main loop
while game:
    ts.update()
    ts.bgcolor(r)
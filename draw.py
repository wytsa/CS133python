# draw.py
# this program is intended to draw a picture with turtl

import turtle

def main():
    print("This pogram draws something with turtle")
    n = eval(input("how many iterations? "))
    turn = 90
    length = eval(input("how long is the line to start? "))
    i = 0
    pLength = length
    for i in range(n):
        turtle.forward(length)
        turtle.left(turn)
        turtle.forward(length)
        turtle.left(turn)
        turtle.forward(length)
        turtle.left(turn)
        turtle.forward(length)
        turtle.left(turn)
        turtle.forward(length)
        turtle.left(turn)
        turtle.forward(length)
        
        # turtle.backward(length)
        # turtle.right(-1 * turn)
        if i < 1:
            length = length
            
        else:
            #if i < 2:
            pLength = length
            
            length = length + pLength
                
##            else:
##                pLength = length
##                length = length + pLength
                
        

main()

import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex
#print("oldalak számát adja meg: ")
#n= float(input())
n=8
i=0
while i<n:
    alex.forward(50)
    alex.left(360/n)
    i=i+1
print("end")           # tell alex to move forward by 150 units
               # turn by 90 degrees
            # complete the second side of a rectangle



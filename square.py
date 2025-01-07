import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle (1 is slowest, 10 is fastest)
t.speed(1)

# Loop to draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)     # Turn right by 90 degrees

# Close the turtle graphics window when clicked
turtle.done()

import turtle as trtl
import random as rand

# -------------------------------------
# Config

dot_size = 5
rows = 25
cols = 40
start_x = -cols * dot_size
start_y = rows * dot_size

dot_drawer = trtl.Turtle()
dot_drawer.speed(0)
dot_drawer.penup()
dot_drawer.hideturtle()
dot_drawer.screen.tracer(0, 0) #stops animation
# -------------------------------------

# -------------------------------------
# Draw the grid by rows

for row in range(rows):
    grid_row = []
    y = start_y - row * (dot_size * 2)
    for col in range(cols):
        x = start_x + col * (dot_size * 2)
        dot_drawer.goto(x, y)
        dot_drawer.dot(dot_size)
        grid_row.append((x, y))

dot_drawer.screen.update()  # Update the screen once after all dots are drawn
dot_drawer.speed(10) #we want to see it being drawn
dot_drawer.screen.tracer(1, 0) #this re-enables animation

# -------------------------------------


# -------------------------------------
# Select and change a random dot

# Use a separate turtle for stamping (faster than dot)
stamp_turtle = trtl.Turtle()
stamp_turtle.hideturtle()
stamp_turtle.penup()
stamp_turtle.speed(0)
stamp_turtle.shape("circle")

for i in range(4000):
    # Select a random row and column
    rand_row = rand.randint(0, rows - 1)
    rand_col = rand.randint(0, cols - 1)

    # Calculate the coordinates of the selected dot
    selected_x = start_x + rand_col * (dot_size * 2)
    selected_y = start_y - rand_row * (dot_size * 2)

    # Draw a new dot of a different size at the same location (no erase step)
    new_dot_size = rand.randint(dot_size + 2, dot_size * 3)
    stamp_turtle.goto(selected_x, selected_y)
    stamp_turtle.shapesize(new_dot_size / 20.0)  # shapesize is diameter/20
    stamp_turtle.stamp()
# -------------------------------------


wn = trtl.Screen()
wn.mainloop()

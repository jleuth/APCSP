import turtle as trtl
import random as rand

# -------------------------------------
# Config

dot_size = 5
rows = 25
cols = 40
start_x = -cols * dot_size
start_y = rows * dot_size

# Track current size of each dot
dot_sizes = [[dot_size for _ in range(cols)] for _ in range(rows)]

dot_drawer = trtl.Turtle()
dot_drawer.speed(0)
dot_drawer.penup()
dot_drawer.hideturtle()
dot_drawer.screen.tracer(0, 0)
# -------------------------------------

# Draw the grid
for row in range(rows):
    y = start_y - row * (dot_size * 2)
    for col in range(cols):
        x = start_x + col * (dot_size * 2)
        dot_drawer.goto(x, y)
        dot_drawer.dot(dot_size)

dot_drawer.screen.update()
dot_drawer.screen.tracer(5, 0)

stamp_turtle = trtl.Turtle()
stamp_turtle.hideturtle()
stamp_turtle.penup()
stamp_turtle.speed(0)
stamp_turtle.shape("circle")

# Ripple loop
for i in range(100):
    rand_row = rand.randint(0, rows - 1)
    rand_col = rand.randint(0, cols - 1)
    
    # Get surrounding dots
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r = rand_row + dr
            c = rand_col + dc
            if 0 <= r < rows and 0 <= c < cols:
                # Get current size and multiply it
                current = dot_sizes[r][c]
                new_size = current * rand.uniform(0.8, 1.5)  # Random factor
                dot_sizes[r][c] = new_size
                
                x = start_x + c * (dot_size * 2)
                y = start_y - r * (dot_size * 2)
                stamp_turtle.goto(x, y)
                stamp_turtle.shapesize(new_size / 20.0)
                stamp_turtle.stamp()

# Request to a model to write a poem about the abstract art


wn = trtl.Screen()
wn.mainloop()
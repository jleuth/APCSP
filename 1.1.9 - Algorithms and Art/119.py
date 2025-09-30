import turtle as trtl
from PIL import Image

# -----------------------
# Config
target_width = 120 
target_height = 68
dot_spacing = 4  # pixels between dot CENTERS

# Load and resize image
img = Image.open("/Users/239911/Desktop/apcsp/APCSP/1.1.9 - Algorithms and Art/Gorilla Couch.webp") #placeholder for now
img = img.resize((target_width, target_height))
img = img.convert("L")  # Convert to grayscale

# Get image dimensions for centering (adjusted for turtle coordinates)
start_x = -(target_width * dot_spacing) // 2
start_y = (target_height * dot_spacing) // 2

# -----------------------
# Init turtle

wn = trtl.Screen()
wn.setup(width=800, height=600)
matrix_width = target_width * dot_spacing
matrix_height = target_height * dot_spacing
wn.setworldcoordinates(-matrix_width//2 - 50, -matrix_height//2 - 50, matrix_width//2 + 50, matrix_height//2 + 50) # I really dont know what this does, Claude suggested it and it worked.
dot_drawer = trtl.Turtle()
dot_drawer.speed(0)
dot_drawer.penup()
dot_drawer.hideturtle()
wn.tracer(0, 0) # Instant

# -----------------------
# Draw image in halftone style

for row in range(target_height):
    y = start_y - row * dot_spacing 
    for col in range(target_width):
        x = start_x + col * dot_spacing  # Changed from - to + for proper centering

        brightness = img.getpixel((col, row))

        dot_size = ((255 - brightness) / 255) * dot_spacing * 0.9 # Some weird ass brightness mapping and inversion so that darker = bigger dot and vice versa.

        if dot_size > 0.1:
            dot_drawer.goto(x, y)
            dot_drawer.dot(dot_size, 'black')

wn.update()
wn.mainloop()
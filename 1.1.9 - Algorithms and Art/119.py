import turtle as trtl
import PIL as Image

# -----------------------
# Config
target_width = 480 # 480p
target_height = 270
dot_spacing = 4  # pixels between dot centers

# Load and resize image
img = Image.open("img.jpg") #placeholder for now
img = img.resize((target_width, target_height))
img = img.convert("L")  # Convert to grayscale

# Get image dimensions for centering
start_x = -(target_width * dot_spacing) // 2
start_y = (target_height * dot_spacing) // 2

# -----------------------
# Init turtle

screen = trtl.Screen()
screen.setup(width=target_width * dot_spacing + 100, height=target_height * dot_spacing + 100)
dot_drawer = trtl.Turtle()
dot_drawer.speed(0)
dot_drawer.penup()
dot_drawer.hideturtle()
screen.tracer(0, 0) # Instant

# -----------------------
# Draw image in halftone style

for row in range(target_height):
    y = start_y - row * dot_spacing 
    for col in range(target_width):
        x = start_x - col * dot_spacing

        brightness = img.getpixel((col, row))

        dot_size = ((255 - brightness) / 255) * dot_spacing * 0.9 # Some weird ass brightness mapping and inversion
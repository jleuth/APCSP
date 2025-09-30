import turtle as trtl
from PIL import Image
import requests
import json
from dotenv import load_dotenv
import os

# -----------------------
# Config
load_dotenv()
target_width = 120 
target_height = 68
dot_spacing = 4  # pixels between dot CENTERS

def loadImg(path):
    # Load and resize image
    img = Image.open(path)
    img = img.resize((target_width, target_height))
    img = img.convert("L")  # Convert to grayscale
    return img

# Get image dimensions for centering (adjusted for turtle coordinates)
start_x = -(target_width * dot_spacing) // 2
start_y = (target_height * dot_spacing) // 2

# -----------------------
# Image gen if chosen. THIS CODE COPIED FROM https://openrouter.ai/docs/features/multimodal/image-generation
def genImg(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv("OR_KEY")}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "google/gemini-2.5-flash-image-preview",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "modalities": ["image", "text"]
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    # The generated image will be in the assistant message
    if result.get("choices"):
        message = result["choices"][0]["message"]
        if message.get("images"):
            for image in message["images"]:
                image_url = image["image_url"]["url"]  # Base64 data URL
                print(f"Generated image: {image_url[:50]}...")
                

# -----------------------

# -----------------------
# Init turtle
def initTurtle():
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
    return wn, dot_drawer
# -----------------------
# Draw image in halftone style
def drawer():
    for row in range(target_height):
        y = start_y - row * dot_spacing 
        for col in range(target_width):
            x = start_x + col * dot_spacing  # Changed from - to + for proper centering

            brightness = img.getpixel((col, row))

            dot_size = ((255 - brightness) / 255) * dot_spacing * 0.9 # Some weird ass brightness mapping and inversion so that darker = bigger dot and vice versa.

            if dot_size > 0.1:
                dot_drawer.goto(x, y)
                dot_drawer.dot(dot_size, 'black')
# -----------------------


# Prompt the user for an image path
image_path = input('Enter the path to the image file (or type "AI" to generate one): ')
if image_path.strip().upper() == "AI":
    # Prompt for a text prompt to generate an image
    prompt = input("Enter a prompt for the AI-generated image: ")
    image_path = genImg(prompt)  # You must define this function elsewhere

img = loadImg(image_path)
wn, dot_drawer = initTurtle()
drawer()
wn.update()
wn.mainloop()
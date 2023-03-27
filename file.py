from PIL import Image
import random

# Image size in pixels
WIDTH = 2400  # 100 pixels x 24 blocks
HEIGHT = 2400  # 100 pixels x 16 blocks

# Number of color blocks horizontally and vertically
BLOCKS_X = 24
BLOCKS_Y = 24

# Colors used in the camouflage pattern


def generate_random_colors(num_colors):
    """Generate a list of num_colors random RGB color tuples"""
    # colors = [(25, 45, 10), (100, 120, 80), (50, 70, 30)]
    colors = []
    for _ in range(num_colors):
        colors = [(43, 48, 40),  (63, 66, 46),  (49, 57, 42)]
    return colors


colors = generate_random_colors(3)

# Density of the pattern
DENSITY = 1.0

# Create a new image with a black background
img = Image.new('RGB', (WIDTH, HEIGHT), color='black')

# Create a pixel access object for the image
pixels = img.load()

# Generate a random pattern of pixels using the colors
block_size = 100
for x_block in range(BLOCKS_X):
    for y_block in range(BLOCKS_Y):
        # Choose a random color from the list
        color = random.choice(colors)
        # Set the color block
        for x in range(block_size):
            for y in range(block_size):
                if random.random() < DENSITY:
                    x_coord = x_block * block_size + x
                    y_coord = y_block * block_size + y
                    pixels[x_coord, y_coord] = color

# Save the image to a file
img.save('digital_camouflage.png')
img.show()

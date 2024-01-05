import cv2
import numpy as np
from ascii_magic import AsciiArt
from PIL import Image

# Define the character cell size
cell_width = 2
cell_height = 2

# Create a mapping from ASCII characters to pixel arrays
char_to_pixels = {}
for char in set(''.join(ascii_art_frames)):
    # Create a pixel array for the character
    pixels = np.zeros((cell_height, cell_width), dtype=np.uint8)

    # Draw the character onto the pixel array
    cv2.putText(pixels, char, (0, cell_height-1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    # Add the character and pixel array to the mapping
    char_to_pixels[char] = pixels

# Convert the ASCII art frames into pixel arrays
ascii_art_frames_pixels = []
for frame in ascii_art_frames:
    # Create a pixel array for the frame
    frame_pixels = np.zeros((cell_height * len(frame), cell_width * len(frame[0])), dtype=np.uint8)

    # Draw the characters onto the pixel array
    for i, row in enumerate(frame):
        for j, char in enumerate(row):
            frame_pixels[i*cell_height:(i+1)*cell_height, j*cell_width:(j+1)*cell_width] = char_to_pixels[char]

    # Add the frame pixel array to the list
    ascii_art_frames_pixels.append(frame_pixels)
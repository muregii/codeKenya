import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import os

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "

# Width & Height of ASCII output
WIDTH = 120
HEIGHT = 35

def frame_to_ascii(frame):
    img = Image.fromarray(frame).convert("L")  # Convert to grayscale

    # Enhance image
    img = ImageEnhance.Contrast(img).enhance(2.6)
    img = ImageEnhance.Brightness(img).enhance(1.15)

    # Edge + sharpen
    edge = img.filter(ImageFilter.FIND_EDGES)
    sharp = img.filter(ImageFilter.SHARPEN)
    img = Image.blend(sharp, edge, 0.5)

    # Resize
    img = img.resize((WIDTH, HEIGHT))
    pixels = np.array(img)

    ascii_img = [
        "".join(ASCII_CHARS[int(p / 256 * len(ASCII_CHARS))] * 2 for p in row)
        for row in pixels
    ]
    return "\n".join(ascii_img)

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def run_ascii_video():
    cap = cv2.VideoCapture("video.mp4")  # Use webcam. To use a video, replace 0 with "video.mp4"
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
            ascii_art = frame_to_ascii(frame)

            clear_terminal()
            print(ascii_art)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()

if __name__ == "__main__":
    run_ascii_video()

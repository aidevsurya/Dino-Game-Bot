import pyautogui
from PIL import ImageGrab
import time

# Obstacle detection area (adjusted for 1366x768 resolution)
# This is a small rectangle just ahead of the Dino character
OBSTACLE_REGION = (530, 290, 535, 305)  # x1, y1, x2, y2

def detect_obstacle():
    img = ImageGrab.grab(bbox=OBSTACLE_REGION)
    gray = img.convert('L')
    pixels = gray.getdata()
    for pixel in pixels:
        if pixel < 100:  # Obstacle detected (dark pixel)
            return True
    return False

def jump():
    pyautogui.press('space')

print("Bot starting in 3 seconds... Open https://chromedino.com and switch to the game tab!")
time.sleep(3)

try:
    while True:
        if detect_obstacle():
            jump()
            time.sleep(0.1)
except KeyboardInterrupt:
    print("Bot stopped.")

This is a simple Python bot that automatically plays the Dino game on https://chromedino.com/ by detecting obstacles and jumping at the right moment. It uses PyAutoGUI and Pillow for screen capture and automation. <br>

# Features
Detects obstacles (cacti or flying birds)<br>

Automatically jumps when an obstacle is detected<br>

Works with the Dino game in Chrome (offline or on https://chromedino.com/)<br>

Supports 1366x768 screen resolution<br>

# Requirements
To run the Dino bot, you'll need Python and some packages installed on your system.<br>

1. Install Python (if you don't have it already)<br>
Download and install Python from python.org.<br>

2. Install Dependencies<br>
Use pip to install the required Python packages. Open your terminal or command prompt and run the following commands:<br>
<code>
pip install pyautogui pillow
</code>
pyautogui: Automates keyboard and mouse actions (e.g., pressing space to jump).<br>

Pillow: Used for screen capture and image processing.<br>

# How to Use
1. Open Dino Game<br>
Open Google Chrome and go to https://chromedino.com.<br>

Alternatively, if you're offline, just type chrome://dino in the address bar to launch the game.<br>

Ensure that your browser is in fullscreen mode and zoom is set to 100% for better accuracy.<br>

2. Run the Script<br>
Open a terminal or command prompt.<br>

Navigate to the folder where you saved the Python script (dino_bot.py).<br>

# Run the script:
<code>
python dino_bot.py
</code>
After a 3-second delay, the bot will automatically start. Focus on the Dino game window, and it will start jumping over obstacles by itself!<br>

3. Stopping the Bot<br>
To stop the bot, simply press Ctrl + C in the terminal/command prompt.<br>

# How It Works
The script captures a small region of the screen, right in front of the Dino character, to check for obstacles.<br>

When an obstacle (like a cactus or a flying bird) appears in this region, the bot sends the space key press to make the Dino jump.<br>

The bot works based on grayscale image processing, detecting dark pixels in the captured region to identify obstacles.<br>

#Troubleshooting
The Dino is not jumping at the right time: If the bot is missing jumps, try adjusting the OBSTACLE_REGION coordinates in the script. You can change the values (530, 290, 535, 305) to better match where the obstacles appear on your screen.<br>

To find the best coordinates, you can use the following helper script to print out your mouse position:<br>

<code>
import pyautogui
import time

print("Move your cursor to the obstacle area in the Dino game window. Coordinates will be printed in 5 seconds...")
time.sleep(5)
print(pyautogui.position())
</code>
Bot doesn't work in full-screen: Make sure you're using the correct screen resolution and the game window is properly positioned. If needed, adjust the OBSTACLE_REGION coordinates.<br>

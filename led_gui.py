import RPi.GPIO as GPIO
import tkinter as tk

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define LED pins
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

# Set up LED pins as outputs and initialize all LEDs off
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.output(RED_PIN, GPIO.LOW)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(BLUE_PIN, GPIO.LOW)

# Functions to control LEDs
def turn_on_red():
    GPIO.output(RED_PIN, GPIO.HIGH)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)

def turn_on_green():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.HIGH)
    GPIO.output(BLUE_PIN, GPIO.LOW)

def turn_on_blue():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.HIGH)

def exit_program():
    GPIO.cleanup()
    window.destroy()

# Create the GUI window
window = tk.Tk()
window.title("LED Controller")

# Create buttons for each LED and exit
button_red = tk.Button(window, text="Red", command=turn_on_red)
button_red.pack(pady=5)

button_green = tk.Button(window, text="Green", command=turn_on_green)
button_green.pack(pady=5)

button_blue = tk.Button(window, text="Blue", command=turn_on_blue)
button_blue.pack(pady=5)

button_exit = tk.Button(window, text="Exit", command=exit_program)
button_exit.pack(pady=20)

# Start the GUI event loop
window.mainloop()

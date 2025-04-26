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

# Function to control LEDs based on text input
def set_led_color():
    color = entry.get().lower()  # Read user input and convert to lowercase
    if color == "red":
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.LOW)
    elif color == "green":
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        GPIO.output(BLUE_PIN, GPIO.LOW)
    elif color == "blue":
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.HIGH)
    else:
        print("Invalid color input. Please enter red, green, or blue.")

# Function to exit program
def exit_program():
    GPIO.cleanup()
    window.destroy()

# Create the GUI window
window = tk.Tk()
window.title("LED Controller by Text Input")

# Create Entry widget for text input
entry = tk.Entry(window)
entry.pack(pady=10)

# Create Submit button
submit_button = tk.Button(window, text="Submit", command=set_led_color)
submit_button.pack(pady=5)

# Create Exit button
exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()

import RPi.GPIO as GPIO

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up LED pin
led_pin = 21
GPIO.setup(led_pin, GPIO.OUT)

while True:
    # Get user input
    user_input = input("Enter 1 to turn on the LED, or 2 to turn it off: ")

    if user_input == "1":
        # Turn on the LED
        GPIO.output(led_pin, GPIO.HIGH)
    elif user_input == "2":
        # Turn off the LED
        GPIO.output(led_pin, GPIO.LOW)
    else:
        # Invalid input
        print("Invalid input. Please enter 1 or 2.")

# Clean up GPIO
GPIO.cleanup()

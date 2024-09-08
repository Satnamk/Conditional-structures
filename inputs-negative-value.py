# Constant for conversion factor
INCH_TO_CM = 4.26

# Start the loop
while True:
    # Ask the user to input a value in inches
    inches = float(input("Enter length in inches (negative value to quit): "))

    # Check if the input is negative
    if inches < 0:
        print("Negative value entered. Program ending.")
        break

    # Convert inches to centimeters
    centimeters = inches * INCH_TO_CM
    print(f"{inches} inches is {centimeters:.2f} cm.")

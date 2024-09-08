# Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to release the fish
# back into the lake and notifies the user of how many centimeters below the size limit the caught
# fish was. A zander must be 42 centimeters or longer to meet the size limit.

# Solution:

# Size limit for a zander
SIZE_LIMIT = 42

# Ask the user for the length of the zander
zander_length = float(input("Enter the length of the zander in centimeters: "))

# Check if the zander meets the size limit
if zander_length >= SIZE_LIMIT:
    print("The zander meets the size limit. You can keep the fish!")
else:
    difference = SIZE_LIMIT - zander_length
    print(f"The zander is {difference:.2f} cm below the size limit. Please release the fish back into the lake.")

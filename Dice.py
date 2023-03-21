import random

# Define the dice format
dice_format = [
    "+-------+",
    "|       |",
    "|   {}   |",
    "|       |",
    "+-------+"
]

# Define a function to roll the dice
def roll_dice():
    # Select a random number between 1 and 6
    dice_roll = random.randint(1, 6)

    # Print the dice roll in dice format
    print("\n".join(dice_format).format(dice_roll))

    # Return the dice roll
    return dice_roll

# Roll the dice and print the result
result = roll_dice()
print("You rolled a", result)

# Prompt the user to roll again
reroll = input("Would you like to roll again? (yes or no): ")

while reroll.lower() == "yes":
    # Roll the dice and print the result
    result = roll_dice()
    print("You rolled a", result)

    # Prompt the user to roll again
    reroll = input("Would you like to roll again? (yes or no): ")

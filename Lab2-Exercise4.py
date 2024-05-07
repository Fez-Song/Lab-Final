import random


def roll_dice():
    return random.randint(1, 7)


if __name__ == "__main__":
    try:
        num_rolls = int(input("Enter the number of dice rolls you want to simulate: "))
        if num_rolls <= 0:
            print("Please enter a positive number.")
        else:
            print(f"Simulating {num_rolls} dice rolls...")
            for i in range(1, num_rolls + 1):
                result = roll_dice()
                print(f"Roll {i}: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number of dice rolls.")

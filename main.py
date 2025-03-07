from random import randint
import time
import json

attempts = 0
all_attempts = 0
number = randint(1, 100)
start_time = 0
difficulty_type = ""

try:
    with open("records.json", "r") as f:
        records = json.load(f)
except (json.decoder.JSONDecodeError, FileNotFoundError):
    with open("records.json", "w") as f:
        records = {}

print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100\n"
      "You have N chances to guess the correct number.\n")

if input("Show best results? y/n: ").lower() == "y":
    if records:
        for key, val in records.items():
            print(f"{key}: {val['attempts']} attempts, {val['time']:.3f} seconds, {val['difficulty']} difficulty")
    else:
        print("No results available.")
    print("\n")


def difficulty():
    global attempts, all_attempts, start_time, difficulty_type

    difficulties = {"1": [10, "Easy"], "2": [5, "Medium"], "3": [3, "Hard"]}

    while True:
        print("Please select the difficulty level:\n"
              "1. Easy (10 chances)\n"
              "2. Medium (5 chances)\n"
              "3. Hard (3 chances)\n")

        diff = input("Enter your choice: ")
        if diff in difficulties:
            all_attempts, difficulty_type = difficulties[diff]
            print(f"Great! You have selected {difficulty_type} difficulty.\nLet's start the game!")
            start_time = time.time()
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")


def guessing():
    global attempts, all_attempts

    low, high = 1, 100

    while attempts < all_attempts:

        if attempts >= all_attempts - 2:
            shift = randint(-3, 3)
            hint_low = max(1, number - 10 + shift)
            hint_high = min(100, number + 10 + shift)
            print(f"The number is between {hint_low} and {hint_high}.\n")

        user_input = input("Enter your guess: ")

        if user_input.isdigit():
            user_input = int(user_input)

            if user_input > 100 or user_input < 0:
                print("Enter correct number\n")
                continue

            if user_input == number:
                time_record = time.time() - start_time
                record_types = {"best time": lambda rec: time_record < rec['time'],
                                "least attempts": lambda rec: attempts < rec['attempts']}

                for key, condition in record_types.items():
                    if key in records:
                        if condition(records[key]):
                            records[key] = {"attempts": attempts, "time": time_record, "difficulty": difficulty_type}
                            print(f"New record for {key}!")

                    else:
                        records[key] = {"attempts": attempts, "time": time_record, "difficulty": difficulty_type}

                if "best" not in records or time_record < records["best"]["time"] and attempts < records["best"]["attempts"]:
                    records["best"] = {"attempts": attempts, "time": time_record, "difficulty": difficulty_type}
                    print("Best performance")

                print(f"Congratulations! You guessed the correct number in {attempts} attempts and {time_record:.3f} secs.")

                with open("records.json", "w") as f:
                    json.dump(records, f, indent=4)

                if input("Play again? y/n: ").lower() == "y":
                    reset_game()
                else:
                    exit()

            if user_input < number:
                print(f"Incorrect! The number is greater than {user_input}\n")
                low = max(low, user_input + 1)
                attempts += 1

            else:
                print(f"Incorrect! The number is less than {user_input}\n")
                high = min(high, user_input - 1)
                attempts += 1


        else:
            print("Enter the number\n")

    print("All attempts were wasted! The correct number was:", number)
    if input("Play again? y/n: ").lower() == "y":
        reset_game()
    else:
        exit()


def reset_game():
    global attempts, number, start_time
    attempts = 0
    number = randint(1, 100)
    difficulty()
    guessing()



difficulty()

guessing()

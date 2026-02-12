import random
MIN_NUMBER = 1
MAX_NUMBER = 100

def get_valid_guess():
    while True:
        guess_text = input("Enter Your Guess:")
        try:
            guess = int(guess_text)
            if guess > MAX_NUMBER or guess < MIN_NUMBER:
                raise ValueError()
            return guess
        except:
            print("That is not a valid guess. Please try again.")



def play_picker():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"Computer picked {number}. Shhh.")
    while True:
        guess = get_valid_guess()
        if guess > number:
            print("You got it right! Thats a first.")
            break
        elif guess > number:
            print


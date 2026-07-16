import random

n = random.randint(1, 100)
#print("Secret number =", n)   # Testing ke liye

a = -1
guesses = 0

while a != n:
    guesses += 1
    a = int(input("Guess the number: "))

    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")
    else:
        print("Correct!")

print(f"You guessed the number {n} correctly in {guesses} attempts.")
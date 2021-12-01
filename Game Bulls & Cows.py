import random
import time

separator = "-" * 60

# Kontrola duplicity
def dupl_check(x):
    my_set = set()
    for char in x:
        my_set.add(char)
    if len(my_set) != len(x):
        return False
    else:
        return True

# # Generování náhodného čísla
def unique_answer(answer):
    while True:
        if dupl_check(answer) == False:
            answer = (str(random.randrange(1000, 9999)))
        else:
            return answer

# Kontrola složení
def num_check(x):
    for char in x:
        if char.isnumeric() != True:
            return False


# Kontrola tipu
def tip_check(tip):
    if len(tip) != 4:
        print("Your number is too short or too long")
        tip = input("Enter a new number: ")
        tip_check(tip)
    elif dupl_check(tip) == False:
        print("There are at least two same charachters in your number")
        tip = input("Enter a new number: ")
        tip_check(tip)
    elif tip[0] == "0":
        print("Your number cannot start with 0")
        tip = input("Enter a new number: ")
        tip_check(tip)
    elif num_check(tip) == False:
        print("You can only enter numbers")
        tip = input("Enter a new number: ")
        tip_check(tip)
    return tip


# Porovnání tipu se správnou odpovědí
def compare(tip, answer):
    index, bulls, cows = 0, 0, 0
    for num in tip:
        if num == answer[index]:
            bulls += 1
            index += 1
        elif num in answer:
            cows += 1
            index += 1
        else:
            index += 1
    return bulls, cows


# Vypsání výsledku porovnání
def result(bulls, cows):
    bulls = compare(tip, answer)[0]
    cows = compare(tip, answer)[1]
    if bulls < 2 and cows < 2:
        print(f"{bulls} bull, {cows} cow")
    elif bulls < 2 and cows >= 2:
        print(f"{bulls} bull, {cows} cows")
    elif bulls >= 2 and cows < 2:
        print(f"{bulls} bulls, {cows} cow")
    else:
        print(f"{bulls} bulls, {cows} cows")


# Uvítání
print(f"""Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls & cows game!

If you need to see the right answer, write SHOW.
{separator}""")


# Hádání
while True:
    answer = unique_answer(str(random.randrange(1000, 9999)))
    guesses = 0
    start = time.time()
    while True:
        tip = input("Enter a number: ").upper()
        if tip == "SHOW":
            print(f"The answer is {answer}. You lost! :(")
            break
        else:
            tip = tip_check(tip)
            compare(tip, answer)
            result(compare(tip, answer)[0], compare(tip, answer)[1])
        print(separator)
        guesses += 1
        if tip == answer:
            end = time.time()
            print(f"""Correct! You have guessed the right number in {guesses} guesses!
It took you {round((end - start), 2)} seconds.
""")
            break
    restart = input("Would you like to play again? Write YES. To finish, press Enter. ").upper()
    if "YES" in restart:
        continue
    else:
        print("Have a nice day! :)")
        time.sleep(5)
        break

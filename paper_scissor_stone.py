import random

def play():
    user = input("what's your choice?: 'p' for paper, 'sc' for scissor, 'st' for stone\n")
    computer = random.choice(['p', 'sc', 'st'])
    print(f"computer picked {computer}")

    if user == computer:
        print("tie")
    elif (user == 'p' and computer == 'st') \
        or (user == 'sc' and computer == 'p') \
        or (user == 'st' and computer == 'sc'):
        print("you won!!!")
    else:
        print("you lost!!!")
play()
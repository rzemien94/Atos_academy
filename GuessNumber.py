from random import randint


def playGuessNumber():
    x = randint(1, 50)
    guess_num = randint(1, 51)
    print('Guess a number between 1-50')
    counter = 0

    while True:
        counter += 1
        try:
            temp = int(input("podaj liczbe 1-50: (-1 to exit)"))
        except ValueError as e:
            print("you should give an int value")
            continue
        if temp == guess_num or temp == -1:
            print(f"congrats, you won after: {counter} moves!")
            break
        if temp > guess_num:
            print('to much')
            continue
        print('not enough')
        continue
    print('This game is over')


while True:
    playGuessNumber()
    decision = input('Do you want to play again? choose "t" if yes:')
    if decision != 't':
        break

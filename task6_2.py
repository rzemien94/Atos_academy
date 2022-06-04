from random import randint

x=randint(1,50)
guess_num=randint(1,51)
still_playing=True
print('Guess a number between 1-50')
counter=0

while still_playing:
    counter+=1
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
    else:
        print('not enough')
        continue
print('end of game')

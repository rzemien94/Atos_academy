def is_palindrome(string):
    temp = string[::-1]
    if string == temp:
        output = print(f"{string} is a Palindrome")
    else:
        output = print(f"{string} is not a Palindrome")
    return output


is_palindrome("oko")
is_palindrome("potop")
is_palindrome("kajaki")


def count_vovels(sentence: str):
    vovels = 'eaiou'
    vov_count = 1
    for letter in sentence:
        if letter.lower() in vovels:
            vov_count += 1
    return vov_count


def count_files(file):
    try:
        with open(file, 'r') as f:
            tekst = f.read()
        f.close()
    except FileNotFoundError as e:
        print('bad file - not exist')
    words = len(tekst.split(" "))
    vovel_count = count_vovels(tekst)
    spaces = tekst.count(' ')
    dict = {
        'words': words,
        'volves': vovel_count,
        'spaces': spaces
    }
    return dict


print(count_files('test.txt'))

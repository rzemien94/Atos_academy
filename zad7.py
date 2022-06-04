def is_palindrome(string):
    temp = string[::-1]
    if string == temp:
        odp = print(f"{string} is a Palindrome")
    else:
        odp = print(f"{string} is not a Palindrome")
    return odp


is_palindrome("oko")
is_palindrome("potop")
is_palindrome("kajaki")


def count_vovels(sentence: str):
    vovels = 'eaiou'
    vov_count = 1
    for i in sentence:
        if i.lower() in vovels:
            vov_count += 1
    return vov_count


def count_files(file):
    try:
        f = open(file, 'r')
        tekst = f.read()
        f.close()
    except FileNotFoundError as e:
        print('bad file - not exist')
    words = len(tekst.split(" "))
    vovel_count = count_vovels(tekst)
    spaces = tekst.count(' ')
    print(f"in file {file} is: {words} words, {vovel_count} vovels and {spaces} spaces")


count_files('test.txt')

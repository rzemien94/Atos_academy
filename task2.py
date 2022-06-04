def wow(number: int):
    word="W"
    for i in range(number):
        word=word+ "o"

    word= word+"w"
    return word
    #raise NotImplementedError

assert wow(1) == 'Wow'
assert wow(4) == 'Woooow'
assert wow(0) == 'Ww'

def check_pattern(sentence: str, pattern: str):
    result='YES' if pattern in sentence else 'NO'
    return result
    #raise NotImplementedError

assert check_pattern('AABBABA', 'BBAA') == 'NO'
assert check_pattern('AAABBB','BBBAAA') == 'NO'
assert check_pattern('AABB','ABB') == 'YES'
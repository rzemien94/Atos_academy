from typing import List

def is_the_same(input_list: List[any]):
    print(input_list)
    flag=True
    for i in range(len(input_list)):
        if input_list[i] != input_list[0]:
            flag=False
    return flag

assert is_the_same([1,1,1]) == True
assert is_the_same([1,2,1]) == False
assert is_the_same([True]) == True
assert is_the_same(['blue','blue']) == True
assert is_the_same([2,'red']) == False

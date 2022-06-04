def compare_two_numbers(a: int, b: int):
    if a < b:
        odp=(f"{a} is smaller than {b}")
    elif a > b:
        odp = (f"{a} is greater than {b}")
    else:
        odp = (f"a is equal b: 0")
    return odp

#assert compare_two_numbers(2,6) == '2 is smaller than 6'
#assert compare_two_numbers(4, -5) == '4 is greater than -5'
#assert compare_two_numbers(100,100) == 'a is equal b: 0'

from typing import List, Tuple

def sort_list(input_list: List[Tuple]):
    return(sorted(input_list, key=lambda x: x[1]))

assert sort_list([('Ania',20),('Monika',110),('Piotr',10)]) == [('Piotr',10),('Ania',20),('Monika',110)]
assert sort_list([('Ania',-10),('Monika',-110),('Piotr',210)]) == [('Monika',-110),('Ania',-10),('Piotr',210)]
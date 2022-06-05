from collections import Counter

import requests
from bs4 import BeautifulSoup as soup


def letter_count(text):
    return Counter(c for c in text.lower() if c.isalpha())


def count_vovels(data: str) -> int:
    vovel_number = 0
    for letter in data:
        if letter in ('a', 'e', 'o', 'u', 'i', 'y', 'ą', 'ę', 'ó'):
            vovel_number += 1
    return vovel_number


# l.samoglosek
# najczesceij pojawiajaca sie litera
# ilosc slow
# ilośc znaczników "p"
# ilość znaczników "a" posaidających link do jakiejś strony

def get_statistics(url: str) -> dict:
    response = requests.get(url)

    if response.status_code != 200:
        print('nie otrzymano odpowiedzi')
        return

    html_data = soup(response.text, 'html.parser')
    word_counter = 0
    vovels_counter = 0
    letter_counter = dict()

    for a in html_data.find_all("a"):
        text = a.text
        number_of_words = len(text.split(' '))
        word_counter += number_of_words
        number_of_vovels = count_vovels(text)
        vovels_counter += number_of_vovels
        dict_of_letters = letter_count(text)
        for letter, value in dict_of_letters.items():
            if letter_counter.get(letter, None):
                letter_counter[letter] += value
            else:
                letter_counter[letter] = value
    most_frequent_letter = max(letter_counter, key=letter_counter.get)

    return {
        'number of words': word_counter,
        'number of vovels': vovels_counter,
        'most letter': f"most frequent letter is '{most_frequent_letter}', {letter_counter[most_frequent_letter]}"
    }

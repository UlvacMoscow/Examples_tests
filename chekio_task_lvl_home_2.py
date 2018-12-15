"""
     You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
    While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

    If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

    Input: A text for analysis as a string.

    Output: The most frequent letter in lower case as a string.

    Example:

    checkio("Hello World!") == "l"
    checkio("How do you do?") == "o"
    checkio("One") == "e"
    checkio("Oops!") == "o"
    checkio("AAaooo!!!!") == "a"
    checkio("abe") == "a"

"""



def checkio(text: str) -> str:
    text = "".join([x for x in text if 64 < ord(x) < 123]).lower()
    char_count_dict = {key: value for key,value in zip(text,[text.count(x) for x in text])}
    max_values = max(char_count_dict.values())
    new_dict = {}
    for elem in char_count_dict:
      if char_count_dict[elem] == max_values:
        new_dict[elem] = max_values
    return min(new_dict)


print(checkio('Hhhellow woedsfsdgk1111!!!')) # h
print(checkio('One')) # e
print(checkio("AAaooo!!!!")) # a
print(checkio("abe")) # a



""""решение с регуляркой"""
# import re

# def checkio(text: str) -> str:
# clean = ''.join(sorted(re.compile('[^a-zA-Z]').sub('', text.lower())))
# result = max(clean, key=clean.count)
# print(result)
# return result

""" Но надо понимать что если  delta > 26 по модулю,
    то его надо обработать разделить на 26 и взять остаток
    и с ним производить манипуляции"""


def to_encrypt(text, delta):
    temp = ''
    for char in text:
        if char == ' ':
            temp += char
        if char.isalpha():
            if ord(char) + delta < 97:
                temp += chr((ord(char) + (26 + delta)))
            elif ord(char) + delta > 122:
                temp += chr((ord(char) - (26 - delta)))
            else:
                temp += chr((ord(char) + delta))
    return temp

print(ord('a'), ord('z'))
print(chr(97), chr(122))

print(to_encrypt('abc', 10))
print(to_encrypt("a b c", 3))
print(to_encrypt("a b c", -3))
print(to_encrypt("simple text", 16))
print(to_encrypt("important text", 10))
print(to_encrypt("state secret", -13))

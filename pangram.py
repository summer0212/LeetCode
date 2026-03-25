import string

alphabet_list = []
lowercase_alphabet_list = list(string.ascii_lowercase)
# uppercase_alphabet_list = list(string.ascii_uppercase)


def is_pangram(sentence):
    sentence = sentence.lower()
    # sentence = sentence.spl
    for char in lowercase_alphabet_list:
        if char not in sentence:
            return False

    return True
            

print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(list(string.ascii_lowercase))
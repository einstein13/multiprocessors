from random import randint

def key_generator(length, dictionary=None):
    # length is int
    # dictionary is str
    if dictionary is None:
        dictionary = "23456789abcdefghijkmnopqrstwxyzABCDEFGHJKLMNPQRSTWXYZ"
    dictionary_length = len(dictionary) - 1
    result = ""
    for el in range(length):
        result += dictionary[randint(0, dictionary_length)]
    return result

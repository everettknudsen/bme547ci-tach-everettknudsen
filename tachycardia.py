import string


def is_tachycardic():
    word = input('Give me something that might be tachycardia:')

    no_punctuation = remove_punctuation(word)
    no_spaces = remove_spaces(no_punctuation)
    print(lowercase_all(no_spaces))


def remove_punctuation(word):
    res = ""
    for char in word:
        if char not in string.punctuation:
            res += char
    return res


def remove_spaces(word):
    stripped = word.strip()
    return stripped


def lowercase_all(word):
    lower = word.lower()
    return lower


if __name__ == "__main__":
    is_tachycardic()

import string


def is_tachycardic():
    word = input('Input tachycardic information:')

    no_punctuation = remove_punctuation(word)
    no_spaces = remove_spaces(no_punctuation)
    all_lower = lowercase_all(no_spaces)
    print(string_to_set_and_check(all_lower))


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


def string_to_set_and_check(word):
    tachy_set = set('tachycardic')
    input_set = set(word)
    common = tachy_set.intersection(input_set)
    number_of_common = len(common)
    if number_of_common > 6:
        answer = True
    else:
        answer = False
    return answer


if __name__ == "__main__":
    is_tachycardic()

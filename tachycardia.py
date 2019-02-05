def is_tachycardic():

    word = input('Give me something that might be tachycardia:')

    remove_spaces(word)


def remove_spaces(word):
    stripped = word.strip()
    return stripped


if __name__ == "__main__":
    is_tachycardic()

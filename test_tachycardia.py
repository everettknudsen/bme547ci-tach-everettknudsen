import pytest


@pytest.mark.parametrize("word, expected", [
    ('...dog...', 'dog'),
    (':,;;tachycardia----', 'tachycardia'),
    ('!@#$heartproblem#$%^', 'heartproblem'),
])
def test_punctuation_removal(word, expected):
    from tachycardia import remove_punctuation
    answer = remove_punctuation(word)
    assert answer == expected


@pytest.mark.parametrize("word, expected", [
    ('   dog   ', 'dog'),
    ('tachycardia    ', 'tachycardia'),
    ('     heart problem  ', 'heart problem'),
])
def test_space_removal(word, expected):
    from tachycardia import remove_spaces
    answer = remove_spaces(word)
    assert answer == expected


@pytest.mark.parametrize("word, expected", [
    ('TaChYcArDiA', 'tachycardia'),
    ('walterBenjamin', 'walterbenjamin'),
    ('letsGODUKE', 'letsgoduke')
])
def test_lowercase_all(word, expected):
    from tachycardia import lowercase_all
    answer = lowercase_all(word)
    assert answer == expected


@pytest.mark.parametrize("word, boolean", [
    ('tachycardic', True),
    ('tachycard1c', True),
    ('tacycardic', True),
    ('tachcardic', True)
])
def test_true_string_to_set_and_check(word, boolean):
    from tachycardia import string_to_set_and_check
    answer = string_to_set_and_check(word)
    assert answer == boolean


@pytest.mark.parametrize("word, boolean", [
    ('glacoma', False),
    ('achycar', False),
    ('3acycar415', False),
    ('livercancer', False)
])
def test_false_string_to_set_and_check(word, boolean):
    from tachycardia import string_to_set_and_check
    answer = string_to_set_and_check(word)
    assert answer == boolean

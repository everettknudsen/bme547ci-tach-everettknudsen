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


def test_true_match():
    from tachycardia import check_for_match
    answer = check_for_match('tachycardic')
    expected = True
    assert answer == expected


def test_false_match():
    from tachycardia import check_for_match
    answer = check_for_match('bradycardia')
    expected = False
    assert answer == expected

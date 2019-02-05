import pytest


@pytest.mark.parametrize("word,expected", [
    ('   dog   ', 'dog'),
    ('tachycardia    ', 'tachycardia'),
    ('     heart problem  ', 'heart problem'),
])
def test_space_removal(word, expected):
    from tachycardia import remove_spaces
    answer = remove_spaces(word)
    assert answer == expected

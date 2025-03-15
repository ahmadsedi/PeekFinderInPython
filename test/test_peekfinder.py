from src.peekfinder import find_peek


def test_find_peek_given_non_empty_list():
    values = [1, 2, 5, 6]
    result = find_peek(values)
    assert result == 2

def test_find_peek_given_single_element_list():
    values = [1]
    result = find_peek(values)
    assert result == 0

def test_find_peek_given_empty_list():
    values = []
    result = find_peek(values)
    assert result == -1
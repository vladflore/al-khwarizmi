from binary_search import binary_search


def test_binary_search_empty_list():
    assert binary_search([], 1) == -1


def test_binary_search_item_found1():
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 7) == 6


def test_binary_search_item_found2():
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 1) == 0


def test_binary_search_item_found3():
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3


def test_binary_search_item_not_found():
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 8) == -1

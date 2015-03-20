from problem06a import number_of_items_in_list, number_of_rooms_in_house


def test_items():
    assert number_of_items_in_list(["hello", "world", "here"]) == 3


def test_house():
    house = {
        'address': '1 Infinite Loop',
        'rooms': ['bedroom 1', 'kitchen', 'bathroom 1', 'bedroom 2']
    }

    assert number_of_rooms_in_house(house) == 4

import pytest


def test_analyse_HDL():
    from blood_calculator import analyse_HDL
    input_data = 65
    expected = "Normal"
    answer = analyse_HDL(input_data)
    assert answer == expected


@pytest.mark.parametrize("a, b, expected",
                         [
                            (2, 3, 5),
                            (-5, 5, 0),
                            (1, 2, 3),
                            (3, 3, 6)

                         ])
def test_add(a, b, expected):
    from blood_calculator import add
    answer = add(a, b)
    assert answer == expected

import pytest

@pytest.mark.parametrize("point1, point2, expected_k, expected_b",
                         [
                             ((0,0), (1,1), 1, 0),
                             ((0,0), (1,2), 2, 0),
                             ((1,1), (2,1), 0, 1),
                             ((0,0), (1,2), 2, 0),

                         ]
        
)

def test_analyse_kb(point1, point2, expected_k, expected_b):
    from line_calc import analyse_kb
    answer = analyse_kb(point1, point2)
    assert answer == (expected_k, expected_b)



@pytest.mark.parametrize("k, b, x, expected",
                         [
                             (0, 1, 2, 1),
                             (1, 0, 1, 1),
                             (1, 1, 2, 3),
                         ]
        
)

def test_analyse_y(k, b, x, expected):
    from line_calc import analyse_y
    answer = analyse_y(k, b, x)
    assert answer == expected


@pytest.mark.parametrize("point1, point2, point3, expected",
                         [
                             ((0, 0), (1, 1), (2, 2), True),
                             ((0, 0), (1, 2), (2, 4), True),
                             ((0, 0), (1, 1), (2, 6), False)
                         ]
        
)

def test_if_on_line(point1, point2, point3,expected):
    from line_calc import if_on_line
    answer = if_on_line(point1, point2,point3)
    assert answer == expected
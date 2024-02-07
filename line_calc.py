def analyse_kb(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1

    return k, b

def analyse_y(k, b, x):
    y = k * x + b
    return y

def if_on_line(point1, point2, point3):
    k1, b1 = analyse_kb(point1, point2)
    k2, b2 = analyse_kb(point2, point3)
    if k1 == k2 and b1 == b2:
        return True
    else:
        return False
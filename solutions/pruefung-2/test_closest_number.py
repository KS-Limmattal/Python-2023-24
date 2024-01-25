from exam_3 import closest_number

def test():
    assert(closest_number([1,4], 2) == 1)
    assert(closest_number([1,4], 0) == 1)
    assert(closest_number([1,5], 3) == 5)
    assert(closest_number([-1,3,3,4], 1) == 3)
    assert(closest_number([-1,3,4,-1], 1) == -1)
    assert(closest_number([2,1,5,8,7,15,0.5,2.3], 6) == 7)
    assert(closest_number([2.3,4.5], 3.8) == 4.5)
    assert(closest_number([2.3,4.5], 4.9) == 4.5)
    assert(closest_number([1.2, 1.35, 2.8, 1.50, 2.33], 2.18) == 2.33)

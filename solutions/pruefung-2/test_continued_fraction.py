from exam_3 import continued_fraction
from numpy import isclose

def test():
    assert(isclose(continued_fraction([1]), 1))
    assert(isclose(continued_fraction([1,1]), 2))
    assert(isclose(continued_fraction([1,1,1]), 1.5))
    assert(isclose(continued_fraction([1,1,1,1]), 5/3))
    assert(isclose(continued_fraction([1,1,1,1,1]), 1.6))
    assert(isclose(continued_fraction([1,1,1,1,1,1]), 1.625))
    assert(isclose(continued_fraction([1,2]), 1.5))
    assert(isclose(continued_fraction([1,2,2]), 1.4))
    assert(isclose(continued_fraction([1,2,2,2]), 17/12))
    assert(isclose(continued_fraction([1,2,2,2,2]), 41/29))
    assert(isclose(continued_fraction([1,2,2,2,2,2]), 99/70))
    assert(isclose(continued_fraction([3,1,4,1,5,9]), 1229/321))
    assert(isclose(continued_fraction([2,7,1,8,2,8]), 2703/1271))

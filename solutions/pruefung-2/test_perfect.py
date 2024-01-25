from exam_2 import is_perfect

def test():
    assert(is_perfect(6))
    assert(is_perfect(28))
    assert(is_perfect(496))
    assert(is_perfect(8128))
    for i in range(1, 6):
        assert(not is_perfect(i))
    for i in range(7, 28):
        assert(not is_perfect(i))    
    for i in range(29, 496):
        assert(not is_perfect(i))    

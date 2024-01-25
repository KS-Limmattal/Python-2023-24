from exam_2 import value_count

def test():
    assert(value_count({"key1": [5,7]}) == {5:1, 7:1})
    assert(value_count({"key1": [5,7], "key2": [5]}) == {5:2, 7:1})
    assert(value_count({"key1": [5], "key2": [5], "key3": [5]}) == {5:3})
    assert(value_count({"a": [1,2,3,4], "b": [4,5,6,7]}) == {1:1, 2:1, 3:1, 4:2, 5:1, 6:1, 7:1})
    assert(value_count({"a":[1,3,5], "b":[2,5], "c":[1,2,1,5]}) == {1: 3, 2: 2, 3: 1, 5: 3})

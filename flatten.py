"""
Flatten
=======

Write a method that returns a flattened list or tuple given a list that may
include nested lists or tuples.
"""

def flatten(data):
    pass

if __name__ == '__main__':
    assert(flatten([1, 2, 3]) == [1, 2, 3])
    assert(flatten([1, 2, 3, ('a', 'b')]) == [1, 2, 3, 'a', 'b'])
    assert(flatten([1, 2, 3, ('a', 'b', ('c', 'd'))]) == [1, 2, 3, 'a', 'b', 'c', 'd'])

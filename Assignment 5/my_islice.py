# Jeremy Ulfohn // jau392 // 5 July 2021

def my_islice_generator(iterable, start = 0, stop = None, step = 1):
    lengthOfIter = len(iterable)

    if (lengthOfIter < stop) or (lengthOfIter < start):
        return
    itera = iter(range(start,stop,step))
    total = start
    enum = next(itera)

    while total <= stop:
        yield iterable[total]
        for i in range(step):
            try:
                enum = next(itera)
            except StopIteration:
                return
        total += step


def test_my_isslice():
    print("isslice generator")

    assert list(my_islice_generator('', 2, 5)) == []
    assert list(my_islice_generator('ABCDEFG', 2, 5)) == ['C', 'D', 'E']
    assert list(my_islice_generator('ABCDEFG', 2, 7)) == ['C', 'D', 'E', 'F', 'G']

    print("isslice iterator")

    p = my_islice_generator('', 2, 5)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p

    assert list(p) == []

    p = my_islice_generator('ABCDEFG', 2, 5)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p
    assert list(p) == ['C', 'D', 'E']

    p = my_islice_generator('ABCDEFG', 2, 7)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p
    assert list(p) == ['C', 'D', 'E', 'F', 'G']

test_my_isslice()
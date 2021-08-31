# define my_zip() to emulate zip()
# all iterables have same length
# all iterables can NOT be indexed
# make only one pass through variables


# INPUT: *parameter === *iterables, which are either lists or tuples
# OUTPUT: list
def my_zip(*iterables):
    # initialize
    iterators = [iter(i) for i in iterables] # make *iterables into list of iterators

    while iterators: # loop terminates upon StopIteration bc of next() calls
        zipped = [] # tuple(zipped) will be our result/yield

        for iterator in iterators: # go across each itr in *iterables, getting next() from each
            next_value = next(iterator, "end")
            if next_value == "end":
                return # return so that loop ends
            zipped.append(next_value) # append next_value iff it exists

        yield tuple(zipped) # e.g. result[0] will be (2, 4, 6) when list() is applied


# tests for my_zip
def test_zip():
   print("my_zip()")
   assert list(my_zip()) == []
   assert list(my_zip([])) == []
   assert list(my_zip((), ())) == []
   assert list(my_zip([2, 3])) == [(2,), (3,)]
   assert list(my_zip((2, 3), (4, 5), (6, 7))) == [(2, 4, 6), (3, 5, 7)]
   assert list(my_zip([2, 3, 4], [5, 6, 7])) == [(2, 5), (3, 6), (4, 7)]

# run tests
test_zip()
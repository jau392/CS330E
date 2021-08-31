import time # to use time.sleep() method below


def my_timer(func): # wrapper function takes argument "func" w optional parameters
    def parameter_handler(*args, **kwargs): # populated by func parameters with '@"
        beginning = time.time()
        func(*args, **kwargs) # run func here
        end = time.time()
        net = float(end - beginning)
        # all functions have __name__ attribute, which is get_name(function)
        print("Inside decorator:", func.__name__, "ran in:",  net, "sec")

    return parameter_handler # no () because of default unpacking


@my_timer # <==> my_timer(func1())
def func1():
    time.sleep(1) # delay of 1 second
    print('func1 is executing!')


@my_timer
def func2():
    time.sleep(2) # delay of 2 seconds
    print('func2 is executing!')


def test_timer () :
    print("Output: my_timer()") # fixed spelling
    func1()
    func2()


test_timer()
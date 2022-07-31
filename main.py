# exercise

#generator performance
from time import time


def performance(func):
    def wrap_func(*args,**kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        print(t2-t1)
        return result
    return wrap_func

@performance
def long_time():
    print('1')
    for i in range(100):
        i*5
    
@performance
def long_time2():
    print('2')
    for i in list(range(100)):
        i*5

long_time()
long_time2()
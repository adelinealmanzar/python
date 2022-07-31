# exercise

#generators under the hood
def for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break

for_loop([1,2,3])
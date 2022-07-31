# exercise

#range generator

class RangeGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if RangeGen.current < self.last:
            num = RangeGen.current
            RangeGen.current += 1
            return num
        raise StopIteration

range_gen = RangeGen(0,100)
for i in range_gen:
    print(i)

import math
# exercise

# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
steps_list = input('What are the up, down, left, and right steps taken?').split(';')

def euclidean_dist(x,y):
   # original position assumed to always start at 0 
    dist = math.sqrt(y**2 + x**2)
    return round(dist)

def abs_dist():
    steps_dict = dict(x.split(" ") for x in steps_list)
    x = abs(int(steps_dict['LEFT']) - int(steps_dict['RIGHT']))
    y = abs(int(steps_dict['UP']) - int(steps_dict['DOWN']))
    return euclidean_dist(x,y)


print(abs_dist())


# Alex Shelton, Physics Motion Functions used in organism and predator classes
#
#
#


def magnitude_calc(vector): 
    x = 0
    for i in vector:
        x += i**2
    magnitude = x**0.5
    return magnitude

def normalise(vector):
    magnitude = magnitude_calc(vector)
    if magnitude != 0:
        vector = vector / magnitude
    return vector

# Alex Shelton, Physics Motion Functions used in organism and predator classes
#
#
#


def magnitude_calc(vector): 
    #Traingular vector 
    x = 0
    for i in vector:
        x += i**2
    magnitude = x**0.5
    return magnitude

def normalise(vector):
    #Takes our vector of size n>1 || n<1 and represents it in unit of 1 terms
    # Function takes old vector and divides it by the magnitude
    magnitude = magnitude_calc(vector)
    #dividing vector by magnutitude to normalise vector
    if magnitude != 0:
        vector = vector / magnitude
    return vector

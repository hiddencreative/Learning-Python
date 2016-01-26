
# import math module to provide access to mathematical functions
import math

#define a function to sum the area and square of the perimeter of a regular polygon with 2 arguments
def polysum(n,s):
    #the area of a regular polygon is: (0.25*n*s^2)/tan(pi/n)
    area = (.25*n*s**2) / (math.tan(math.pi/n))
    #the perimeter of a polygon is the length of the boundary of the polygon
    perimeter = n*s
    #sum the area and square of the perimeter
    x = area + perimeter**2
    #return the sum, rounded to 4 decimal places
    return round(x, 4)

print polysum(97, 29)
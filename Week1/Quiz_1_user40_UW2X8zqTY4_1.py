# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.
# Quiz 1

#Q2
print "Q2"
p = True
q = True
print p,q,not ( p or not q)

q = False
print p,q,not ( p or not q)

p = False
print p,q,not ( p or not q)

q = True
print p,q,not ( p or not q)


#Q3
print "Q3"
def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"
    
print do_stuff()

#Q4
print "Q4"
n=123
print (n // 10) % 10
print ((n - n % 10) % 100) / 10
print (n % 10) / 10
n=98765
print (n // 10) % 10
print ((n - n % 10) % 100) / 10
print (n % 10) / 10

#Q6
print "Q6"
def f(x):
    return -5*x**5 + 69*x**2 -47

print f(0)
print f(1)
print f(2)
print f(3)

#Q7
print "Q7"
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value * (1.0 + rate_per_period) ** periods

print future_value(500, .04, 10, 10)
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

#Q8
print "Q8"
import math
def polygon_area(n,s):
    return 0.25 * n * s**2 / math.tan(math.pi/n)

print polygon_area(5,7)
print polygon_area(7,3)

#Q9
print "Q9"
def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

print max_of_3(4,3,7)


#Q10
print "Q10"
#define project_to_distance(point_x point_y distance):
#    dist_to_origin = math.square_root(pointx ** 2 + pointy ** 2)    
#     scale == distance / dist_to_origin
#    print point_x * scale, point_y * scale
#    
#project-to-distance(2, 7, 4)
#
import math
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)
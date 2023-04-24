"""
There is no closed formula for the circumference of an ellipse. Write a Python script that approximates the circumference. 
The ellipse is to be approximated by an increasing number of straight
lines.
An ellipse is given by the parametric curve
𝑓 ∶ [0; 2𝜋] → ℝ2, 𝑡 ↦ (𝑎 cos𝑡, 𝑏 sin 𝑡)
where 𝑎 and 𝑏 are the half axes
Start with a function that determines the distance between two points (x1, y1) and (x2, y2):
length(x1, y1, x2, y2)
• Add a function that computes points on the boundary of an ellipse. One way of returning two
coordinates is returning a tuple.
ellipse(a, b, t)
• Determine the circumference for an ellipse that is approximated by n straight line edges—split
the interval [0; 2𝜋] into n parts of equal size.
circumference(a, b, n)
• In the main program, read in the half axes 𝑎 and 𝑏 and the desired relative accuracy 𝜀. Compute
and print the circumference for 𝑛 = 2, 4, 8, 16, … until the relative accuracy is reached.
"""


import math

def length(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

def ellipse(a, b, t):
    return (a * math.cos(t), b * math.sin(t))

def circumference(a, b, n):
    theta = 2 * math.pi /n
    x1 = a
    y1 = 0
    t = theta
    z=0
    for i in range(n):
        x2,y2 = ellipse(a, b, t)
        t = t + theta
        z = z + length(x1, y1, x2, y2)
        x1 = x2
        y1 = y2
    return z

def main():
    print('Enter a, b')
    a = float(input('a = '))
    b = float(input('b = '))
    epsilon = 1e-10
    n = 2
    c = circumference(a, b, n)
    RA = 1
    iteration = 0
    while (RA>epsilon):
        n = n * 2
        cnew = circumference(a, b, n)
        RA = abs((cnew - c) / cnew)
        c = cnew
        iteration += 1
        if n == 2**24:
            break
    print('Circumference of Ellipse:', c)
    print('Number of iteration',iteration)
main()


"""
Krutarth Trivedi
2130962
"""
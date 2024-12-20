#this program computes estimates of pi by simulating dart throws onto a square
''' 
Pi Estimation Using Monte Carlo Simulation :
This program estimates the value of 𝜋 using a Monte Carlo method. 
It simulates throwing random "darts" (points) onto a square and calculates 
the ratio of points that land inside a unit circle to the total number of points. 
This ratio is used to approximate π.
'''


from random import random

TRIES = 10000
hits = 0

for i in range(TRIES) :
    #generate two negative numbers between -1 and 1
    r = random()
    x = -1 + 2 * r
    r = random()
    y = -1 + 2 * r

    #check whether the point lies in the unit circle (radius = 1)
    if x*x + y*y <= 1 :
        hits += 1
    '''the ratio hits/tries is approximately the same as the ratio
    circle area / square area = pi / 4 '''

piEstimate = 4.0 * hits/TRIES
print("Estimate for pi:",piEstimate)
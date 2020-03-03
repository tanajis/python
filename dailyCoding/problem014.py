# Monte Carlo estimation
# Monte Carlo methods are a broad class of computational algorithms that rely on
# repeated random sampling to obtain numerical results. One of the basic examples of 
# getting started with the Monte Carlo algorithm is
# the estimation of Pi.

#Ref :geeksforgeeks.org/estimating-value-pi-using-monte-carlo/


#Explaination :
#cosnider square of 1 unit edge lenth
#ARe of Sqaure = a**2  =1*1 =1
#Cicrlce will fir in that sqaure so radius will be 0.5
#Are of circle = pi * r**2  =pi *0.25

#A(circle) /A(square) = [ pi * r**2  ] / a**2
#                      = pi  *   r**2 / 4 *  r**2
#                      =pi /4   ----------------------------eq(1)

#Also
#A(circle) /A(square) =among total points n how many falls inside circle/total points ---es(2)

#Now matchright sides of both equations eq(1) and eq(2)
# pi/4  = among total points n how many falls inside circle/total points 
# pi =      4 * (among total points n how many falls inside circle/total points )



                        





# The Algorithm(Not mine, Copied from Geeksforgeeks)
# 1. Initialize circle_points, square_points and interval to 0.
# 2. Generate random point x.
# 3. Generate random point y.
# 4. Calculate d = x*x + y*y.
# 5. If d <= 1, increment circle_points.
# 6. Increment square_points.
# 7. Increment interval.
# 8. If increment < NO_OF_ITERATIONS, repeat from 2.
# 9. Calculate pi = 4*(circle_points/square_points).
# 10. Terminate.

from random import random,randrange
radius = 2


def estimate_pi(num_random_tests):
    pi_counter = 0
    rsquared = radius ** 2
    #number of square points will be equal to num_random_tests
    for _ in range(num_random_tests):

        #Generate random x and y. Multiplying by radius so as to keep it greter thar radium 
        #    keeping in multiple of radius value


        #random() generates points between o and 1 ex. 0.88765 etc

        x_rand = random() * radius
        y_rand = random() * radius

        print(x_rand,y_rand)

        #if point falls inside circle ,increments its cnt
        if (x_rand ** 2) + (y_rand ** 2) < rsquared:
            pi_counter += 1


    return 4 * pi_counter / num_random_tests


#assert round(estimate_pi(10), 3) == 3.141
print(round(estimate_pi(100),3))

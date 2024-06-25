# 3.	The height of a projectile (y) from a gun (ignoring air resistance) is given as:
#
#                                     gx2
# y = y0 + x tan θ -
#                              2(v0 cos θ)2
#
# where:
# g      	: Acceleration due to gravity:  9.81 m/s squared
# v0    	: the initial velocity m/s
# θ	: (theta) elevation angle in radians
# x	: the horizontal distance travelled
# y0  	: height of the barrel (m)
#
# Write a Python program to answer the following question:
# At a barrel height of 1m, after a horizontal distance of 0.5m, an elevation of 80 degrees, and an initial velocity of 44 m/s, what is the height of the projectile?
# To convert degrees (deg) to radians use:
# theta = deg * (pi/180)
# You will need to import some math methods:
# from math import pi, tan, cos


from math import pi, tan, cos
g = 9.81
v0 = 44
theta = 80 * (pi/180)
x = 0.5
y0 = 1

y = y0 + x*tan(theta) - (g*x**2)/(2 * ((v0*cos(theta))**2))
print("Height:", y, "m")

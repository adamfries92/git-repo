#!/usr/bin/python3
import os
import sys
from timeit import default_timer as timer
from random import seed, random
import math

# Clear screen
os.system("clear")

multTime = 0
shiftTime = 0
floatTime = 0
its = 100000

for t in range(0,its):
	# Time Int multiplication
	x = 50098456
	startMult = timer()
	x = x * 1024
	endMult = timer()
	multTime = multTime + endMult - startMult
	
	# Time Int shift
	y = 50098456
	startShift = timer()
	y = y << 10
	endShift = timer()
	shiftTime = shiftTime + endShift - startShift
	
	z = 50098455.974198712418617126
	startFloat = timer()
	z = z * 1025.1135898715984
	endFloat = timer()
	floatTime = floatTime + endFloat - startFloat
	# Display results
	#print("t: ",t)
	#print("x: ",x," Time elapsed: ",multTime)
	#print("y: ",y," Time elapsed: ",shiftTime)

	

# Average
multTime = multTime/its
shiftTime = shiftTime/its
floatTime = floatTime/its

print("Iterations: ",its)
print("Average Difference (Shift - Mult): ",shiftTime-multTime)
print("Average Difference (Float - Mult): ",floatTime-multTime)
print("Average Difference (Float - Shift): ",floatTime-shiftTime)
print("x: ",x,"y: ",y,"z: ",z)

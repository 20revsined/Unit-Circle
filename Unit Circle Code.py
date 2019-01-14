import math

Input = str(input("Welcome to the Unit Circle calculator! Please state whether you will be entering a degree measurement or a radian measurement on the Unit Circle."))

if Input == "degrees":
	degrees = float(input("Please enter your degree measurement."))

	while degrees < 0:
		degrees += 360

	if(degrees % 30 == 0) and (degrees % 60 != 0) and (degrees > 0 and degrees < 90):
		print("The coordinates of this measurementment are (" + str(math.sqrt(3) / 2) + "," + str(0.5) + ")")
	elif (degrees % 30 == 0) and (degrees % 60 != 0) and (degrees > 90 and degrees < 180):
		print("The coordinates of this measurement are (" + str(-math.sqrt(3) / 2) + "," + str(0.5) + ")")
	elif (degrees % 30 == 0) and (degrees % 60 != 0) and (degrees > 180 and degrees < 270):
		print("The coordinates of this measurement are (" + str(-math.sqrt(3) / 2) + "," + str(-0.5) + ")")
	elif (degrees % 30 == 0) and (degrees % 60 != 0) and (degrees > 270 and degrees < 360):
		print("The coordinates of this measurement are (" + str(math.sqrt(3) / 2) + "," + str(-0.5) + ")")

	if (degrees % 60 == 0) and (degrees % 2 == 0) and (degrees > 0 and degrees < 90):
		print("The coordinates of this measurementment are (" + str(0.5) + "," + str(math.sqrt(3) / 2) + ")")
	elif (degrees % 60 == 0) and (degrees % 2 == 0) and (degrees > 90 and degrees < 180):
		print("The coordinates of this measurement are (" + str(-0.5) + "," + str(math.sqrt(3) / 2) + ")")
	elif (degrees % 60 == 0) and (degrees % 2 == 0) and (degrees > 180 and degrees < 270):
		print("The coordinates of this measurement are (" + str(-0.5) + "," + str(-math.sqrt(3) / 2) + ")")
	elif (degrees % 60 == 0) and (degrees % 2 == 0) and (degrees > 270 and degrees < 360):
		print("The coordinates of this measurement are (" + str(0.5) + "," + str(-math.sqrt(3) / 2) + ")")

	if (degrees % 45 == 0) and (degrees > 0 and degrees < 90):
		print("The coordinates of this measurementment are (" + str(math.sqrt(2) / 2) + "," + str(math.sqrt(2) / 2) + ")")
	elif (degrees % 45 == 0) and (degrees > 90 and degrees < 180):
		print("The coordinates of this measurement are (" + str(-math.sqrt(2) / 2) + "," + str(math.sqrt(2) / 2) + ")")
	elif (degrees % 45 == 0) and (degrees > 180 and degrees < 270):
		print("The coordinates of this measurement are (" + str(-math.sqrt(2) / 2) + "," + str(-math.sqrt(2) / 2) + ")")
	elif (degrees % 45 == 0) and (degrees > 270 and degrees < 360):
		print("The coordinates of this measurement are (" + str(math.sqrt(2) / 2) + "," + str(-math.sqrt(2) / 2) + ")")

	if(degrees == 0 or degrees == 360):
		print("The coordinates of this measurement are (1, 0)")
	elif degrees == 90:
		print("The coordinates of this measurement are (0, 1)")
	elif degrees == 180:
		print("The coordinates of this measurement are (-1, 0)")
	elif degrees == 270:
		print("The coordinates of this measurement are (0, -1)")
	else:
		print("You have entered an invalid degree value. Please try again.")

elif Input == "radians":
	radians = float(input("Please enter your radian measurement."))

	while radians < 0:
		radians += 6.28

	if(radians % 0.523 == 0) and (radians % 1.046 != 0) and (radians > 0 and radians < (math.pi / 2)):
		print("The coordinates of this measurementment are (" + str(math.sqrt(3) / 2) + "," + str(0.5) + ")")
	elif (radians % 0.523 == 0) and (radians % 1.046 != 0) and (radians > (math.pi / 2) and radians < (math.pi)):
		print("The coordinates of this measurement are (" + str(-math.sqrt(3) / 2) + "," + str(0.5) + ")")
	elif (radians % 0.523 == 0) and (radians % 1.046 != 0) and (radians > (math.pi) and radians < (math.pi * 1.5)):
		print("The coordinates of this measurement are (" + str(-math.sqrt(3) / 2) + "," + str(-0.5) + ")")
	elif (radians % 0.523 == 0) and (radians % 1.046 != 0) and (radians > (math.pi * 1.5) and radians < (math.pi * 2)):
		print("The coordinates of this measurement are (" + str(math.sqrt(3) / 2) + "," + str(-0.5) + ")")

	if (radians % 1.046 == 0) and (radians % 2 == 0) and (radians > 0 and radians < (math.pi / 2)):
		print("The coordinates of this measurementment are (" + str(0.5) + "," + str(math.sqrt(3) / 2) + ")")
	elif (radians % 1.046 == 0) and (radians % 2 == 0) and (radians > (math.pi / 2) and radians < (math.pi)):
		print("The coordinates of this measurement are (" + str(-0.5) + "," + str(math.sqrt(3) / 2) + ")")
	elif (radians % 1.046 == 0) and (radians % 2 == 0) and (radians > (math.pi) and radians < (math.pi * 1.5)):
		print("The coordinates of this measurement are (" + str(-0.5) + "," + str(-math.sqrt(3) / 2) + ")")
	elif (radians % 1.046 == 0) and (radians % 2 == 0) and (radians > (math.pi * 1.5) and radians < (math.pi * 2)):
		print("The coordinates of this measurement are (" + str(0.5) + "," + str(-math.sqrt(3) / 2) + ")")

	if (radians % 0.785 == 0) and (radians > 0 and radians < (math.pi / 2)):
		print("The coordinates of this measurementment are (" + str(math.sqrt(2) / 2) + "," + str(math.sqrt(2) / 2) + ")")
	elif (radians % 0.785 == 0) and (radians > (math.pi / 2) and radians < (math.pi)):
		print("The coordinates of this measurement are (" + str(-math.sqrt(2) / 2) + "," + str(math.sqrt(2) / 2) + ")")
	elif (radians % 0.785 == 0) and (radians > (math.pi) and radians < (math.pi * 1.5)):
		print("The coordinates of this measurement are (" + str(-math.sqrt(2) / 2) + "," + str(-math.sqrt(2) / 2) + ")")
	elif (radians % 0.785 == 0) and (radians > (math.pi * 1.5) and radians < (math.pi * 2)):
		print("The coordinates of this measurement are (" + str(math.sqrt(2) / 2) + "," + str(-math.sqrt(2) / 2) + ")")

	if(radians == 0 or radians == 6.28):
		print("The coordinates of this measurement are (1, 0)")
	elif radians == 1.57:
		print("The coordinates of this measurement are (0, 1)")
	elif radians == 3.14:
		print("The coordinates of this measurement are (-1, 0)")
	elif radians == 4.71:
		print("The coordinates of this measurement are (0, -1)")

XCoordinate = float(input("Please enter the x coordinate to determine what angle measure the x and y coordinates are located."))
YCoordinate = float(input("Please enter the y coordinate to determine what angle measure the x and y coordinates are located."))

if XCoordinate == 1 and YCoordinate == 0:
	print("The angle measures are 0 or 360 degrees and 0 or 2π radians")
elif XCoordinate == 0 and YCoordinate == 1:
	print("The angle measure is 90 degrees or π/2 radians")
elif XCoordinate == 0 and YCoordinate == -1:
	print("The angle measure is 270 degrees are 3π/2 radians")
elif XCoordinate == -1 and YCoordinate == 0:
	print("The angle measure is 180 degrees or π radians")

if XCoordinate == 0.5 and YCoordinate == 0.866:
	print("The angle measure is 60 degrees or π/3 radians")
elif XCoordinate == -0.5 and YCoordinate == 0.866:
	print("The angle measure is 120 degrees or 2π/3 radians")
elif XCoordinate == -0.5 and YCoordinate == -0.866:
	print("The angle measure is 240 degrees or 4π/3 radians")
elif XCoordinate == 0.5 and YCoordinate == -0.886:
	print("The angle measure is 300 degrees or 5π/3 radians")

if XCoordinate == 0.866 and YCoordinate == 0.5:
	print("The angle measure is 30 degrees or π/6 radians")
elif XCoordinate == -0.866 and YCoordinate == 0.5:
	print("The angle measure is 150 degrees or 5π/6 radians")
elif XCoordinate == -0.866 and YCoordinate == -0.5:
	print("The angle measure is 210 degrees or 7π/6 radians")
elif XCoordinate == 0.866 and YCoordinate == -0.5:
	print("The angle measure is 330 degrees or 11π/6")

if XCoordinate == 0.707 and YCoordinate == 0.707:
	print("The angle measure is 45 degrees or π/4 radians")
elif XCoordinate == -0.707 and YCoordinate == 0.707:
	print("The angle measure is 135 degrees or 3π/4 radians")
elif XCoordinate == -0.707 and YCoordinate == -0.707:
	print("The angle measure is 225 degrees or 5π/4 radians")
elif XCoordinate == 0.707 and YCoordinate == -0.707:
	print("The angle measure is 315 degrees or 7π/4 radians")

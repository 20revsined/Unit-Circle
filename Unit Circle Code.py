import math

Input = str(input("Welcome to the Unit Circle calculator! Please state whether you will be entering a degree measurement or a radian measurement on the Unit Circle."))

if Input == "degrees":
	degrees = float(input("Please enter your degree measurement."))

	if(degrees < 0):
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

elif Input == "radians":
	radians = float(input("Please enter your radian measurement."))

	if(radians < 0):
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

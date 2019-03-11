import math

Input = str(input("Welcome to the Unit Circle calculator! Please state whether you will be entering a degree measurement or a radian measurement on the Unit Circle."))

if Input == "degrees":
	degrees = float(input("Please enter your degree measurement."))

	while degrees < 0 and degrees <= 360:
		degrees += 360

	while degrees > 360 and degrees >= 0:
		degrees -= 360

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
	radians = str(input("Please enter your radian measurement."))

	if(radians == "pi"):
		radians = math.pi
		ModifyRadian = float(input("Please enter a value that will modify your input."))
		ModifyRadian *= math.pi

	while ModifyRadian < 0 and ModifyRadian <= (2 * math.pi):
		ModifyRadian += (2 * math.pi)

	while ModifyRadian > (2 * math.pi) and ModifyRadian <= 0:
		ModifyRadian -= (2 * math.pi)

	if(ModifyRadian % (math.pi / 6) == 0) and (ModifyRadian % (math.pi/3) != 0) and (ModifyRadian > 0 and ModifyRadian < (math.pi / 2)):
		print("The coordinates of this measurementment are (" + str(math.sqrt(3) / 2) + "," + str(0.5) + ")")
	elif (ModifyRadian % (math.pi / 6) == 0) and (ModifyRadian % (math.pi/3) != 0) and (ModifyRadian > (math.pi / 2) and ModifyRadian < (math.pi)):
		print("The coordinates of this measurement are (" + str(-math.sqrt(3) / 2) + "," + str(0.5) + ")")
	elif (ModifyRadian % (math.pi / 6) == 0) and (ModifyRadian % (math.pi/3) != 0) and (ModifyRadian > (math.pi) and ModifyRadian < (math.pi * 1.5)):
		print("The coordinates of this measurement are (" + str(-math.sqrt(3) / 2) + "," + str(-0.5) + ")")
	elif (ModifyRadian % (math.pi / 6) == 0) and (ModifyRadian % (math.pi/3) != 0) and (ModifyRadian > (math.pi * 1.5) and ModifyRadian < (math.pi * 2)):
		print("The coordinates of this measurement are (" + str(math.sqrt(3) / 2) + "," + str(-0.5) + ")")

	if (ModifyRadian % (math.pi / 3) == 0) and (ModifyRadian % 2 == 0) and (ModifyRadian > 0 and ModifyRadian < (math.pi / 2)):
		print("The coordinates of this measurementment are (" + str(0.5) + "," + str(math.sqrt(3) / 2) + ")")
	elif (ModifyRadian % (math.pi / 3) == 0) and (ModifyRadian % 2 == 0) and (ModifyRadian > (math.pi / 2) and ModifyRadian < (math.pi)):
		print("The coordinates of this measurement are (" + str(-0.5) + "," + str(math.sqrt(3) / 2) + ")")
	elif (ModifyRadian % (math.pi / 3) == 0) and (ModifyRadian % 2 == 0) and (ModifyRadian > (math.pi) and ModifyRadian < (math.pi * 1.5)):
		print("The coordinates of this measurement are (" + str(-0.5) + "," + str(-math.sqrt(3) / 2) + ")")
	elif (ModifyRadian % (math.pi / 3) == 0) and (ModifyRadian % 2 == 0) and (ModifyRadian > (math.pi * 1.5) and ModifyRadian < (math.pi * 2)):
		print("The coordinates of this measurement are (" + str(0.5) + "," + str(-math.sqrt(3) / 2) + ")")

	if (ModifyRadian % (math.pi / 4) == 0) and (ModifyRadian > 0 and ModifyRadian < (math.pi / 2)):
		print("The coordinates of this measurementment are (" + str(math.sqrt(2) / 2) + "," + str(math.sqrt(2) / 2) + ")")
	elif (ModifyRadian % (math.pi / 4) == 0) and (ModifyRadian > (math.pi / 2) and ModifyRadian < (math.pi)):
		print("The coordinates of this measurement are (" + str(-math.sqrt(2) / 2) + "," + str(math.sqrt(2) / 2) + ")")
	elif (ModifyRadian % (math.pi / 4) == 0) and (ModifyRadian > (math.pi) and ModifyRadian < (math.pi * 1.5)):
		print("The coordinates of this measurement are (" + str(-math.sqrt(2) / 2) + "," + str(-math.sqrt(2) / 2) + ")")
	elif (ModifyRadian % (math.pi / 4) == 0) and (ModifyRadian > (math.pi * 1.5) and ModifyRadian < (math.pi * 2)):
		print("The coordinates of this measurement are (" + str(math.sqrt(2) / 2) + "," + str(-math.sqrt(2) / 2) + ")")

	if(ModifyRadian == 0 or ModifyRadian == math.pi * 2):
		print("The coordinates of this measurement are (1, 0)")
	elif ModifyRadian == math.pi / 2:
		print("The coordinates of this measurement are (0, 1)")
	elif ModifyRadian == math.pi:
		print("The coordinates of this measurement are (-1, 0)")
	elif ModifyRadian == math.pi * 1.5:
		print("The coordinates of this measurement are (0, -1)")

XCoordinate = str(input("Please enter the x coordinate to determine what angle measure the x and y coordinates are located."))
YCoordinate = str(input("Please enter the y coordinate to determine what angle measure the x and y coordinates are located."))

if XCoordinate == "sqrt3":
	XCoordinate = math.sqrt(3)
	ModifyX = float(input("Please enter a value in which sqrt3 will be multiplied."))
	XCoordinate *= ModifyX
if XCoordinate == "sqrt2":
	XCoordinate = math.sqrt(2)
	ModifyX = float(input("Please enter a value in which sqrt2 will be multiplied."))
	XCoordinate *= ModifyX
if YCoordinate == "sqrt3":
	YCoordinate = math.sqrt(3)
	ModifyY = float(input("Please enter a value in which sqrt3 will be multiplied."))
	YCoordinate *= ModifyY
if YCoordinate == "sqrt2":
	YCoordinate = math.sqrt(2)
	ModifyY = float(input("Please enter a value in which sqrt2 will be multiplied."))
	YCoordinate *= ModifyY

print("XCoordinate: " + str(XCoordinate))
print("YCoordinate: " + str(YCoordinate))

X = XCoordinate
Y = YCoordinate

if X == 1 and Y == 0:
	print("The angle measures are 0 or 360 degrees and 0 or 2π radians")
elif X == 0 and Y == 1:
	print("The angle measure is 90 degrees or π/2 radians")
elif X == 0 and Y == -1:
	print("The angle measure is 270 degrees are 3π/2 radians")
elif X == -1 and Y == 0:
	print("The angle measure is 180 degrees or π radians")

if X == 0.5 and Y == (math.sqrt(3) * 0.5):
	print("The angle measure is 60 degrees or π/3 radians")
elif X == -0.5 and Y == math.sqrt(3) * 0.5:
	print("The angle measure is 120 degrees or 2π/3 radians")
elif X == -0.5 and Y == (-math.sqrt(3) * 0.5):
	print("The angle measure is 240 degrees or 4π/3 radians")
elif X == 0.5 and Y == (-math.sqrt(3) * 0.5):
	print("The angle measure is 300 degrees or 5π/3 radians")

if X == (math.sqrt(3) * 0.5) and Y == 0.5:
	print("The angle measure is 30 degrees or π/6 radians")
elif X == (-math.sqrt(3) * 0.5) and Y == 0.5:
	print("The angle measure is 150 degrees or 5π/6 radians")
elif X == (-math.sqrt(3) * 0.5) and Y == -0.5:
	print("The angle measure is 210 degrees or 7π/6 radians")
elif X == (math.sqrt(3) * 0.5) and Y == -0.5:
	print("The angle measure is 330 degrees or 11π/6 radians")

if X == math.sqrt(2) * 0.5 and Y == math.sqrt(2) * 0.5:
	print("The angle measure is 45 degrees or π/4 radians")
elif X == -math.sqrt(2) * 0.5 and Y == math.sqrt(2) * 0.5:
	print("The angle measure is 135 degrees or 3π/4 radians")
elif X == -math.sqrt(2) * 0.5 and Y == -math.sqrt(2) * 0.5:
	print("The angle measure is 225 degrees or 5π/4 radians")
elif X == math.sqrt(2) * 0.5 and Y == -math.sqrt(2) * 0.5:
	print("The angle measure is 315 degrees or 7π/4 radians")

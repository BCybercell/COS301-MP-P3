import time as time
import random as Rand
import json as json

# TODO Kyle
def AuthenticateImage(aImg):
	# print(aImg);
	lChance = Rand.randint(1, 100) # TODO need to make this the actual facial recognition function library
	
	lUser = Rand.randint(1, 10) #userID just 10 users for now as example
	if lChance < 50: 	#TODO change to 85 after demo as must be 85% match
		lUser = -1		#userID of -1 means it failed for this demo purpose
	
	return lUser, lChance
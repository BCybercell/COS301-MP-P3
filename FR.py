import time as time
import random as Rand
import json as json

#  TODO Richard
def AuthenticateUser(aArrImg):
    
    start = time.time()
    lUserIDs = []
    lPercentages = []
    for img in aArrImg:
        userID, percent = AuthenticateImage(img) #This function is implemented elsewhere

    return lUserIDs[ind]  # TODO fix
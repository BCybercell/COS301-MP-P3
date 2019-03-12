import time as time
import random as Rand
import json as json

#  TODO Richard
def AuthenticateUser(aArrImg):
    Update() #Call Update function to get new/updated list of the database from CIS
    start = time.time()
    lUserIDs = []
    lPercentages = []
    for img in aArrImg:
        userID, percent = AuthenticateImage(img) #This function is implemented elsewhere

    ind = -1
    Log(lUserIDs[ind],start, end, status)
    return lUserIDs[ind]  # TODO fix
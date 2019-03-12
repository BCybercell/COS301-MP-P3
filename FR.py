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
        lUserIDs.append(userID)
        lPercentages.append(percent)
    lCount = []

    for id in lUserIDs.copy():
        print(id)
        lCount.append(0)
        for id2 in lUserIDs.copy():
            if id == id2:
                index = lUserIDs.index(id)
                lCount[index] += 1

  

    end = time.time()
    if lUserIDs[ind] == -1:
        status = False
    else:
        status = True
    Log(lUserIDs[ind],start, end, status) # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)
    # TODO call log
    print('======')
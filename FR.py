import time as time
import random as Rand
import json as json
import statistics as stat

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

    #Get the user ID that appears the most in the array
    lUserIDToSend = stat.median(lUserIDs)  
    
    #Determine the status of the id. -1 indicates the user could not be found
    if lUserIDToSend == -1:
        status = False
    else:
        status = True

    end = time.time()
    Log(lUserIDToSend,start, end, status) # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)
    
    #testing purposes
    #print("=============User Id :"+ lUserIDs[ind]+"=============")
    return lUserIDToSend
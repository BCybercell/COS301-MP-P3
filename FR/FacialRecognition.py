import time as time
import random as Rand
import json as json
#import statistics as stat
import datetime as dt
from dateutil.parser import parse as parse_date
from dateutil import parser



def AuthenticateUser(aArrImg):
    Update()  # Call Update function to get new/updated list of the database from CIS
    start = time.time()
    lUserIDs = []
    lPercentages = []
    if not aArrImg:
        return -1
    for img in aArrImg:
        userID, percent = AuthenticateImage(img)  # This function is implemented elsewhere
        lUserIDs.append(userID)
        lPercentages.append(percent)

    # Get the user ID that appears the most in the array
    lUserIDToSend = stat.median(lUserIDs)

    # Determine the status of the id. -1 indicates the user could not be found
    if lUserIDToSend == -1:
        status = False
    else:
        status = True

    end = time.time()
    Log(lUserIDToSend, start, end,
        status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)

    # testing purposes
    # print("=============User Id :"+ lUserIDs[ind]+"=============")
    return lUserIDToSend


def AuthenticateImage(aImg):
    # print(aImg);
    if not aImg:
        return -1, 0
    lChance = Rand.randint(1, 100)  # TODO need to make this the actual facial recognition function library

    lUser = Rand.randint(1, 10)  # userID just 10 users for now as example
    if lChance < 50:  # TODO change to 85 after demo as must be 85% match
        lUser = -1  # userID of -1 means it failed for this demo purpose

    return lUser, lChance


def Log(aUserID, aStart, aEnd, aStatus):

    lDate = dt.datetime.now().isoformat()

    lLog = {
        "ID": aUserID,
        "Start": str(aStart),
        "End": str(aEnd),
        "Date": lDate,
        "Status": aStatus
    }

    with open('log.json', 'r') as f:
        lData = json.load(f)
        lData["logs"].append(lLog)

    with open('log.json','w') as f:
        json.dump(lData, f,indent=2)

    return True


def getLog(aStart, aEnd):
    if not aStart:
        return {'error': 'Missing start parameter'}
    if not aEnd:
        return {'error': 'Missing end parameter'}

    with open('log.json', 'r') as f:
        lReturnLog = json.load(f)

    aEnd = parser.parse(aEnd)
    aStart = parser.parse(aStart)
    lLogArray = {"logs": []}
    lIndex = 0;

    for log in lReturnLog['logs']:
        lTime = ((parse_date(log['Date'])).time()).replace(microsecond=0)

        if lTime >= aStart.time() and lTime <= aEnd.time():
            lLogArray["logs"].append(lReturnLog['logs'][lIndex])

        lIndex = lIndex + 1

    if len(lLogArray['logs']) == 0:
        return {'error': 'No matching logs found'}

    return lLogArray


#  TODO Deane
def Update():
    # call CIS json
    userID = 8
    image = 'GKRSBGJKSZBGKJZXFVJKB'
    lJson = {
        'ID': userID,
        'Image': image
    }
    with open('ClientInfo.json', 'w') as f:
        json.dump(lJson, f)

    return True

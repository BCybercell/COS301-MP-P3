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

    lDate = dt.datetime.now().isoformat() #TODO epoch format????

    lLog = {
        "ID": aUserID,
        "Start": str(aStart),
        "End": str(aEnd),
        "Date": lDate,
        "Status": aStatus
    }

    with open('log.json', 'r') as f:
        data = json.load(f)
        data["logs"].append(lLog)

    with open('log.json','w') as f:
        json.dump(data, f,indent=2)

    return True


def getLog(aStart, aEnd):
    if not aStart or not aEnd:
        return {'error': 'Missing parameter start or end'}
    # with open('log.json') as f:
    #     lReturnLog = json.load(f) TODO fix
    log = {}
    lReturnLog = {"logs": [{"ID": 1, "Start": "2019-03-12 18:00:00", "End": "2019-03-12 18:39:00", "Date": "2019-03-14T18:35:50.811452", "Status": True}]}
    # TODO remove dummy log
    lCount = 0

    aEnd = parser.parse(aEnd)
    aStart = parser.parse(aStart)
    for p in lReturnLog['logs']:
        dt = parse_date(p['Date'])
        if dt >= aStart and dt <= aEnd:

            # TODO Return in a format that Reporting sub-system needs
            log[lCount] = {}

            log[lCount]['UserID'] = p['ID']
            log[lCount]['Start Time'] = p['Start']
            log[lCount]['End Time'] = p['End']
            log[lCount]['Date'] = p['Date']
            log[lCount]['Status'] = p['Status']
            lCount += 1
    return log


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

import time as time
import random as Rand
import json as json
import statistics as stat
import datetime as dt
from dateutil.parser import parse as parse_date


def AuthenticateUser(aArrImg):
    Update()  # Call Update function to get new/updated list of the database from CIS
    start = time.time()
    lUserIDs = []
    lPercentages = []
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
    lChance = Rand.randint(1, 100)  # TODO need to make this the actual facial recognition function library

    lUser = Rand.randint(1, 10)  # userID just 10 users for now as example
    if lChance < 50:  # TODO change to 85 after demo as must be 85% match
        lUser = -1  # userID of -1 means it failed for this demo purpose

    return lUser, lChance


def Log(aUserID, aStart, aEnd, aStatus):

    lDate = dt.datetime.now().isoformat()

    lLog = {}
    lLog['logs'] = []
    lLog['logs'].append({
        "ID": aUserID,
        "Start": aStart,
        "End": aEnd,
        "Date": lDate,
        "Status": aStatus
    })

    with open('log.json', 'a') as f: # TODO Fix json format when appened to the file
        json.dump(lLog,f)

def getLog(aStart,aEnd):
    with open('log.json') as f:
        lReturnLog = json.load(f)
    for p in lReturnLog['logs']:
        dt = parse_date(p['Date'])
        if dt >= aStart and dt <= aEnd:

            # TODO Return in a format that Reporting sub-system needs
            print('UserID: ' + p['ID'])
            print('Start Time: ' + str(p['Start']))
            print('End Time: ' + str(p['End']))
            print('Date: ' + p['Date'])
            print('Status: ' + str(p['Status']))
            print('')


#Log(str(12345),13,14,True)
#lDate1 = dt.datetime(2019, 03, 12, 18, 00, 00)
#lDate2 = dt.datetime(2019, 03, 12, 18, 39, 00)
#getLog(lDate1,lDate2)


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

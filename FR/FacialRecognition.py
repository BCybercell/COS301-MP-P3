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

    # with open('log.json', mode='r', encoding='utf-8') as feedsjson:  TODO fix read
    #     feeds = json.load(feedsjson)

    lLog = {}
    lLog['logs'] = []
    lLog['logs'].append({
        "ID": aUserID,
        "Start": str(aStart),
        "End": str(aEnd),
        "Date": lDate,
        "Status": aStatus
    })

    # with open('log.json', 'a') as f: # TODO Fix json format when appened to the file
    #     json.dump(lLog, f)

    with open('log.json', mode='w', encoding='utf-8') as feedsjson:
        # feeds = json.load(feedsjson)
        # feeds.append(lLog)
        json.dump(lLog, feedsjson)  # TODO make feed

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
    for p in lReturnLog['logs']:
        dt = parse_date(p['Date'])
        if dt >= aStart and dt <= aEnd:

            # TODO Return in a format that Reporting sub-system needs
            log[lCount] = {}

            log[lCount]['UserID'] = p['ID']
            # print('UserID: ' + p['ID'])
            log[lCount]['Start Time'] = p['Start']
            # print('Start Time: ' + str(p['Start']))
            # print('End Time: ' + str(p['End']))
            log[lCount]['End Time'] = p['End']
            # print('Date: ' + p['Date'])
            log[lCount]['Date'] = p['Date']
            # print('Status: ' + str(p['Status']))
            log[lCount]['Status'] = p['Status']
            # print('')
            lCount += 1
    return log

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

    return True

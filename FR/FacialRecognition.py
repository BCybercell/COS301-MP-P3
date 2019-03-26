import time as time
import random as Rand
import json as json
import statistics as stat
import datetime as dt
from dateutil.parser import parse as parse_date
from dateutil import parser
import pymongo
from grdfs import GridFS
import face_recognition


client = pymongo.MongoClient("mongodb+srv://fr_dbAdmin:ZGEkMGEeTYg6fmyH@fr-db-c5rwj.gcp.mongodb.net/test?retryWrites=true")
db = client["FR-DB"]
collection = db.activeUsers
#! details = collection.find ({"Work": "id_"})

def AuthenticateUser(aArrImg):
    Update()  #Call Update function to get new/updated list of the database from CIS
    start = time.time()    
    lUserId = AuthenticateImage(aArrImg) #!Magic happens in the AuthenticateImage Function

    if lUserId == -1:
        status = False
    else: status = True

    end = time.time()
    Log(lUserId, start, end,status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)

    return lUserId


def AuthenticateImage(aImg):
    if not aImg:
        return -1

    #Read images from database and compare till match or no images left
    allData = collection.find() #Contains every element in the database
    imageFromDb = []
    imagetoTest = face_recognition.load_image_file(aImg) #Image they send us encoded
    image_encoding = face_recognition.face_encodings(imagetoTest,num_jitters=100)[0]

    for cursor in allData: #cursor here acts as a iterator for each image
        for img in cursor.image:
            imageFromDb.append(face_recognition.load_image_file(img))
        for i in imageFromDb:
            #!Compare the face we just encoded with the one sent through
            result_encoding = face_recognition.face_encodings(i)[0]
            result = (face_recognition.compare_faces([result_encoding], image_encoding, tolerance=0.5))
            #*If it was true and matched then return the userId
            if result == True:
                return cursor.userID
    
    return -1
        

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

    aEnd = parser.parse(aEnd)
    aStart = parser.parse(aStart)
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

import time as time
import random as Rand
import json as json
#import statistics as stat
import datetime as dt
from dateutil.parser import parse as parse_date
from dateutil import parser
import pymongo
# from gridfs import GridFS   #  if you want this to work please let me know - Deane
import face_recognition
import json
from bson import json_util
import base64


client = pymongo.MongoClient("mongodb+srv://fr_dbAdmin:ZGEkMGEeTYg6fmyH@fr-db-c5rwj.gcp.mongodb.net/test?retryWrites=true")
db = client["FR-DB"]
collection = db.testing  # change back to activeUsers
#! details = collection.find ({"Work": "id_"})


def AddImages(userID, aArrImg):
    start = int(time.time())

    allData = collection.find()
    print allData
    status = False

    for key in allData:
        if key.get("userID") == userID:
            #add images to db
            for img in aArrImg:
                encoded_string = base64.b64encode(img)
                strr = encoded_string
                myquery = { "userID": str(userID) }
                newvalues = { "$push": { "photos": [strr] } }
                x = collection.update_one(myquery, newvalues)
            status = True


    end = int(time.time())
    Log(userID, start, end, status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)

    return status
        

def Log(aUserID, aStart, aEnd, aStatus):
    #Work on the collection log
    logTest = db['logTest']  # TODO fix
    # logCollection =db.log
    # TODO change time format to epoc
    lDate = dt.datetime.now().isoformat()  # ?Does this still need to change?
    dataToLog = {
        "ID": aUserID,
        "Start": str(aStart),
        "End": str(aEnd),
        "Date": lDate,
        "Status": aStatus
    }
    # Do the query and if it returns false loop till it returns true
    y = logTest.insert_one(dataToLog)

    return True

AddImages("1", "/test.jpg") #TODO remove this - only for testing
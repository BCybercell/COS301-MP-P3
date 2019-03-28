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
    Log(lUserId, start, end, status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)

    return lUserId


def AuthenticateImage(aImg):
    if not aImg:
        return -1

    # Read images from database and compare till match or no images left
    allData = collection.find()  # Contains every element in the database
    imageFromDb = []
    results = []
    imagetoTest = face_recognition.load_image_file(aImg)  # Image they send us encoded
    image_encoding = face_recognition.face_encodings(imagetoTest, num_jitters=100)[0]

#! Adds all the images and IDs to a tuple, imageFromDb
    print("Getting IMAGES from database:")
    for key in allData:
        for img in key.get("photos"):
            imageFromDb.append(tuple((key.get("userID"), face_recognition.load_image_file(img))))
            print("IMG:" + str(img))

    # for cursor in allData: #cursor here acts as a iterator for each image
    #     for img in cursor.image:
    #         imageFromDb.append(face_recognition.load_image_file(img))
    #     for i in imageFromDb:
    #         #!Compare the face we just encoded with the one sent through
    #         result_encoding = face_recognition.face_encodings(i)[0]
    #         result = (face_recognition.compare_faces([result_encoding], image_encoding, tolerance=0.5))
    #         #*If it was true and matched then return the userId
    #         if result == True:
    #             return cursor.userID

    #!This loops through the tuple list imageFromDB and compares it . Once a true is hit it retrieves the id from the tuple and returns it
    counter = 0
    for i, j in imageFromDb:
        test = face_recognition.face_encodings(j, num_jitters=10)[0]
        results.append(face_recognition.compare_faces([test], image_encoding, tolerance=0.6))  
        for e in results[counter]:
            if e:
                print("The image matched and returned userID:" + str(i))
                return i
        counter = counter + 1
    return -1
        

def Log(aUserID, aStart, aEnd, aStatus):
    #Work on the collection log 
    logCollection =db.log
    #TODO change time format to epoc
    lDate = dt.datetime.now().isoformat()#?Does this still need to change?
    dataToLog = {
        "ID": aUserID,
        "Start": str(aStart),
        "End": str(aEnd),
        "Date": lDate,
        "Status": aStatus
    }
    #Do the query and if it returns false loop till it returns true
    y = logCollection.insert_one(dataToLog)
    if not y:
        while not y:
             y = logCollection.insert_one(dataToLog)   
    #when done then return true. Ensures it never breaks
    return True


def getLog(aStart, aEnd):
    if not aStart:
        return {'error': 'Missing start parameter'}
    
    log = {}
    logCol =db.log

    #Get the data between the two dates from the db
    log = logCol.find({
        "Date":
        {
            "$gte": aStart,
            "$lt": aEnd
        }
        })
    #TODO might need to change this. Depends on what they need

    # lIndex = lIndex + 1
    #
    # if len(lLogArray['logs']) == 0:
    #     return {'error': 'No matching logs found'}

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

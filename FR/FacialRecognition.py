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
collection = db.activeUsers
#! details = collection.find ({"Work": "id_"})


def AuthenticateUser(aArrImg):
    Update()  # Call Update function to get new/updated list of the database from CIS
    start = int(time.time())
    lUserId = AuthenticateImage(aArrImg)  # !Magic happens in the AuthenticateImage Function

    if lUserId == -1:
        status = False
    else: status = True

    end = int(time.time())
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

    # Have a counter for the file naming
    counter = 0
#! Adds all the images and IDs to a tuple, imageFromDb
    print("Getting IMAGES from database:")
    for key in allData:
        for img in key.get("photos"):
            # Decode the base64 string
            dec_img =base64.decodestring(img)
            # create a name for the file. example userIDCounter.jpg thus 01.jpg
            st = str(key.get("userID"))+str(counter)+".jpg"
            counter = counter +1
            # save the binary as an image to use
            with open(st, 'wb') as f:
                f.write(dec_img)
            # now append and let the magic happen
            imageFromDb.append(tuple((key.get("userID"), face_recognition.load_image_file("./"+st))))
            print("IMG:" + str(img))

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
    if not y:
        while not y:
            y = logTest.insert_one(dataToLog)
    # when done then return true. Ensures it never breaks
    return True


def getLog(aStart, aEnd):
    if not aStart:
        return {'error': 'Missing start parameter'}

    logCol = db.logTest

    # Get the data between the two dates from the db
    log = logCol.find({
        # "Date":
        # {
        #     "$gte": aStart,
        #     "$lt": aEnd
        # }
        # })
        "Start":
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


    json_docs = []
    for doc in log:
        json_doc = json.dumps(doc, default=json_util.default)
        json_docs.append(json_doc)
    return json_docs


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

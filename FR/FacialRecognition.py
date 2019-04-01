import time as time
import random as Rand
import json as json
#import statistics as stat
import datetime as dt
from dateutil.parser import parse as parse_date
from dateutil import parser
import pymongo
# from gridfs import GridFS   #  if you want this to work please let me know - Deane
#import face_recognition
import json
from bson import json_util
import base64


client = pymongo.MongoClient("mongodb+srv://fr_dbAdmin:ZGEkMGEeTYg6fmyH@fr-db-c5rwj.gcp.mongodb.net/test?retryWrites=true")
db = client["FR-DB"]
collection = db.testing  # change back to activeUsers
#! details = collection.find ({"Work": "id_"})


# def AuthenticateUser(aArrImg):
#     # Update()  # Call Update function to get new/updated list of the database from CIS
#     start = int(time.time())
#     lUserId = AuthenticateImage(aArrImg)  # !Magic happens in the AuthenticateImage Function
#
#     if lUserId == -1:
#         status = False
#     else: status = True
#
#     end = int(time.time())
#     Log(lUserId, start, end, status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)
#
#     return lUserId
#
#
# def AuthenticateImage(aImg):
#     if not aImg:
#         return -1
#     # Read images from database and compare till match or no images left
#     allData = collection.find()  # Contains every element in the database
#     imageFromDb = []
#     results = []
#     imagetoTest = face_recognition.load_image_file(aImg)  # Image they send us encoded
#     image_encoding = face_recognition.face_encodings(imagetoTest, num_jitters=100)[0]
#
#     # Have a counter for the file naming
#     counter = 0
#     # ! Adds all the images and IDs to a tuple, imageFromDb
#     print("Getting IMAGES from database:")
#     for key in allData:
#         for img in key.get("photos"):
#             # Decode the base64 string
#             dec_img = base64.decodebytes(img)
#             # create a name for the file. example userIDCounter.jpg thus 01.jpg
#             st = str(key.get("userID"))+str(counter)+".jpg"
#             counter = counter + 1
#             # save the binary as an image to use
#             with open(st, 'wb') as f:
#                 f.write(dec_img)
#             # now append and let the magic happen
#             imageFromDb.append(tuple((key.get("userID"), face_recognition.load_image_file("./"+st))))
#             print("IMG:" + str(img))
#
#     #This loops through the tuple list imageFromDB and compares it . Once a true is hit it retrieves the id from the tuple and returns it
#     counter = 0
#     for i, j in imageFromDb:
#         test = face_recognition.face_encodings(j, num_jitters=10)[0]
#         results.append(face_recognition.compare_faces([test], image_encoding, tolerance=0.6))
#         for e in results[counter]:
#             if e:
#                 print("The image matched and returned userID:" + str(i))
#                 return i
#         counter = counter + 1
#     return -1

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

#
# def Log(aUserID, aStart, aEnd, aStatus):
#     #Work on the collection log
#     logTest = db['logTest']  #TODO update collection when ready
#     #logCollection =db.['log']
#
#     lDate = dt.datetime.now().isoformat()
#     lData = {
#         "ID": aUserID,
#         "Start": str(aStart),
#         "End": str(aEnd),
#         "Date": lDate,
#         "Status": aStatus
#     }
#
#     #TODO Make this asynchronous
#     # Do the query and if it returns false loop until it returns true - ensures that the log is always written to DB
#     log = logTest.insert_one(lData)
#     if not log:
#         while not log:
#             log = logTest.insert_one(lData)
#     return True
#
#
# def getLog(aStart, aEnd):
#     if not aStart:
#         return {'error': 'Missing start parameter'}
#     if not aEnd:
#         return {'error': 'Missing end parameter'}
#
#     logTest = db['logTest']
#
#     #Get the data between the two dates from the db
#     # lquery = {"$and:" [{ "Start": {"$gte":aStart}}, {"End": {"$lte": aEnd}}]}
#     lquery = { "Date": {"$gte":aStart, "$lt":aEnd}}
#     print(lquery)
#     log = logTest.find(lquery)
#
#     for l in log:
#         print(l)
#
#     #TODO might need to change this. Depends on what they need
#
#     # lIndex = lIndex + 1
#
#     if not log:
#         return {'error': 'No matching logs found'}
#
#     if log:
#         return "Working"
#
#     json_docs = []
#     for doc in log:
#         json_doc = json.dumps(doc, default=json_util.default)
#         json_docs.append(json_doc)
#     return json_docs


# #  TODO Deane
# def Update():
#     # call CIS json
#     userID = 8
#     image = 'GKRSBGJKSZBGKJZXFVJKB'
#     lJson = {
#         'ID': userID,
#         'Image': image
#     }
#     with open('ClientInfo.json', 'w') as f:
#         json.dump(lJson, f)
#
#     return True

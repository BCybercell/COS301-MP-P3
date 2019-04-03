import time as time
import random as Rand
import json as json
#import statistics as stat
import datetime as dt
import pymongo
# from gridfs import GridFS   #  if you want this to work please let me know - Deane
import face_recognition
import os 
from bson import json_util
import base64
from dateutil.parser import parse as parse_date
from dateutil import parser


client = pymongo.MongoClient("mongodb://fr_dbAdmin:ZGEkMGEeTYg6fmyH@ds017155.mlab.com:17155/heroku_6lqvmjth")
db = client["heroku_6lqvmjth"]
collection = db.testingRichard

# app = Flask(__name__)
# @app.route('/favicon.ico') 
# def favicon(): 
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
# @app.route("/AuthenticateUser",methods=['Get'])
def AuthenticateUser(aArrImg):
    start = time.time()
    lUserId = AuthenticateImage(aArrImg)  # !Magic happens in the AuthenticateImage Function

    if lUserId == -1:
        status = False
    else:
        status = True

    end = int(time.time())
    Log(lUserId, start, end,status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)
    return lUserId

def AddImages(userID, aArrImg):
    start = int(time.time())

    allData = collection.find()
    status = False

    for key in allData:
        if key.get("userID") == userID:
            encoded_string = base64.b64encode(aArrImg)
            strr = encoded_string
            myquery = {"userID": str(userID)}
            newvalues = {"$push": {"photos": [strr]}}
            x = collection.update_one(myquery, newvalues)
            status = True
    end = int(time.time())
    Log(userID, start, end, status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)

    return status


def AuthenticateImage(aImg):
    if not aImg:
        return -1
    # Read images from database and compare till match or no images left
    allData = collection.find()  # Contains every element in the database
    # imageFromDb = []
    results = []
    imagetoTest = face_recognition.load_image_file(aImg)  # Image they send us encoded
    image_encoding = face_recognition.face_encodings(imagetoTest)[0]

    # Have a counter for the file naming
    counter = 0
    print("Getting IMAGES from database:")
    
    # for key in allData:
    #     for img in key.get("photos"):
    #         dec_img = base64.decodebytes(img)
    #         #create a name for the file. example userIDCounter.jpg thus 01.jpg
    #         st = str(key.get("userID"))+str(counter)+".jpg"
    #         #save the binary as an image to use
    #         with open(st, 'wb') as f:
    #             f.write(dec_img)
    #         #now append and let the magic happen
    #         imageFromDb = (tuple((key.get("userID"),face_recognition.load_image_file("./"+st))))
    #         for i,j in imageFromDb:
    #             test = face_recognition.face_encodings(j)[0]
    #             results.append(face_recognition.compare_faces([test], image_encoding, tolerance=0.6))  
    #             for e in results[counter]:
    #                 if e == True:
    #                     print("The image matched and returned userID:"+ str(i))
    #                     obj = {"userID":i}
    #                     return obj
    #             counter = counter +1
    for key in allData:
        for img in key.get("photos"):
            dec_img = base64.decodebytes(img)
            # create a name for the file. example userIDCounter.jpg thus 01.jpg
            st = str(key.get("userID"))+str(counter)+".jpg"
            # save the binary as an image to use
            with open(st, 'wb') as f:
                f.write(dec_img)
            # now append and let the magic happen
            # imageFromDb = (tuple((key.get("userID"),face_recognition.load_image_file("./"+st))))
            imageID = key.get("userID")
            imageFromDB = face_recognition.load_image_file("./"+st)
            # for i,j in imageFromDb:
            test = face_recognition.face_encodings(imageFromDB)[0]
            results = (face_recognition.compare_faces([test], image_encoding, tolerance=0.6))  
            for e in results:
                if e == True:
                    #print("The image matched and returned userID:"+ str(imageFromDB[0]))
                    obj = {"userID":imageID}
                    return obj
            counter = counter +1
    return -1

    # def finalWork():
    #     counter = 0
    #     for i,j in imageFromDb:
    #         test = face_recognition.face_encodings(j)[0]
    #         results.append(face_recognition.compare_faces([test], image_encoding, tolerance=0.6))  
    #         for e in results[counter]:
    #             if e == True:
    #                 print("The image matched and returned userID:"+ str(i))
    #                 obj = {"userID":i}
    #                 return obj
    #         counter = counter +1
    #     return -1
    # def decodeImage(img,counter,key):
    #     #Decode the base64 string
    #         dec_img = base64.decodebytes(img)
    #         #create a name for the file. example userIDCounter.jpg thus 01.jpg
    #         st = str(key.get("userID"))+str(counter)+".jpg"
    #         #save the binary as an image to use
    #         with open(st, 'wb') as f:
    #             f.write(dec_img)
    #         #now append and let the magic happen
    #         imageFromDb.append(tuple((key.get("userID"),face_recognition.load_image_file("./"+st))))
    #         return ("IMG:"+ str(img))
            
    # def design():
    #     print("Getting IMAGES from database:")
    #     counter =0
    #     for key in allData:
    #         for img in key.get("photos"):
    #             yield "<p>Getting IMAGEs from Database"
    #             yield decodeImage(img,counter,key)
    #             counter = counter +1
    #     returnObj =  finalWork()
    # return Response(design()) 


# AuthenticateUser("./test1.jpg")
def Log(aUserID, aStart, aEnd, aStatus):

    lDate = dt.datetime.now().time().replace(microsecond=0).isoformat()

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

#BACKUP LOG CODE FOR DB IN CASE LOG FILE FAILS
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

if __name__ == "FacialRecognition":
    app.run(debug=True)

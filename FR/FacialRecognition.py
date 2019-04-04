import time as time
import random as Rand
import json as json
# import statistics as stat
import datetime as dt
import pymongo
# import face_recognition
import json
import requests
import os 
from bson import json_util
import base64
from dateutil.parser import parse as parse_date
from dateutil import parser



client = pymongo.MongoClient("mongodb://fr_dbAdmin:ZGEkMGEeTYg6fmyH@ds017155.mlab.com:17155/heroku_6lqvmjth")
db = client["heroku_6lqvmjth"]
collection = db.testingRichard
testClient = db.testingTegan

# app = Flask(__name__)
# @app.route('/favicon.ico') 
# def favicon(): 
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
# @app.route("/AuthenticateUser",methods=['Get'])
# def AuthenticateUser(aArrImg):
#     start = int(time.time())
#     lUserId = AuthenticateImage(aArrImg)  # !Magic happens in the AuthenticateImage Function
#
#     if lUserId == -1:
#         status = False
#     else:
#         status = True
#
#     end = int(time.time())
#     Log(lUserId, start, end,status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)
#     return lUserId
#
# def AddImages(userID, aArrImg):
#     start = int(time.time())
#
#     allData = collection.find()
#     status = False
#
#     for key in allData:
#         if key.get("userID") == userID:
#             for img in aArrImg.read():
#                 encoded_string = base64.b64encode(img)
#                 strr = encoded_string
#                 myquery = {"userID": str(userID)}
#                 newvalues = {"$push": {"photos": strr}}
#                 x = collection.update_one(myquery, newvalues)
#             status = True
#     end = int(time.time())
#     Log(userID, start, end, status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)
#
#     return status
#
#
# def AuthenticateImage(aImg):
#     if not aImg:
#         return -1
#     # Read images from database and compare till match or no images left
#     allData = collection.find()  # Contains every element in the database
#     # imageFromDb = []
#     results = []
#     imagetoTest = face_recognition.load_image_file(aImg)  # Image they send us encoded
#     image_encoding = face_recognition.face_encodings(imagetoTest)[0]
#
#     # Have a counter for the file naming
#     counter = 0
#     print("Getting IMAGES from database:")
#
#     for key in allData:
#         for img in key.get("photos"):
#             dec_img = base64.decodebytes(img)
#             # create a name for the file. example userIDCounter.jpg thus 01.jpg
#             st = str(key.get("userID"))+str(counter)+".jpg"
#             # save the binary as an image to use
#             with open(st, 'wb') as f:
#                 f.write(dec_img)
#             # now append and let the magic happen
#             # imageFromDb = (tuple((key.get("userID"),face_recognition.load_image_file("./"+st))))
#             imageID = key.get("userID")
#             imageFromDB = face_recognition.load_image_file("./"+st)
#             # for i,j in imageFromDb:
#             test = face_recognition.face_encodings(imageFromDB)[0]
#             results = (face_recognition.compare_faces([test], image_encoding, tolerance=0.6))
#             for e in results:
#                 if e == True:
#                     #print("The image matched and returned userID:"+ str(imageFromDB[0]))
#                     obj = {"userID":imageID}
#                     return obj
#             counter = counter +1
#     return -1

##################################
#            SEND LOG
#    Pushes log to Reporting
##################################
def sendLog(aLogJSON):

    url = 'https://fnbreports-6455.nodechef.com/api'
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(aLogJSON), headers=headers)

    print(aLogJSON)
    if response:
        return True

    return False

##################################
#             LOG
#    Logs all authenication
#           details
##################################
def Log(aUserID, aStatus):

    lTimestamp = int(time.time())

    lLog = {
        "ID": str(aUserID),
        "Timestamp": lTimestamp,
        "Success": aStatus
    }

    json_log = json.dumps(lLog, separators=(',', ':'))

    lDataToReporting = { "system":"FRS", "data":json_log}



    with open('log.json', 'r') as f:
        lData = json.load(f)
        lData["logs"].append(lLog)

    with open('log.json','w') as f:
        json.dump(lData, f,indent=2)

    sendLog(lDataToReporting)

    return True

##################################
#           ADD CLIENT
#    Adds a client to our DB
#    *This user has no images*
##################################
def addClient(aClientID):

    #Check if the user already exist
    lFoundClient = testClient.find({ "userID": aClientID })

    if lFoundClient:
        reactivateClient(aClientID)
    elif not lFoundClient:
        newClient = {
            "userID" : str(aClientID),
            "status" : True,
            "photos" : []
        }

        testClient.insert_one(newClient)

    return

##################################
#      DEACTIVATE CLIENT
#    Deactivates client status
#     *Doesn't delete client*
##################################
def deactivateClient(aClientID):

    query = {"userID" : str(aClientID)}
    newValue = {"$set": { "status": False}}

    testClient.update_one(query, newValue)

##################################
#      REACTIVATE CLIENT
#    Reactivates client status
##################################
def reactivateClient(aClientID):

    query = {"userID" : str(aClientID)}
    newValue = {"$set": { "status": True}}

    testClient.update_one(query, newValue)


##################################
#        SYNCLIST CLIENT
#    Gets initial clients from
#            CIS
##################################
def syncList(aClientList):

    for client in aClientList["ID"]:
        addClient(client)

##################################
#        CHECK OPERATION
#       Checks CIS requests
##################################
def checkClientOperation(aClientJSON):

    if aClientJSON["Operation"] == "CREATE":
        addClient(aClientJSON["ID"])
    elif aClientJSON["Operation"] == "DELETE":
        deactivateClient(aClientJSON["ID"])
    elif aClientJSON["Operation"] == "subscribed":
        syncList(aClientJSON)




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




if __name__ == "FacialRecognition":
    app.run(debug=True)

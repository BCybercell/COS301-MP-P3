import time as time
import pymongo
import face_recognition
import json
import requests
import base64
import numpy as np
from django.views.decorators.csrf import csrf_exempt

client = pymongo.MongoClient("mongodb://fr_dbAdmin:ZGEkMGEeTYg6fmyH@ds017155.mlab.com:17155/heroku_6lqvmjth")
db = client["heroku_6lqvmjth"]
collection = db["CIS_Client"]
testClient = db["CIS_Client"]
testKyle = db["CIS_Client"]

def AuthenticateUser(aArrImg):
    start = time.time()   
    lUserId = AuthenticateImage(aArrImg)  # !Magic happens in the AuthenticateImage Function

    if 'userID' in lUserId:
        status = True
        Log(lUserId['userID'], status)
    else:
        status = False

    end = time.time()
      # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)
    return lUserId

def AddImages(userID, aArrImg):     #TODO Kyle
    if not aArrImg:
        return False
    if not userID:
        return False
    # start = int(time.time())
    encoding = []
    allData = testKyle.find()
    status = False
    #strr=[]
    for key in allData:
        if key.get("userID") == userID:
            #for img in aArrImg:
            encoded_string = base64.b64encode(aArrImg.read())
            encoding.append(np.array(face_recognition.face_encodings(face_recognition.load_image_file(aArrImg))[0]).tolist())
                    #strr.append(encoded_string)
                    #myquery = {"userID": str(userID)}
                    #newvalues = {"$push": {"photos": strr}}
                    #x = collection.update_one(myquery, newvalues)
            myquery = {"userID": str(userID)}
            newvalues = {"$push": {"photos": encoded_string, "endoding":encoding[0]}}       #newvalues = {"$push": {"photos": encoded_string}}
            x = testKyle.update_one(myquery, newvalues)
            status = True
    # end = int(time.time())
    # Log(userID, start, end, status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)

    return status

@csrf_exempt
def AuthenticateUserTest(aArrImg):
    start = time.time()
    lUserId = AuthenticateImageTest(aArrImg) #!Magic happens in the AuthenticateImage Function

    if 'userID' in lUserId:
        status = True
        Log(lUserId['userID'], status)

    else:
        status = False

    end = time.time()

    return lUserId


def AuthenticateImage(aImg):
    if not aImg:
        return {"Exception":"Not Authenticated"}
    dec_img =base64.decodestring(aImg)
    #create a name for the file. example userIDCounter.jpg thus 01.jpg
    st = "test.jpg"
    #save the binary as an image to use
    with open(st, 'wb') as f:
        f.write(dec_img)

    results = []
    imagetoTest = face_recognition.load_image_file("test.jpg") #Image they send us encoded
    image_encoding = face_recognition.face_encodings(imagetoTest)[0]

    #Have a counter for the file naming
    counter = 0
    print("Getting IMAGES from database:")
    j = collection.count()
    for i in range(j):
        allData = collection.find({"userID":str(counter)})
        for key in allData:
            imageID = key.get("userID")
            counter = counter +1
            if key.get("endoding"):
                test = np.asarray(key.get("endoding")[0]) # face_recognition.face_encodings(imageFromDB)[0]
                results = (face_recognition.compare_faces([test], image_encoding, tolerance=0.6))
                for e in results:
                    if e == True:
                        print("The image matched and returned userID:")
                        obj = {"userID":imageID}
                        print(imageID)
                        return obj

    return {"Exception":"Not Authenticated"}
    # for key in allData:
    #     imageCounter = 0 #!Added a counter for the sole purpose of only looking at two images. After that it will most likely not recognize if the first two failed
    #     for img in key.get("photos"):
    #         if imageCounter < 1:
    #             #dec_img = base64.decodebytes(img)
    #             # create a name for the file. example userIDCounter.jpg thus 01.jpg
    #             # st = str(key.get("userID"))+str(counter)+".jpg"
    #             # #save the binary as an image to use
    #             # with open(st, 'wb') as f:
    #             #     f.write(dec_img)
    #             # st = imread(io.BytesIO(dec_img))

    #             # imageID = key.get("userID")
    #             # imageFromDB = face_recognition.load_image_file(st+".jpg")
    #             # print("here")
                
    #             # counter = counter +1
    #             # imageCounter = imageCounter + 1
    #              #now append and let the magic happen
    #             imageID = key.get("userID")
    #             # imageFromDB = face_recognition.load_image_file("./"+st)
              
    #             counter = counter +1
    #             imageCounter = imageCounter + 1

                
    #             test = np.asarray(key.get("endoding")[0]) # face_recognition.face_encodings(imageFromDB)[0]
    #             results = (face_recognition.compare_faces([test], image_encoding, tolerance=0.6))  

    #             # test = face_recognition.face_encodings(imageFromDB)[0]
    #             # results = (face_recognition.compare_faces([test], image_encoding, tolerance=0.6))  
    #             for e in results:
    #                 if e == True:
    #                     print("The image matched and returned userID:")
    #                     print(imageID)
    #                     obj = {"userID":imageID}
    #                     return obj
    #         else:
    #             break
    # return -1

##################################
#            SEND LOG
#    Pushes log to Reporting
##################################
def AuthenticateImageTest(aImg):
    if not aImg:
        return {"Exception":"Not Authenticated"}

    #Read images from database and compare till match or no images left
    #allData = collection.find() #Contains every element in the database

    results = []
    imagetoTest = face_recognition.load_image_file(aImg) #Image they send us encoded
    image_encoding = face_recognition.face_encodings(imagetoTest)[0]

    #Have a counter for the file naming
    counter = 0
    print("Getting IMAGES from database:")
    j = collection.count()
    for i in range(j):
        allData = collection.find({"userID":str(34041)})
        for key in allData:
            imageID = key.get("userID")
            counter = counter +1
            if key.get("endoding"):
                test = np.asarray(key.get("endoding")[0]) # face_recognition.face_encodings(imageFromDB)[0]
                results = (face_recognition.compare_faces([test], image_encoding, tolerance=0.6))
                for e in results:
                    if e == True:
                        print("The image matched and returned userID:")
                        obj = {"userID":imageID}
                        print(imageID)
                        return obj
            # test = np.asarray(key.get("endoding")[0]) # face_recognition.face_encodings(imageFromDB)[0]
            # results = (face_recognition.compare_faces([test], image_encoding, tolerance=0.6))
            # for e in results:
            #     if e == True:
            #         print("The image matched and returned userID:")
            #         obj = {"userID":imageID}
            #         print(imageID)
            #         return obj

    return {"Exception":"Not Authenticated"}

def sendLog(aLogJSON):

    url = 'https://fnbreports-6455.nodechef.com/api'
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(aLogJSON), headers=headers)

    if response:
        return True
    elif not response:
         with open('log.json', 'r') as f:
             lData = json.load(f)
             lData["logs"].append(aLogJSON)
         with open('log.json','w') as f:
            json.dump(lData, f,indent=2)


    return False

##################################
#             LOG
#    Logs all authenication
#           details
##################################
def Log(aUserID, aStatus):

    # d = datetime.strptime(int(round(time.time() * 1000)), "%d.%m.%Y %H:%M:%S,%f").strftime('%s')
    d_in_ms = int(round(time.time() * 1000))

    lLog = [{
        "ID": str(aUserID),
        "timestamp": d_in_ms,
        "Success": aStatus
    }]

    json_log = json.dumps(lLog, separators=(',', ':'))

    lDataToReporting = {"system":"FRS", "data":json_log}

    sendLog(lDataToReporting)

    return True

##################################
#           ADD CLIENT
#    Adds a client to our DB
#    *This user has no images*
##################################
def addClient(aClientID):
    aClientID = json.loads(aClientID)
    #Check if the user already exist
    # if testClient.count_documents({"userID": "3"}) == 1:
    #     reactivateClient(aClientID)
    # elif not testClient.count_documents({"userID": "3"}) == 1:
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
    # aClientID = json.loads(aClientID)
    query = {"userID" : str(aClientID)}
    newValue = {"$set": { "status": False}}

    testClient.update_one(query, newValue)

##################################
#      REACTIVATE CLIENT
#    Reactivates client status
##################################
def reactivateClient(aClientID):
    # aClientID = json.loads(aClientID)
    query = {"userID" : str(aClientID)}
    newValue = {"$set": { "status": True}}

    testClient.update_one(query, newValue)


##################################
#        SYNCLIST CLIENT
#    Gets initial clients from
#            CIS
##################################
def syncList(aClientListJson):
    # lClientList = json.loads(aClientListJson)

    for client in aClientListJson:

        addClient(client)

##################################
#        CHECK OPERATION
#       Checks CIS requests
##################################
def checkClientOperation(aClientJSON):

    if aClientJSON["Operation"] == "CREATE":
        addClient(aClientJSON["ID"])

    if aClientJSON["Operation"] == "DELETE":
        print(aClientJSON["ID"])
        deactivateClient(aClientJSON["ID"])

    if aClientJSON["Operation"] == "subscribed":
        syncList(aClientJSON["ID"])

if __name__ == "FacialRecognition":
    app.run(debug=True)

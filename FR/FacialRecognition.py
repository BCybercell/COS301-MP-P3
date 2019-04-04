import time as time
import random as Rand
import json as json
import statistics as stat
import datetime as dt
import pymongo
from gridfs import GridFS
import face_recognition
import os 
import base64
import io
from imageio import imread

client = pymongo.MongoClient("mongodb://fr_dbAdmin:ZGEkMGEeTYg6fmyH@ds017155.mlab.com:17155/heroku_6lqvmjth")
db = client["heroku_6lqvmjth"]
collection = db.testingRichard

def AuthenticateUser(aArrImg):
   # Update()  #Call Update function to get new/updated list of the database from CIS

    start = int(time.time())    
    lUserId = AuthenticateImage(aArrImg) #!Magic happens in the AuthenticateImage Function

    if lUserId == -1:
        status = False
    else: status = True

    end = int(time.time())
    #?Log commented out for the sake that I do not have the working code,
    #Log(lUserId,status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)

    return lUserId


def AuthenticateImage(aImg):
    if not aImg:
        return -1

    #Read images from database and compare till match or no images left
    allData = collection.find() #Contains every element in the database

    results = []
    imagetoTest = face_recognition.load_image_file(aImg) #Image they send us encoded
    image_encoding = face_recognition.face_encodings(imagetoTest)[0]

    #Have a counter for the file naming
    counter = 0
    print("Getting IMAGES from database:")
    for key in allData:
        imageCounter = 0 #!Added a counter for the sole purpose of only looking at two images. After that it will most likely not recognize if the first two failed
        for img in key.get("photos"):
            if imageCounter < 1:
                dec_img = base64.decodebytes(img)
                # create a name for the file. example userIDCounter.jpg thus 01.jpg
                # st = str(key.get("userID"))+str(counter)+".jpg"
                # #save the binary as an image to use
                # with open(st, 'wb') as f:
                #     f.write(dec_img)
                st = imread(io.BytesIO(dec_img))

                imageID = key.get("userID")
                imageFromDB = face_recognition.load_image_file(st+".jpg")
                print("here")
                counter = counter +1
                imageCounter = imageCounter + 1

                test = face_recognition.face_encodings(imageFromDB)[0]
                results = (face_recognition.compare_faces([test], image_encoding, tolerance=0.6))  
                for e in results:
                    if e == True:
                        print("The image matched and returned userID:")
                        print(imageID)
                        obj = {"userID":imageID}
                        return obj
            else:
                break
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


AuthenticateUser("./test5.jpg")
def getLog(aStart, aEnd):
    if not aStart or not aEnd:
        return {'error': 'Missing parameter start or end'}
    
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


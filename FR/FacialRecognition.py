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
from flask import Flask,Response,send_from_directory,request


client = pymongo.MongoClient("mongodb://fr_dbAdmin:ZGEkMGEeTYg6fmyH@ds017155.mlab.com:17155/heroku_6lqvmjth")
db = client["heroku_6lqvmjth"]
collection = db.richardTest

app = Flask(__name__)
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/AuthenticateUser",methods=['GET'])
def AuthenticateUser():
   # Update()  #Call Update function to get new/updated list of the database from CIS
    aArrImg = request.args.get("image")
    start = time.time()    
    lUserId = AuthenticateImage(aArrImg) #!Magic happens in the AuthenticateImage Function

    if lUserId == -1:
        status = False
    else: status = True

    end = time.time()
    #Log(lUserId, start, end,status)  # call Log() which logs the time,status of finding and the userId(-1 if not found, Most likely when status is false)

    return lUserId


def AuthenticateImage(aImg):
    if not aImg:
        return -1

    #Read images from database and compare till match or no images left
    allData = collection.find() #Contains every element in the database
    imageFromDb = []
    results = []
    imagetoTest = face_recognition.load_image_file(aImg) #Image they send us encoded
    image_encoding = face_recognition.face_encodings(imagetoTest)[0]

    #Have a counter for the file naming
    counter = 0
    def finalWork():
        counter = 0
        for i,j in imageFromDb:
            test = face_recognition.face_encodings(j)[0]
            results.append(face_recognition.compare_faces([test], image_encoding, tolerance=0.6))  
            for e in results[counter]:
                if e == True:
                    print("The image matched and returned userID:"+ str(i))
                    obj = {"userID":i}
                    return obj
            counter = counter +1
        return -1
    def decodeImage(img,counter,key):
        #Decode the base64 string
            dec_img = base64.decodebytes(img)
            #create a name for the file. example userIDCounter.jpg thus 01.jpg
            st = str(key.get("userID"))+str(counter)+".jpg"
            #save the binary as an image to use
            with open(st, 'wb') as f:
                f.write(dec_img)
            #now append and let the magic happen
            imageFromDb.append(tuple((key.get("userID"),face_recognition.load_image_file("./"+st))))
            return ("IMG:"+ str(img))
            
    def design():
        print("Getting IMAGES from database:")
        counter =0
        for key in allData:
            for img in key.get("photos"):
                yield "<p>Getting IMAGEs from Database"
                yield decodeImage(img,counter,key)
                counter = counter +1
        finalWork()
    return Response(design()  ) 



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

if __name__ == "FacialRecognition":
    app.run(debug=True)
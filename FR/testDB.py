import pymongo 
import base64
import gridfs
import face_recognition
import numpy as np

myclient = pymongo.MongoClient("mongodb://fr_dbAdmin:ZGEkMGEeTYg6fmyH@ds017155.mlab.com:17155/heroku_6lqvmjth")

mydb = myclient["heroku_6lqvmjth"]
mycol = mydb["secondRichard"]
strr=[]
encoding =[]
for i in range(11):
  s = "./"+str(i+1)+".jpg"
  with open(s, "rb") as imageFile:
       encoded_string = base64.b64encode(imageFile.read())
       strr.append(encoded_string)
       encoding.append(np.array(face_recognition.face_encodings(face_recognition.load_image_file("./"+s))[0]).tolist())
       


exampleActiveUser = {
        "userID" : "0", #ID should be stored as a string
        "status" : True,
        "photos" : [
            strr[0],strr[1],strr[2],strr[3],strr[4]
        ],
        "endoding":
        [
          encoding[0],encoding[1],encoding[2],encoding[3],encoding[4]
        ]
    }
x = mycol.insert_one(exampleActiveUser)
#print("Active user example: " + str(exampleActiveUser))
exampleActiveUserTwo = {
    "userID" : "1", #ID should be stored as a string
    "status" : True,
    "photos" : [
      strr[5],strr[6],strr[7]
    ],
    "endoding":
    [
      encoding[5],encoding[6],encoding[7]
    ]
}
y = mycol.insert_one(exampleActiveUserTwo)
exampleActiveUserThree = {
    "userID" : "2", #ID should be stored as a string
    "status" : True,
    "photos" : [
      strr[8],strr[9],strr[10]
    ],
    "endoding":
    [
      encoding[8],encoding[9],encoding[10]
    ]
}
z = mycol.insert_one(exampleActiveUserThree)
#print("Active user example: " + str(exampleActiveUserThree))

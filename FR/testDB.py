import pymongo 
import base64
import gridfs

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = myclient["testDB"]
mycol = mydb["work"]
strr=[]
for i in range(6):
  s = "./"+str(i+1)+".jpg"
  with open(s, "rb") as imageFile:
       encoded_string = base64.b64encode(imageFile.read())
       strr.append(encoded_string)

exampleActiveUser = {
        "userID" : "0", #ID should be stored as a string
        "status" : True,
        "photos" : [
            strr[0],strr[1],strr[2],strr[3],strr[4]
        ]
    }
x = mycol.insert_one(exampleActiveUser)
# print("Active user example: " + str(exampleActiveUser))
exampleActiveUserTwo = {
    "userID" : "1", #ID should be stored as a string
    "status" : True,
    "photos" : [
      "./8.jpg", "./10.jpg","./12.jpg" 
    ]
}
x = mycol.insert_one(exampleActiveUserTwo)

# print("Active user example: " + str(exampleActiveUserTwo))
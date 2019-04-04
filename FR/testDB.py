import pymongo 
import base64
import gridfs

myclient = pymongo.MongoClient("mongodb://fr_dbAdmin:ZGEkMGEeTYg6fmyH@ds017155.mlab.com:17155/heroku_6lqvmjth")

mydb = myclient["heroku_6lqvmjth"]
mycol = mydb["DoNotUSE"]
strr=[]
for i in range(10):
  s = "./"+str(i+1)+".jpg"
  with open(s, "rb") as imageFile:
       encoded_string = base64.b64encode(imageFile.read())
       strr.append(encoded_string)

exampleActiveUser = {
        "userID" : "0", #ID should be stored as a string
        "status" : True,
        "photos" : [
            strr[0],strr[1],strr[2],strr[4],strr[7]
        ]
    }
x = mycol.insert_one(exampleActiveUser)
#print("Active user example: " + str(exampleActiveUser))
exampleActiveUserTwo = {
    "userID" : "1", #ID should be stored as a string
    "status" : True,
    "photos" : [
      strr[3],strr[5],strr[6]
    ]
}
y = mycol.insert_one(exampleActiveUserTwo)
exampleActiveUserThree = {
    "userID" : "2", #ID should be stored as a string
    "status" : True,
    "photos" : [
      strr[8],strr[9]
    ]
}
#z = mycol.insert_one(exampleActiveUserThree)
#print("Active user example: " + str(exampleActiveUserThree))
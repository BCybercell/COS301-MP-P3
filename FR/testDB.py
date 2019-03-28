import pymongo 

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

mydb = myclient["testDB"]
mycol = mydb["Clients"]

exampleActiveUser = {
    "userID" : "0", #ID should be stored as a string
    "status" : True,
    "photos" : [
      "./1.jpg", "./2.jpg","./6.jpg","./9.jpg","./15.jpg" 
    ]
}

x = mycol.insert_one(exampleActiveUser)
print("Active user example: " + str(exampleActiveUser))
exampleActiveUserTwo = {
    "userID" : "1", #ID should be stored as a string
    "status" : True,
    "photos" : [
      "./8.jpg", "./10.jpg","./12.jpg" 
    ]
}
x = mycol.insert_one(exampleActiveUserTwo)

print("Active user example: " + str(exampleActiveUserTwo))
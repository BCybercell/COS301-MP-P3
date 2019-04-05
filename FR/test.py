import face_recognition
import pymongo 
import base64
import numpy as np

myclient = pymongo.MongoClient("mongodb://fr_dbAdmin:ZGEkMGEeTYg6fmyH@ds017155.mlab.com:17155/heroku_6lqvmjth")
db = myclient["heroku_6lqvmjth"]
collection = db.secondRichard

allData = collection.find()
# results = []
# known_image = []
# #known_id = []
# counter =0
# #! This is the image we want to compare (imgToTest)
# unknown_image = face_recognition.load_image_file("test1.jpg")
# unknown_encoding = face_recognition.face_encodings(unknown_image,num_jitters=10)[0]
# print("Getting IMAGES from database:")
# for key in allData:
#     for img in key.get("photos"):
#         #Decode the base64 string
#             dec_img =base64.decodestring(img)
#             #create a name for the file. example userIDCounter.jpg thus 01.jpg
#             st = str(key.get("userID"))+str(counter)+".jpg"
#             counter = counter +1
#             #save the binary as an image to use
#             with open(st, 'wb') as f:
#                 f.write(dec_img)
#             #now append and let the magic happen
#             known_image.append(tuple((key.get("userID"),face_recognition.load_image_file("./"+st))))
#             print("IMG:"+ str(img))
#             counter = counter +1
#     #known_id.append(key.get("userID"))    

# def checking():
#     counter = 0
#     for i,j in known_image:
#         biden_encoding = face_recognition.face_encodings(j,num_jitters=10)[0]
#         results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))  
#         for e in results[counter]:
#             if e == True:
#                 print("The image matched and returned userID:"+ str(i))
#                 return
#         counter = counter +1
# checking()       
#Read images from database and compare till match or no images left
 #Contains every element in the database
# imageFromDb = []
results = []
imagetoTest = face_recognition.load_image_file("./test6.jpg") #Image they send us encoded
image_encoding = face_recognition.face_encodings(imagetoTest)[0]

def checking():
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
        
    return -1
checking()


# print("======= Testing Purposes =======")
# for i in results:
#     print(i)


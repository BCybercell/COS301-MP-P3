import face_recognition
import pymongo 
import base64

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = myclient["testDB"]
collection = db.work

allData = collection.find()
results = []
known_image = []
#known_id = []
#! This is the image we want to compare (imgToTest)
unknown_image = face_recognition.load_image_file("13.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image,num_jitters=10)[0]
print("Getting IMAGES from database:")
for key in allData:
    for img in key.get("photos"):
        dec_img =base64.decodestring(img)
        known_image.append(tuple((key.get("userID"),face_recognition.load_image_file(dec_img))))
        print("IMG:"+ str(dec_img))
    #known_id.append(key.get("userID"))    

def checking():
    counter = 0
    for i,j in known_image:
        biden_encoding = face_recognition.face_encodings(j,num_jitters=10)[0]
        results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))  
        for e in results[counter]:
            if e == True:
                print("The image matched and returned userID:"+ str(i))
                return
        counter = counter +1
checking()       

print("======= Testing Purposes =======")
for i in results:
    print(i)


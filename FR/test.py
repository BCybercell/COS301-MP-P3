import face_recognition
import pymongo 

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = myclient["testDB"]
collection = db.Clients

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
        known_image.append(tuple((key.get("userID"),face_recognition.load_image_file(img))))
        print("IMG:"+ str(img))
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
# known_image.append(face_recognition.load_image_file("1.jpg"))
# known_image.append(face_recognition.load_image_file("2.jpg"))
# known_image.append(face_recognition.load_image_file("6.jpg"))
# known_image.append(face_recognition.load_image_file("7.jpg"))
# known_image.append(face_recognition.load_image_file("8.jpg"))
# known_image.append(face_recognition.load_image_file("9.jpg"))
# known_image.append(face_recognition.load_image_file("12.jpg"))
# known_image.append(face_recognition.load_image_file("10.jpg"))
# known_image.append(face_recognition.load_image_file("13.jpg"))
# known_image.append(face_recognition.load_image_file("14.jpg"))
# known_image.append(face_recognition.load_image_file("15.jpg"))

# #! This is the image we want to compare (imgToTest)
# unknown_image = face_recognition.load_image_file("test1.jpg")
# unknown_encoding = face_recognition.face_encodings(unknown_image,num_jitters=10)[0]

# results =[]
# for i in known_image:
#     biden_encoding = face_recognition.face_encodings(i,num_jitters=10)[0]
#     results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
# biden_encoding = face_recognition.face_encodings(known_image[1])[0]
# results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
# biden_encoding = face_recognition.face_encodings(known_image[2])[0]
# results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
# biden_encoding = face_recognition.face_encodings(known_image[3])[0]
# results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
# biden_encoding = face_recognition.face_encodings(known_image[4])[0]
# results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
# biden_encoding = face_recognition.face_encodings(known_image[5])[0]
# results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
# biden_encoding = face_recognition.face_encodings(known_image[6])[0]
# results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
# biden_encoding = face_recognition.face_encodings(known_image[7])[0]
# results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
# biden_encoding = face_recognition.face_encodings(known_image[8])[0]
# results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
# biden_encoding = face_recognition.face_encodings(known_image[9])[0]
# results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
# biden_encoding = face_recognition.face_encodings(known_image[10])[0]
# results.append(face_recognition.compare_faces([biden_encoding], unknown_encoding, tolerance=0.6))
print("======= Testing Purposes =======")
for i in results:
    print(i)


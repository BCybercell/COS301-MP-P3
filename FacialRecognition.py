import time as time
import random as Rand
import json as json

#  TODO Richard
def AuthenticateUser(aArrImg):




# TODO Kyle
def AuthenticateImage(aImg):



# TODO Tegan
def Log(aUserID, aStart, aEnd, aStatus):



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
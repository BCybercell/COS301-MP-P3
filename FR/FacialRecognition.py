import time as time
import random as Rand
import json as json

#  TODO Richard
def AuthenticateUser(aArrImg):
    a=1



# TODO Kyle
def AuthenticateImage(aImg):
    a = 1


# TODO Tegan
def Log(aUserID, aStart, aEnd, aStatus):
    a = 1


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
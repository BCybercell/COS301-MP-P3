import json as json

# TODO Tegan
def Log(aUserID, aStart, aEnd, aStatus):
    lLog = {
                "ID": aUserID,
                "Start" : aStart,
                "End" : aEnd,
                "Status" : aStatus
            }

    with open('log.json', 'a') as f: # TODO Fix json format when appened to the file
        json.dump(lLog, f)


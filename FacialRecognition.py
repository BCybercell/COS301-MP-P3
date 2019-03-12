import json as json
import datetime as dt
from dateutil.parser import parse as parse_date


# TODO Tegan
def Log(aUserID, aStart, aEnd, aStatus):

    lDate = dt.datetime.now().isoformat()

    lLog = {}
    lLog['logs'] = []
    lLog['logs'].append({
        "ID": aUserID,
        "Start": aStart,
        "End": aEnd,
        "Date": lDate,
        "Status": aStatus
    })

    with open('log.json', 'a') as f: # TODO Fix json format when appened to the file
        json.dump(lLog,f)

def getLog(aStart,aEnd):
    with open('log.json') as f:
        lReturnLog = json.load(f)
    for p in lReturnLog['logs']:
        dt = parse_date(p['Date'])
        if dt >= aStart and dt <= aEnd:

            # TODO Return in a format that Reporting sub-system needs
            print('UserID: ' + p['ID'])
            print('Start Time: ' + str(p['Start']))
            print('End Time: ' + str(p['End']))
            print('Date: ' + p['Date'])
            print('Status: ' + str(p['Status']))
            print('')


#Log(str(12345),13,14,True)
#lDate1 = dt.datetime(2019, 03, 12, 18, 00, 00)
#lDate2 = dt.datetime(2019, 03, 12, 18, 39, 00)
#getLog(lDate1,lDate2)

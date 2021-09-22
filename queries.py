from threading import current_thread
from app import db
from dbTables import Users
from dbTables import busySlots

currentUser = ""
def addUser(userNameList, userPassword):
    #print(type(userNameList))
    userName = ' '.join(userNameList)
    print(userName)
    userObject = Users(name = userName, password = userPassword)
    try:
        db.session.add(userObject)
        db.session.commit()
        #print("here")
        return 1
    except:
        print("couldn't add to database a user")
        return 0

def addBusySlot( slot):
    
    slotObject = busySlots(name = currentUser, busySlot= slot)
    try:
        db.session.add(slotObject)
        db.session.commit()
        #print("here")
        return 1
    except:
        print("couldn't add to database a slot")
        return 0


def verifyCred(userNameList, userPassword):
    print("hna")
    userName = ' '.join(userNameList)
    #no such user
    obj = Users.query.get(userName)
    if obj == None:
        return 0
    #correct password
    elif obj.password == userPassword:
        global currentUser
        currentUser = userName
        return 1
    #wrong password
    else:
        return -1

def printUsersTable():
    users = Users.query.all()
    for i in users:
        print("name: "+i.name+"    password: "+i.password)

def printBusySlotsTable():
    busy = busySlots.query.all()
    for i in busy:
        print("name: "+i.name+"    busySlot: "+i.busySlot)

def deleteUserSlots():
    busySlots.query.filter(busySlots.name == currentUser).delete()
    db.session.commit()

def getFreeUsers(day, hour):
    printUsersTable()
    dayDict = {"sunday": 0, "monday": 1, "tuesday": 2, "wednesday": 3, "tursday": 4,
                    "friday": 5, "saturday": 6}
    day = str.lower(day)
    colNum = (int(hour) + 18) % 24
    targetNum = int(dayDict[day])*24 + colNum
    print("targetSlot")
    print(targetNum)
    users = Users.query.all()
    names = ""
    for i in users:
        print(i.name)
        slots = busySlots.query.filter(busySlots.name == i.name)
        flag = True
        for ii in slots:
            if ii.busySlot == str(targetNum):
                flag = False
        if flag:
            names += i.name + "-"
        print(names)
    return names


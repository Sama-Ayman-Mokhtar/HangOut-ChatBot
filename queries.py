from app import db
from dbTables import Users

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

def printUsersTable():
    users = Users.query.all()
    for i in users:
        print("id: "+str(i.id)+"    name: "+i.name+"    password: "+i.password)
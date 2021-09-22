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


def verifyCred(userNameList, userPassword):
    print("hna")
    userName = ' '.join(userNameList)
    #no such user
    obj = Users.query.get(userName)
    if obj == None:
        return 0
    #correct password
    elif obj.password == userPassword:
        return 1
    #wrong password
    else:
        return -1
    
def printUsersTable():
    users = Users.query.all()
    for i in users:
        print("name: "+i.name+"    password: "+i.password)
    #print(getPass("sama"))
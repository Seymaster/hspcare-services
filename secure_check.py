from testdb import User

users = [User(1,"Oluwaseyi","secret"),
        User(2, "Folake", "moyo") ]

username_table = {u.username: u for u in users}
userid_table   = {u.id: u for u in users}

def authenticate(username,password):
    #check if user exists and return user
    user = username_table.get(username,None)
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id,None)

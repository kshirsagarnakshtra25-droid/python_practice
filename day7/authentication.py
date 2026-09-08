users = {}


def register_user(username, password):

    if username in users:
        print("User already exists")

    else:
        users[username] = password
        print("Registration successful")


def login_user(username, password):

    if username in users and users[username] == password:
        print("Login successful")

    else:
        print("Invalid username or password")
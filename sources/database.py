import datetime


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            username, password, name, created = line.strip().split(";")
            self.users[username] = (password, name, created)

        self.file.close()

    def get_user(self, username):
        if username.text in self.users:
            return self.users[username.text]
        else:
            return -1

    def add_user(self, username, password, name):
        if username.text.strip() not in self.users:
            self.users[username.text.strip()] = (password.text.strip(), name.text.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            return -1

    def validate(self, username, password):
        if self.get_user(username) != -1:
            if self.users[username.text][0] == password.text:
                return True
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
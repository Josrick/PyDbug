
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
            schid, password, nickname, created = line.strip().split(";")
            self.users[schid] = (password, nickname, created)

        self.file.close()

    def get_user(self, schid):
        if schid in self.users:
            return self.users[schid]
        else:
            return -1

    def add_user(self, schid, password, nickname):
        if schid.strip() not in self.users:
            self.users[schid.strip()] = (password.strip(), nickname.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Account  already exist")
            return -1

    def validate(self, schid, password):
        if self.get_user(schid) != -1:
            return self.users[schid][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
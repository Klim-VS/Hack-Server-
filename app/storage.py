class UserStore:
    def __init__(self):
        self.users = dict()

    def add(self, name, password):
        self.users.update({name: password})

    def get(self, name):
        return self.users.get(name)
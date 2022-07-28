class Employee:
    def __init__(self, id, email, firstName, lastName, avatar):
        self.id = id
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.avatar = avatar

    def getID(self):
        return self.id
    def getEmail(self):
        return self.email
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getAvatar(self):
        return self.avatar
class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None

    def set_user(self, user):
        self.user = user

    
    @classmethod
    def create_user(cls,user):
        connection = cls()
        connection.user = user
        return connection
    

c1 = Connection("malado")
print(c1.host)

c2 = Connection.create_user("gabriel")
print(c2.host)

c3 = Connection()
c3.set_user("dinossauro rei")
print(c3.user)
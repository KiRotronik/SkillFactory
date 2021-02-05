from t_1_10_3 import Client

class GuestsList(Client):
    def __init__(self, location, status):
        self.location = location
        self.status = status
    def client_info(self):
        return f"{self.name} {self.lastname}, г.{self.location}, статус {self.status}"


aber = GuestsList(nm = "Ваня", lmn = "Иванов")


print(aber.client_info())
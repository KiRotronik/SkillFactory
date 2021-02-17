from t_1_10_3 import Client, clients_list

class GuestsList(Client):
    def __init__(self, nm, lnm, bal, location, status):
        # import Client attributes
        super().__init__(nm, lnm, bal)
        self.location = location
        self.status = status
    def add_guest(self):
        guests_list.append({"name": self.name, "lastname": self.lastname, "location": self.location, "status": self.status})


guests_list = []
person = GuestsList(nm="Ваня", lnm="Иванов", bal="", location="г. Москва", status="Наставник", )
person.add_guest()


for guest in guests_list:
    print(
        guest.get("name"),
        guest.get("lastname"),
        guest.get("location"),
        "статус " + guest.get("status"))

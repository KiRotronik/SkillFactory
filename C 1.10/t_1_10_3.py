class Client:
    def __init__(self, nm, lnm, bal):
        self.name = nm
        self.lastname = lnm
        self.balance = bal
    def client_info(self):
        return f"Клиент «{self.name} {self.lastname}». Баланс: {self.balance} руб."

clients = [
    {
     "name": "Иван",
     "lastname": "Петров",
     "balance": 100
    },
    {
     "name": "Олег",
     "lastname": "Иванов",
     "balance": 500
    },
    {
     "name": "Петр",
     "lastname": "Сидоров",
     "balance": 233
    }
]


for one in clients:
    person = Client(nm = one.get("name"),
                    lnm = one.get("lastname"),
                    bal = one.get("balance"))
    print(person.client_info())



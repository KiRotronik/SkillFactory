class Client:
    def __init__(self, nm, bal):
        self.name = nm
        self.balance = bal
    def client_info(self):
        return f"Клиент «{self.name}». Баланс: {self.balance} руб."

clients = [
    {
     "name": "Иван Петров",
     "balance": 100
    },
    {
     "name": "Василий Иванов",
     "balance": 122
    },
    {
     "name": "Петр Сидоров",
     "balance": 500
    }
]


for one in clients:
    person = Client(nm = one.get("name"),
                    bal = one.get("balance"))
    print(person.client_info())



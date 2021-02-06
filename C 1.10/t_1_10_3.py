class Client:
    def __init__(self, nm, lnm, bal):
        self.name = nm
        self.lastname = lnm
        self.balance = bal
    def client_info(self):
        return f"Клиент «{self.name} {self.lastname}». Баланс: {self.balance} руб."

clients_list = [
    {
     "name": "Иван",
     "lastname": "Петров",
     "balance": 100,
     "location": "Москва",
     "status": "Наставник"
    },
    {
     "name": "Олег",
     "lastname": "Иванов",
     "balance": 500,
     "location": "Спб",
     "status""status": "Волонтер"
    },
    {
     "name": "Петр",
     "lastname": "Сидоров",
     "balance": 233,
     "location": "Спб",
     "status": "Волонтер"
    }
]

if __name__ == "__main__":
    for one in clients_list:
        person = Client(nm = one.get("name"),
                    lnm = one.get("lastname"),
                    bal = one.get("balance"))
        print(person.client_info())




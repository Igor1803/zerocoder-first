class Account:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет на {money} руб. Сумма на счете - {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Недостаточно средств на счёте")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счете: {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")


# Создаем объект класса Account
man = Account("12323132", 600)


man.all_balance()

man.withdraw(500)
man.all_balance()

man.deposit(300)
man.all_balance()
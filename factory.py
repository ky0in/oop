from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PaymentProcessor:
    def pay(self, payment_type, amount):
        if payment_type == "card":
        print(f"Zaplceno kartou: {amount} Kč")
        elif payment_type == "paypal":
            print(f"Zaplceno přes PayPal: {amount} Kč")
        elif payment_type == "bank":
            print(f"Zaplceno bankovním převodem: {amount} Kč")

def payment_factory(payment_type):


class PaymentProcessor:
    def pay(self, payment_type, amount):
        obj - payment_factory.pay()

if __name__ == "__main__":
    processor = PaymentProcessor()
    processor.pay("card", 100)
    processor.pay("paypal", 200)
    processor.pay("bank", 300)
from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class StripPayment(PaymentProvider):
    def process_payment(self, amount):
        print("Strip payment done !: ", amount)

class PaypalPayment(PaymentProvider):
    def process_payment(self, amount):
        print("Strip payment done !: ", amount)

class PayoneerPayment(PaymentProvider):
    def process_payment(self, amount):
        print("Strip payment done !: ", amount)

class PaymentContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def checkout(self, amount):
        self._strategy.process_payment(amount)

client = PaymentContext(strategy=StripPayment())
client.checkout(100)

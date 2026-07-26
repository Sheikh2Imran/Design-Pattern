class AuthService:
    def authentication(self, username, password):
        print("Authenticating user: ", username)
        return True

class PaymentService:
    def process_payment(self, amount):
        print("Processing payment of ", amount)
        return True


class NotificationService:
    def send_receipt(self, user, amount):
        print("Sending receipt to {} for ${}", user, amount)

# facade 
class EcommerceFacade:
    def __init__(self):
        self.auth = AuthService()
        self.payment = PaymentService()
        self.notify = NotificationService()

    def checkout(self, username, password, amount):
        if self.auth.authentication(username, password):
            if self.payment.process_payment(amount):
                self.notify.send_receipt(username, amount)
                print("Checkout Successful !")
            else:
                print("Payment Failed")
        else:
            print("Authentication Failed")


store = EcommerceFacade()
store.checkout('imran', '1234', 10)

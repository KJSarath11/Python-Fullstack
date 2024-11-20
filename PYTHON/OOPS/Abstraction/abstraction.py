from abc import ABC, abstractmethod

# Abstract class representing the concept of Payment
class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        """Process the payment of a given amount"""
        pass

# Subclass for Credit Card Payment
class CreditCardPayment(Payment):
    
    def __init__(self, card_number, card_holder, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv

    def pay(self, amount):
        # Specific implementation for credit card payment
        print(f"Processing credit card payment of ${amount} for {self.card_holder} using card {self.card_number}.")

# Subclass for PayPal Payment
class PayPalPayment(Payment):
    
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        # Specific implementation for PayPal payment
        print(f"Processing PayPal payment of ${amount} for account {self.email}.")

# Subclass for Bank Transfer Payment
class BankTransferPayment(Payment):
    
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder

    def pay(self, amount):
        # Specific implementation for bank transfer payment
        print(f"Processing bank transfer of ${amount} for {self.account_holder} using account {self.account_number}.")


# Client code that works with the abstraction
def make_payment(payment_method, amount):
    # payment_method can be any subclass of Payment
    payment_method.pay(amount)

# Instantiate payment methods
credit_card = CreditCardPayment("1234-5678-9012-3456", "John Doe", "123")
paypal = PayPalPayment("johndoe@example.com")
bank_transfer = BankTransferPayment("9876543210", "John Doe")

# Making payments using different payment methods
make_payment(credit_card, 100)  # Output: Processing credit card payment of $100
make_payment(paypal, 200)       # Output: Processing PayPal payment of $200
make_payment(bank_transfer, 300) # Output: Processing bank transfer of $300

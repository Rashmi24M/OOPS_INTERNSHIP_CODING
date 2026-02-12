#Method overriding 
class Payment:
    def pay(self):
        print("Payment made using Payment class")
        
        
class GooglePay(Payment):
    def pay(self):
        print("Payment made using Google Pay")
class PhonePe(Payment):
    def pay(self):
        print("Payment made using PhonePe") 
class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")
obj1=Payment()
obj2=GooglePay()
obj3=PhonePe()
obj4=CreditCard()
obj1.pay()
obj2.pay()
obj3.pay()
obj4.pay()
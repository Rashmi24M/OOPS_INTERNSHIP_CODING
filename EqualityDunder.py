class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def __eq__(self,other):
        if isinstance(other,Mobile):
            return self.brand == other.brand and self.model == other.model and self.price == other.price
        return False
mobile1=Mobile("Apple","iPhone 13",999)
mobile2=Mobile("Apple","iPhone 13",999) 
mobile3=Mobile("Samsung","Galaxy S21",799)
print(mobile1 == mobile2)  # Output: True
print(mobile1 == mobile3)  # Output: False
print(mobile1 == mobile2 and mobile2 == mobile3)  # Output: False

class ShoppingCart:
    def __init__(self):
        self.items = []
    def __getitem__(self,index):
        return self.items[index]
    def __setitem__(self,index,value):
        self.items[index] = value
cart=ShoppingCart()
cart.items.append("Apple")   
cart.items.append("Banana")
print(cart[0]) 
cart[1]="New Item"
print(cart.items) 
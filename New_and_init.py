class User:
    def __new__(cls,name):
        print(f"Object is being created: {name}") #First object is created then initialized
        instance=super().__new__(cls)
       
        return instance
    def __init__(self,name):
        print("Object is initialized")   
        self.name = name 
       
    
u=User("Alice")

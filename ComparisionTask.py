class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __gt__(self,salary):
        return self.salary>salary.salary
    def __lt__(self,salary):
        return self.salary<salary.salary
e1=Employee("Alice",50000)
e2=Employee("Bob",60000)
print(e1>e2)
print(e1<e2)
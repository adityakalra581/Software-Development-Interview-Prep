class employee:
    def put_data(self):
        self.id = int(input("Enter employee id:"))
        self.name = input("Enter employee name:")
    
    def direct_data(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print("Employee id:",self.id)
        print("Employee name:",self.name)


a = employee()
# a.put_data()
a.direct_data(1,'Aditya')
a.display()
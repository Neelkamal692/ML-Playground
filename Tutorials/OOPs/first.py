class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "Software Engineer"
        print("I want to see if constructor is called as soon as object is created")

    def travel(self, destination):
        return f"Employee is traveling to {destination}"
# creating an object of the class employee
sam = employee()

print(sam.id)
print(sam.salary)
print(sam.designation)
print(sam.travel("New York"))
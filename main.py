class Person:

    def __int__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

class employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)
    def show(self):

        print(self.salary)
        print(self.post)
e1=employee("Hayyan", 1, 500000, "CEO")
e1.show()
e1.display()
    
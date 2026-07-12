class Employee:
    company = "Google"
    def show(self):
        print(f"The company name is {self.company}")
        print(f"Employee name is {self.name}")
        print(f"salary of employee is {self.salary}")

class Coder:
  language = "Python"
  def print_language(self):
      print(f"out of all the language here is your language: {self.language}")



class Programmer(Employee, Coder):
    company = "Google"
    def show_language(self):
        print(f"{self.name}is good at {self.language}")


b= Programmer()

b.name = "Rajat"
b.salary = 50000
b.language = "Python"


b.show()
b.print_language()
b.show_language()


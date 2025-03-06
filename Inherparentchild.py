class Person:
  def __init__(self, fname, lname):
      print(fname,lname)

class Student(Person):
      def __init__(self, fname, lname, year):
          super().__init__(fname, lname)
          print("Welcome", fname, lname, "to the class of", year)

x = Student("Mike", "Olsen",2024)
#x.welcome()

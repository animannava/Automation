from Parentclass import Person1


class Student1(Person1):
    def __int__(self, fname, lname, year):
        super().__init__(fname, lname)
        print("Welcome ", fname, lname, "year of", year)


s1 = Student1('Anitha', 'Mannava', 2006)

#s1.printname()

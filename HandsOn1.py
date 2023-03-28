class Person:
    def __init__(self, std, pre, mid, fin):
        self.__std = std
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin
    def grade(self):
        print("   Average grade is: ", round((self.__pre + self.__mid + self.__fin) / 3, 2))
        print()
    def display(self):
        print(self.__std)
        print("   Prelims grade is: ", self.__pre)
        print("   Midterms grade is: ", self.__mid)
        print("   Finals grade is: ", self.__fin)
class std1(Person):
    pass
class std2(Person):
    pass
class std3(Person):
    pass

Student1 = std1("Jarren Ramos", 94, 93, 90)
Student1.display()
Student1.grade()
Student2 = std2("Leigh Ramos", 88, 80, 90)
Student2.display()
Student2.grade()
Student3 = std3("C. Ramos", 94, 88, 89)
Student3.display()
Student3.grade()

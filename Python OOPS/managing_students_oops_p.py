class students:
    def __init__(self,name,age,rollnumber):
        self.__name = name
        self.__age = age
        self.__rollnumber = rollnumber

    def getname(self):
        return self.__name
    
    def getage(self):
        return self.__age
    
    def getrollnumber(self):
        return self.__rollnumber
    
    def setname(self,new_name):
        self.__name = new_name 

    def setage(self, new_age):
        self.__age = new_age

    def setrollnumber(self,new_rollnumber):
        self.__rollnumber = new_rollnumber

    def display_student_info(self):
        print(f"Name:{self.__name}")
        print(f"age:{self.__age}")
        print(f"roll_number:{self.__rollnumber}")

    def update_student_info(self,new_name,new_age,new_rollnumber):
        self.setname(new_name)
        self.setage(new_age)
        self.setrollnumber(new_rollnumber)

print("/n previous students info")
students1 = students("Harsh",29,99) 
students1.display_student_info()

print("/n updating student info")
students1.update_student_info("Sharma", 24, 10)
students1.display_student_info()
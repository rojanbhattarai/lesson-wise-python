class Employee:
    name="handsome"
    language="py"
    salary=100000
    
    def getinfo(self):
        print("the language is:",self.language)
    @staticmethod
    def greet():
        print("hello")


harry=Employee()
harry.language="javascript"
harry.greet()
harry.getinfo()

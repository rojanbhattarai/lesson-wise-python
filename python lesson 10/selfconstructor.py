class Employee:
    
    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary

    
    def getinfo(self):
        print("the language is:",self.language)
    @staticmethod
    def greet():
        print("hello")


harry=Employee("harry","javascript","salary")

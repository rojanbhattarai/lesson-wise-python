class PROGRAMMER:
    company="microsoft"

    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary

    def getinfo(self):
        print("the info of the personnel is:",self.name,self.language,self.salary,self.company )
    

harry=PROGRAMMER("harry","python",200000)
rojan=PROGRAMMER("rojan","R",500000)
rahul=PROGRAMMER("rahul","java",300000)
harry.getinfo()
rojan.getinfo()
rahul.getinfo()

 
 

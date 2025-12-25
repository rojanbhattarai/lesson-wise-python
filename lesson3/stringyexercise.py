# problem1
a=input("enter a name")
print("goodmorning",a)
print(f"goodmorning {a}")
# problem2
letter = ''' Dear <name>
 you are selected
  <date>'''
print(letter.replace("<name>",a).replace("<date","2082/02/08"))
# problem3
print(a.find("r"))
# strings are immutable that means it doesnot change its original value
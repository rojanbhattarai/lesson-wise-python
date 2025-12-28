student=["hari",35,320.3,False]
print(student[3])
# we can write student[0]='ram' because string are immutable but lists are not
student[3]="ram"
print(student[3])
student.append("hari")
print(student)
friends=["ram","shyam",0]
friends[2]="hari"
print(friends[2])
#unlike strings lists are mutable and can be assigned with values
friends.append("hancy")
friends.remove("hari")
print(friends)
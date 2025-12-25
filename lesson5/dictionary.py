# dictionary in python programing
# dictionary are mutable
marks={
    "rojan": 100,
    "shivam": 22,
    "rohan":23
}
print(marks["rojan"])
print(marks.items())
marks.update({"rojan": 99}) #includes if not present as well 
print(marks.items())
print(marks.get("rojan")) #if not present this will give none but if we use line number 8 then it will give error

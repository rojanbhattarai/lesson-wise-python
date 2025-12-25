p1="spam"
p2="error"
p3="subscribe"
message=input("enter your message")
if(p1 in message or p2 in message or p3 in message):
    print("this is a spam message")

else:
    print("thank you for the message")    
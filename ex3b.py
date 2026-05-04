phone={}
n=int(input("enter the number of contacts:"))
for i in range(n):
    number=input("enter mobile number:")
    name=input("enter name:")
    phone[number]=name
search=input("enter mobile number to search:")
if search in phone:
    print("person name:",phone[search])
else:
    print("number not found")
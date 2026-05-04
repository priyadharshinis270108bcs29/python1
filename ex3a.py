phone={}
n=int(input("enter the number of contacts"))
for i in range(n):
    name=input("enter name:")
    number=int(input("enter the mobile number:"))
    phone[number]=name
print(phone)
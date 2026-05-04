employees=((101,"ravi",45000),(102,"sita",60000),(103,"arun",75000),(104,"meena",50000))
print("employee details:")
for emp in employees:
    print(emp)
search_id =int(input("enter employee id to search:"))
Found=1
for emp in employees:
    if emp[0]==search_id:
       print("employee found:",emp)
       Found=0
    else:
       print("employee not found")
       highest=employees[0]
for emp in employees:
    if emp[2]>highest[2]:
       highest=emp
print("\n employee with highest salary:",highest)
print("\n employee with salary of 50000")
for emp in employees:
    if emp[2]>50000:
       print(emp)

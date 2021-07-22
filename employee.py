n=int(input("Enter the number of employee:"))
employeelist=[]
for i in range(n):
    id=int(input("enter the id:"))
    name=input("enter the name:")
    mail=input("enter the mail:")
    age=int(input("enter the age:"))
    dept=input("enter the dept:")
    salary=input("enter the salary:")
    emp={"id":id,"name":name,"mail":mail,"age":age,"dept":
    dept,"Salary":salary}
    employeelist.append(emp)
print(employeelist)
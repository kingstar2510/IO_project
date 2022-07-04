class Clerk:
    def create(self):
        f=open("Clerk.txt","x")
        a=open("Clerk.txt","a")
        uid=input("enter ID:")
        name=input("enter name:")
        age=input("enter age:")
        salary=input("enter salary:")
        designation="Clerk"
        space="   "
        a.write(uid)
        a.write(space)
        a.write(name)
        a.write(space)
        a.write(age)
        a.write(space)
        a.write(salary)
        a.write(space)
        a.write(designation)
        a.close()
    def display(self):
        readdata=open("Clerk.txt","r")
        print(readdata.read())

        
    def options(self):
        print("..........................................")
        print("Choose the below Option number to perform the certain task");
        print("1.Create")
        print("2.Display")
        print("3.exit")

class Manager:
    def create(self):
        f=open("Manager.txt","x")
        a=open("Manager.txt","a")
        uid=input("enter ID:")
        name=input("enter name:")
        age=input("enter age:")
        salary=input("enter salary:")
        designation="Manager"
        space="   "
        a.write(uid)
        a.write(space)
        a.write(name)
        a.write(space)
        a.write(age)
        a.write(space)
        a.write(salary)
        a.write(space)
        a.write(designation)
        a.close()
    def display(self):
        readdata=open("Manager.txt","r")
        print(readdata.read())

class Tester:
    def create(self):
        f=open("Tester.txt","x")
        a=open("Tester.txt","a")
        uid=input("enter ID:")
        name=input("enter name:")
        age=input("enter age:")
        salary=input("enter salary:")
        designation="Tester"
        space="   "
        a.write(uid)
        a.write(space)
        a.write(name)
        a.write(space)
        a.write(age)
        a.write(space)
        a.write(salary)
        a.write(space)
        a.write(designation)
        a.close()
    def display(self):
        readdata=open("Tester.txt","r")
        print(readdata.read())
class Developer:
    def create(self):
        f=open("Developer.txt","x")
        a=open("Developer.txt","a")
        uid=input("enter ID:")
        name=input("enter name:")
        age=input("enter age:")
        salary=input("enter salary:")
        designation="Developer"
        space="   "
        a.write(uid)
        a.write(space)
        a.write(name)
        a.write(space)
        a.write(age)
        a.write(space)
        a.write(salary)
        a.write(space)
        a.write(designation)
        a.close()
    def display(self):
        readdata=open("Developer.txt","r")
        print(readdata.read())
c=Clerk();
m=Manager();
t=Tester();
d=Developer();
counter=0;
print("Choose the below Option number to perform the certain task");
print("1.Create");
print("2.Display");
print("3.exit");

while True:
    counter+=1;
    n=int(input("enter your choice number:"));
    if(n==1):
        print("1.Clerk");
        print("2.Manager");
        print("3.Tester");
        print("4.Developer");
        n1=int(input("choose the option number to create:"));
        if(n1==1):
            print("enter the clerk details")
            c.create();
            c.options()
            
            
        elif(n1==2):
            print("enter the Manager details")
            m.create();
            c.options()
            
           
        elif(n1==3):
            print("enter the Tester details")
            t.create();
            c.options()
            
        elif(n1==4):
            print("enter the Developer details")
            d.create();
            c.options()
            
            
        else:
            print("wrong selection......:(");
            
        
    if(n==2):
        print("1.Clerk");
        print("2.Manager");
        print("3.Tester");
        print("4.developer");
        n2=int(input("choose the option number to display:"));
        if(n2==1):
            print("clerk details")
            c.display();
        elif(n2==2):
            print("Manager details")
            m.display();
        elif(n2==3):
            print("Tester details")
            t.display();
        elif(n2==4):
            print("developer details")
            d.display();
        else:
            print("wrong option")
        c.options()
        
        
    if(n==3):
        print("thank you.....:)");
        break
    
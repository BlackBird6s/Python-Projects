                               # Customer Management System
# BLL: Business Logic Layer
class customer:
    cus_list=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
        self.state=0
        self.city=0
    def addcustomer(self):
        customer.cus_list.append(self)

    def searchcustomer(self):
        for e in customer.cus_list:
            if(e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.state=e.state
                self.city=e.city
                return
    def deletecustomer(self):
        customer.cus_list.pop()
        for e in customer.cus_list:
           if(e.id==self.id):
            e.name=0
            e.age=0
            e.mob=0
            e.state=0
            e.city=0
            return

    def modifycustomer(self):
        for e in customer.cus_list:
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                e.state=self.state
                e.city=self.city
                return

# PL: Presentation Layer

print("welcome to CRM ")
def showcustomer(cus):
    print("CUST ID:",cus.id,"CUST NAME:",cus.name,"CUST AGE:",cus.age,"CUST MOB:",cus.mob,"CUST STATE:",cus.state,"CUST CITY",cus.city)
while(1):
    ch=input("Enter the choice: 1 ADD, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
    if(ch=="1"):
        cus=customer()
        cus.id=input("Enter the cust id:")
        cus.name=input("Enter the cust name:")
        cus.age=input("Enter the cust age:")
        cus.mob=input("Enter the cust mob:")
        cus.state=input("Enter the cust state:")
        cus.city=input("Enter the cust city:")
        cus.addcustomer()
    elif(ch=="2"):
        cus=customer()
        cus.id=input("Enter the cust ID:")
        cus.searchcustomer()
        showcustomer(cus)
    elif(ch=="3"):
        cus=customer()
        cus.id=("Enter the cust id:")
        cus.deletecustomer()
        showcustomer(cus)
    elif(ch=="4"):
        cus=customer()
        cus.id=input("Enter the cust update ID:")
        cus.name=input("Enter the cust update NAME:")
        cus.age=input("Enter the cust update AGE:")
        cus.mob=input("Enter the cust update MOB:")
        cus.state=input("Enter the cust update STATE:")
        cus.city=input("Enter the cust update CITY:")
        cus.modifycustomer()
        showcustomer(cus)
    elif(ch=="5"):
        for i in customer.cus_list:
            showcustomer(i)
    elif(ch=="6"):
        print("Welcome for using CRM with OOPS")
        break
    else:
        print("invalid choice")


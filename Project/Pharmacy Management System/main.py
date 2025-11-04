from tabulate import tabulate
text = "PHARMACY MANAGEMENT SYSTEM"
data = [[text.center(50)]]  
print(tabulate(data, tablefmt="grid"))
from Admin import Admin
from userwork import Userwork
ch = 0
while ch != '3':
    print('''Please select the choice for logging:
    1. 👤 User
    2.  👨‍💼 Admin
    3. ❌ Exit ''')
    ch = input("Enter the chiose:")
    if ch == '1':
        Userwork()
    elif ch == '2':
        id = input("Enter the id 🆔:")
        passw = input("Enter the password 🔒:")
        with open("Pharmacy Management System/adData.txt","r") as fp:
            addata=fp.read()
            adlist = addata.strip("\n").split(", ")
            if(adlist[0] == id and adlist[1] == passw):
                text=(" 👨‍💼 Logging successfuly...")
                data = [[text.center(50)]]  
                print(tabulate(data, tablefmt="grid"))
                Admin()
            else:
                print(" ❌ Wrong userid and passworld....")
    elif ch == '3':
        print("********************* 🔓 logging out successfully *********************")
    else:
        print(" ❌ Invaild choice...Please select vaild chiose....")
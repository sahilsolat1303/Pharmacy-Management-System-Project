from Auserwork import Userwork
from medicinework import Medicinework
from order import Pharmacy
p=Pharmacy()

class Admin:
    def __init__(self):
        ch = 0
        while ch != '4':
            print('''Please select the below option:  
            1. 👤 User
            2. 💊 Medicine
            3. 📦 History
            4. ❌ Exit''')

            ch = input("Enter the choise:")
            if ch == '1':
                Userwork()
            elif ch == '2':
                Medicinework()
            elif ch == '3':
                p.view_orders()
            elif ch == '4':
                print("******************** 🔓Logging out successfuly********************")
            else:
                print("❌ Invaild choise....")

if __name__ == '__main__':
    a1 = Admin()      
      
   
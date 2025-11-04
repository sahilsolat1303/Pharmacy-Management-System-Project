from userregistraction import Regi 
r = Regi()
from userlogin import Userlogin
u=Userlogin()
class Userwork:
    def __init__(self):
        ch = 0
        while ch != '3':
            print('''User Registration and Login:
            1. 📝 User Registration
            2. 🔑 Login 
            3. ❌ Exit''')
            ch = input("Enter the choice:")
            if ch == '1':
                r.registration()
            elif ch == '2':
                u.userloging()
            elif ch == '3':
                print("******************** 🙏Thanku for wesite the website..!********************")
            else:
                print("❌ Invalid choice....")


if __name__ == '__main__':

    u1 = Userwork()

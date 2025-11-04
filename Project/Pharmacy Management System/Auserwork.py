from Ausermange import Usermanage
u1 = Usermanage()
class Userwork:
    def __init__(self):
        ch = 0
        while ch != '6':
            print('''Please select the below option:  
            1. ➕ Add user
            2. ✏️ Update user
            3. 🗑️ Delete user
            4. 👥 Show all user
            5. 🔍 Search user
            6. ❌ Exit''')

            ch = input("Enter the choise:")
            if ch == '1':
              u1.adduser()

            elif ch == '2':
                u1.Updateuser()

            elif ch == '3':
                u1.Deleteuser()

            elif ch == '4':
                u1.Showalluser()

            elif ch == '5':
                u1.Searchuser()

            elif ch == '6':
                print("******************** Exits successfuly ********************")
            else:
                print("❌ Invaild choise....")

if __name__ == '__main__':
    a1 = Userwork()      
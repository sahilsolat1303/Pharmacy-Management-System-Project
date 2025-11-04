from medicinemange import Medicinemanage
m1 = Medicinemanage()
class Medicinework:
    def __init__(self):
        ch = 0
        while ch != '6':
            print('''Please select the below option:  
                  1. ➕ Add Medicine
                  2. ✏️ Update Medicine
                  3. 🗑️ Delete Medicine
                  4. 👥 Show all Medicine
                  5. 🔍 Search Medicine
                  6. ❌ Exit''')
            

            ch = input("Enter the choise:")
            if ch == '1':
                m1.addmedicine()

            elif ch == '2':
                m1.Updatemedicine()

            elif ch == '3':
                m1.delete()

            elif ch == '4':
                m1.Showallmedicine()

            elif ch == '5':
                m1.Searchmedicine()

            elif ch == '6':
                print("******************* Exits successfuly ********************")
            else:
                print("Invaild choise....")

if __name__ == '__main__':
    a1 = Medicinework()      
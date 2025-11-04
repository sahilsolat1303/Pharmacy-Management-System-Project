from order import Pharmacy
p=Pharmacy()
import globals
class Userorder:
    def __init__(self):
        ch = 0
        while ch != '4':
            print('''Oreder the Medicine...:
            1. Order
            2. Delete
            3. History
            4. Exit ''')
            ch = input("Enter the chiose:")
            if ch == '1':
                p.show_medicines()
                p.order_medicine()
            elif ch == '2':
                p.delete_order()
            elif ch == '3':
                p.show_my_orders()
            elif ch == '4':
                print("********************* 🙏Thanku for visting website ********************")
            else:
                print("✅Invaild choise..Please select vaild choise..!")



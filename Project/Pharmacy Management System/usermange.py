class Usermanage:
    def __init__(self):
        self.medicine = {}

    def load(self):
        with open("Pharmacy Management System/medicineData.txt",'r') as fp:
            for record in fp:
                parts = record.strip().split(", ")
                if len(parts) == 2:
                    name,price = parts
                    self.medicine[name.lower()] = int(price)
   
    
    def show(self):
        print("\n----Medicine Name & Price----")
        for name, price in self.medicine.items():
            print(f"{name.title()} - ${price}")





e1 = Usermanage()
e1.load()
e1.show()
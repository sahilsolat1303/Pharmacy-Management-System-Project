from tabulate import tabulate
from medicine import Medicine
class Medicinemanage:
    def addmedicine(self):
        text = "ADD THE MEDICINE"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        try:
            m_id = input("Enter the new Medicine ID🆔:").strip()
            name = input("Enter the new Name💊:").strip()
            type= input("Enter the Type🧪:").strip()
            price= input("Enter the Price💰:").strip()
            if not price.isdigit() or int(price) <= 0:
                print("❌ Invalid price! Must be a positive number.")
                return
            price = int(price)
            quanitity= input("Enter the Quanitity📦:").strip()
            if not quanitity.isdigit() or int(quanitity) <= 0:
                print("❌ Invalid quantity! Must be a positive integer.")
                return
            quanitity = int(quanitity)
            id_exists=False
            try:
                with open("Pharmacy Management System/medicineData.txt", "r") as fp:
                    for line in fp:
                        existing_id = line.strip().split(", ")[0]  
                        if existing_id == m_id:
                            id_exists = True
                            break
            except FileNotFoundError:
                pass
            if id_exists:
                print(f"❌User ID '{m_id}' already exists. User not added.")
            else:
        
         
                m1 = Medicine(m_id, name, type, price, quanitity)
                MedicineData = str(m1)
                with open("Pharmacy Management System/medicineData.txt","a") as fp:
                    fp.write(MedicineData + '\n')
                    text = "Medicine Add successfuly."
                    data = [[text.center(50)]]  
                    print(tabulate(data, tablefmt="grid"))
                    

        except Exception as e:
            print("⚠️ Error adding user:", e)
            

    def Updatemedicine(self):
        text = "UPDATE THE MEDICINE"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        allmedicine = []
        m_id = input("Enter the id ot update:")
        idchek = False
        update = False
        try:
            with open("Pharmacy Management System/medicineData.txt","r") as fp:
                for record in fp:
                    mlist = record.split(", ")
                    if(mlist[0]== m_id):
                        idchek = True
                        chk = input("Do you wont to change the name(y/n):")
                        if chk.lower() in ['y','yes']:
                            mlist[1]=input("Enter the new name:")
                            update=True

                        chk = input("Do you wont to change the type(y/n):")
                        if chk.lower() in ['y','yes']:
                            mlist[2]=input("Enter the new type:")
                            update=True

                        chk = input("Do you wont to change the price(y/n):")
                        if chk.lower() in ['y','yes']:
                            mlist[3]=input("Enter the new Price:")
                            update=True

                        chk = input("Do you wont to change the quanitity(y/n):")
                        if chk.lower() in ['y','yes']:
                            mlist[4]=input("Enter the new Quanitity:")
                            update=True

                        if update:
                            record = ", ".join(mlist) + "\n"
                        allmedicine.append(record)
                    else:
                        allmedicine.append(record)
        except FileNotFoundError as e:
            print("⚠️Error: medicineData.txt file not found.")
        except Exception as e:
            print("⚠️Error:",e)
        else:
            if(idchek):
                with open("Pharmacy Management System/medicineData.txt","w") as fp:
                    for record in allmedicine:
                        fp.write(record)
                    
                text = "Data updated successfully."
                data = [[text.center(50)]]  
                print(tabulate(data, tablefmt="grid"))
                        
            else:
                print("❌ID not found...")                       

    
    def delete(self):
        text = "DELETE THE MEDICINE"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        med_id = input("Enter Medicine ID to delete: ").strip()
        found = False
        lines = []

        try:
            with open("Pharmacy Management System/medicineData.txt", "r") as f:
                for line in f:
                    if line.strip().split(",")[0] != med_id:
                        lines.append(line)
                    else:
                        found = True
        except FileNotFoundError:
            print("⚠️Error: medicineData.txt file not found.")
            return
        except Exception as e:
            print("⚠️Error reading file:", e)
            return
        
        try:
            with open("Pharmacy Management System/medicineData.txt", "w") as f:
                f.writelines(lines)
        except Exception as e:
            print("⚠️Error writing file:", e)
            return
        if found:
            text = "Medicine deleted."
            data = [[text.center(50)]]  
            print(tabulate(data, tablefmt="grid"))
            
        else:
            print("❌ Medicine not found.")

    
                            

  


    def Showallmedicine(self):
        text = "SHOW ALL MEDICINE"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        data = []
        try:
            with open("Pharmacy Management System/medicineData.txt", "r") as fp:
                for record in fp:
                    try:
                        m_id, name, type_, price, quanitity = record.strip().split(", ")
                        data.append([
                            m_id.strip(),
                            name.strip(),
                            type_.strip(),
                            int(price.strip()),
                            int(quanitity.strip())
                        ])
                    except ValueError:
                        print(f"❌Skipping invalid record: {record.strip()}")
        except FileNotFoundError:
            print(" ⚠️Error: medicineData.txt file not found.")
            return
        except Exception as e:
            print(" ⚠️Error reading file:", e)
            return 
        if data:          
            headers = ["ID", "Name", "Type", "Price", "Quantity"]

            print("-" * 80)
            print(tabulate(data, headers=headers, tablefmt="grid"))
            print("-" * 80)
        else:
            print("❌No medicine records found.")

    def Searchmedicine(self):
        text = "SEARCH THE MEDICINE"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        search_m_id = input("Enter the id to search: ")
        found = False
        try:
            with open("Pharmacy Management System/medicineData.txt", "r") as fp:
                for record in fp:
                    parth = record.strip().split(", ")
                    if parth[0].strip() == search_m_id:
                        headers = ["ID", "Name", "Type", "Price", "Quantity"]
                        table = [[parth[0], parth[1], parth[2], parth[3], parth[4]]]
                        print(tabulate(table, headers, tablefmt="grid"))
                        found = True
                        break
        except FileNotFoundError:
            print(" ⚠️Error: medicineData.txt file not found.")
        except Exception as e:
            print(" ⚠️Error searching medicine:", e)

        if not found:
            text = "Record not found."
            data = [[text.center(50)]]  
            print(tabulate(data, tablefmt="grid"))
                            



if __name__ == '__main__':
    e1 = Medicinemanage()
    e1.addmedicine()

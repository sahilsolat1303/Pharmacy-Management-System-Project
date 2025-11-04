from user import User
from tabulate import tabulate
class Usermanage:
    def adduser(self):
        text = "ADD THE USER"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        try:
            id = input("Enter the new ID 🆔:")
            name = input("Enter the new Name 👤:")
            add = input("Enter the Address 🏠:")
            id_exists= False
            try:
                with open("Pharmacy Management System/userData.txt", "r") as fp:
                    for line in fp:
                        existing_id = line.strip().split(", ")[0]  
                        if existing_id == id:
                            id_exists = True
                            break
            except FileNotFoundError:
                pass
            if id_exists:
                print(f"⚠️ User ID '{id}' already exists. User not added.")
            else:   
                u1 = User(id, name, add)
                userData = str(u1)
                with open("Pharmacy Management System/userData.txt","a") as fp:
                    fp.write(userData+'\n')
                    text = "User Add successfuly"
                    data = [[text.center(50)]]  
                    print(tabulate(data, tablefmt="grid"))
                    
        except Exception as e:
            print("⚠️ Error adding user:", e)


    def Updateuser(self):
        text = "UDATE THE USER"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        alluser = []
        id = input("Enter the id ot update:")
        idchek = False
        try:
            with open("Pharmacy Management System/userData.txt","r") as fp:
                for record in fp:
                    ulist = record.split(", ")
                    if(ulist[0]==id):
                        idchek = True
                        chk = input("Do you wont to change the name(y/n):")
                        if chk.lower() in ['y','yes']:
                            ulist[1]=input("Enter the new name:")
                        chk = input("Do you wont to change the address(y/n):")
                        if chk.lower() in ['y','yes']:
                            ulist[2]=input("Enter the new Address:")+'\n'

                        record = ", ".join(ulist)
                        alluser.append(record)
                    else:
                        alluser.append(record)
        except FileNotFoundError as e:
            print("⚠️ Error: userData.txt file not found.")
        except Exception as e:
            print("⚠️ Error:",e)
        else:
            if(idchek):
                with open("Pharmacy Management System/userData.txt","w") as fp:
                    for record in alluser:
                        fp.write(record)
                    else:
                        text = "Data updated successfully"
                        data = [[text.center(50)]]  
                        print(tabulate(data, tablefmt="grid"))
                       
            else:
                text = "ID not found..."
                data = [[text.center(50)]]  
                print(tabulate(data, tablefmt="grid"))
                                     

    def Deleteuser(self):
        text = "DELETE THE USER"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        id = input("Enter the id to delete:")
        alluser = []  
        idchkv=False
        try:
        
            with open("Pharmacy Management System/userData.txt","r") as fp:
                
                for record in fp:
                    ulist = record.split(", ")
                    if (ulist[0]!= id):
                        alluser.append(record)
                    else:
                        idchkv = True
        except FileNotFoundError:
            print("⚠️ Error: userData.txt file not found.")
            return
        except Exception as e:
            print("⚠️ Error while reading file:", e)
            return
        
        if(idchkv):
                try:
                    with open("Pharmacy Management System/userData.txt","w") as fp:
                        for record in alluser:
                            fp.write(record)
                    text = "User delete successfuly."
                    data = [[text.center(50)]]  
                    print(tabulate(data, tablefmt="grid"))
                                     
                except Exception as e:
                    print("⚠️ Error while deleting user:", e)
        else:
            print("⚠️ id can not change..")


    def Showalluser(self):
        text = "SHOW ALL THE USER"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        data = []
        try:
            with open("Pharmacy Management System/userData.txt", "r") as fp:
                for record in fp:
                    try:
                        id, name, add = record.strip().split(", ")
                        data.append([int(id.strip()), name.strip(), add.strip()])
                    except ValueError:
                        print(f"Skipping invalid record: {record.strip()}")
        except FileNotFoundError:
            print("⚠️ Error: userData.txt file not found.")  
            return
        except Exception as e:
            print("⚠️ Error while reading file:", e)
            return 
        if data:           
                print(tabulate(data, headers=["ID", "Name", "Address"], tablefmt="grid"))
        else:
            print("❌ No user records found.")

    
    def Searchuser(self):
        text = "SEARCH THE USER"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        search_id = input("Enter the id to search: ").strip()
        found = False
        try:
            with open("Pharmacy Management System/userData.txt","r") as fp:
                for record in fp:
                    parth = record.strip().split(", ")
                    if parth[0].strip() == search_id:
                        headers = ["ID", "Name", "Address"]
                        print(tabulate([parth], headers=headers, tablefmt="grid"))
                        found = True
                        break
        except FileNotFoundError:
            print("⚠️ File not found.")
        except Exception as e:
            print("⚠️ Error:", e)

        if not found:
            print("❌ Record not found.")



if __name__ == '__main__':
    e1 = Usermanage()
    e1.Showalluser()
    e1.adduser()
    

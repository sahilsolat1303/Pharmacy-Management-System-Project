from userorder import Userorder
import globals
from tabulate import tabulate
class Userlogin:
    def userloging(self):
                text = "USER LOGGING"
                data = [[text.center(50)]]  
                print(tabulate(data, tablefmt="grid"))
                try:
                    email = input("Enter the user email:").strip().lower()
                    passworld = input("Enter the Passworld:").strip()

                    found = False
                    with open("Pharmacy Management System/uData.txt","r") as fp:
                        for line in fp:
                            adlist = line.strip().split(", ")
                            if len(adlist) >= 6:
                                s_email = adlist[1].strip().lower()
                                s_pass = adlist[3].strip()
                                s_name = adlist[0].strip().lower()
                                globals.logged_in_user = s_name
                                
                                if(s_email== email and s_pass == passworld):
                                    
                                    
                                    print("******************** ✅Logging successfuly ********************")
                                    Userorder()
                                    
                                    
                                
                                    found = True
                                    
                                    break
                                
                                
                    if not found:
                        print("❌ Invalid username or password. Try again.")

                except FileNotFoundError:
                    print("❌ User data file not found. Please register first.")
                except Exception as e:
                    print("⚠️ Unexpected error during login:", e)  


if __name__ == '__main__':
    e1 = Userlogin()
    e1.userloging()

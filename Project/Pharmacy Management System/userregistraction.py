from tabulate import tabulate
class Regi:
    def registration(self):
        
        text = "USER REGISTRATION FORM"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        try:
            while True:
                Name = input("Enter the Name: ").strip()
                if not Name.replace(" ", "").isalpha():
                    print(" Name must contain only alphabets and spaces.")
                else:
                    break
                
            while True:
                Email = input("Enter the Email: ").strip()
                if '@' not in Email or '.' not in Email or len(Email) < 5 or Email.startswith('@') or Email.endswith('@') or '.com' not in Email or 'gmail' not in Email:
                    print(" Invalid email format.")
                else:
                    break 

            while True: 
                Mobile = input("Enter the Mobile no: ").strip()
                if not Mobile.isdigit() or len(Mobile) != 10 or Mobile[0] not in "6789":
                    print(" Mobile number must be 10 digits and start with 6/7/8/9.")
                else:
                    break

                
            Address = input("Enter the Address: ").strip()
                


            while True:   
                password = input("Enter the 4 digit password: ").strip()
                C_passw = input("Enter the Confirm Password: ").strip()

                if len(password) < 4:
                    print(" Password must be at least 4 characters long.")
                elif password != C_passw:
                    print(" Password and Confirm Password do not match.")
                else:
                    break

            text = "Registration successful!"
            data = [[text.center(50)]]  
            print(tabulate(data, tablefmt="grid"))
        

            UData = f"{Name}, {Email}, {Mobile}, {password}, {C_passw}, {Address}\n"
            try:
                with open("Pharmacy Management System/udata.txt", "a") as fp:
                    fp.write(UData)
                print("********************* User data saved successfully **********************")
                
            except Exception as e:
                print(" Error writing user data:", e)

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(" Error during registration:", e)


if __name__ == '__main__':
    r = Regi()
    r.registration()
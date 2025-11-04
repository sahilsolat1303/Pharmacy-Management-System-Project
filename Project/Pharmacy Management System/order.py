from tabulate import tabulate
import globals
class Pharmacy:
    

    def show_medicines(self):
        try:
            data = []
            with open("Pharmacy Management System/medicineData.txt", "r") as f:
                for line in f:
                    m_id, name, m_type, price, stock = line.strip().split(", ")
                    data.append([m_id, name, m_type, price, stock])

            print("\n--- 💊 Medicines Available ---")
            print(tabulate(data, headers=["ID", "Name", "Type", "Price", "Quantity"], tablefmt="grid"))
        except FileNotFoundError:
            print("❌ Medicines stock file not found!")

    from tabulate import tabulate

    def order_medicine(self):
        try:
            no_of_medicine = int(input("Enter how many medicines you want to order: "))
            if no_of_medicine <= 0:
                print("❌ Please enter a number greater than 0.")
                return

            user = globals.logged_in_user
            medicines = []
            with open("Pharmacy Management System/medicineData.txt", "r") as f:
                for line in f:
                    m_id, name, m_type, price, stock = line.strip().split(", ")
                    medicines.append([m_id, name, m_type, int(price), int(stock)])

            ordered_items = []
            total_amount = 0

            while no_of_medicine > 0:
                med_id = input("\nEnter medicine ID: ").strip()
                try:
                    qty = int(input("Enter quantity: "))
                except ValueError:
                    print("❌ Please enter a valid number for quantity.")
                    continue

                found = False
                for med in medicines:
                    if med[0] == med_id:
                        found = True
                        if qty <= med[4]:
                            total = qty * med[3]
                            total_amount += total
                            ordered_items.append([med[1], qty, med[3], total])
                            med[4] -= qty  # Reduce stock
                            print(f"✅ Added {qty} of {med[1]} (Subtotal: {total})")
                        else:
                            print("❌ Not enough stock available!")
                        break

                if not found:
                    print("❌ Medicine ID not found!")

                no_of_medicine -= 1

            if not ordered_items:
                print("⚠️ No valid orders placed.")
                return

            # ---------- Payment Section ----------
            print("\n--- 💳 PAYMENT SECTION ---")
            text = f"📝 TOTAL AMOUNT TO PAY: {total_amount}"
            data = [[text.center(50)]]
            print(tabulate(data, tablefmt="grid"))

            card_no = input("Enter your 16-digit card number: ")
            cvv = input("Enter 3-digit CVV: ")
            passw = input("Enter 4-digit password: ")

            if len(card_no) == 16 and card_no.isdigit() and len(cvv) == 3 and cvv.isdigit() and len(passw) == 4:
                print(tabulate([[f"{total_amount} Payment Successful ✅"]], tablefmt="grid"))

                # Save orders to file
                with open("Pharmacy Management System/orderData.txt", "a") as f:
                    for item in ordered_items:
                        f.write(f"{user}, {item[0]}, {item[1]}, Total={item[3]}\n")

                # Update medicine stock
                with open("Pharmacy Management System/medicineData.txt", "w") as f:
                    for m in medicines:
                        f.write(f"{m[0]}, {m[1]}, {m[2]}, {m[3]}, {m[4]}\n")

                print("\n✅ Order placed successfully!")
                print(tabulate(
                    [[user, i[0], i[1], i[2], i[3]] for i in ordered_items],
                    headers=["User", "Medicine", "Qty", "Price", "Total"],
                    tablefmt="grid"
                ))
            else:
                print("\n❌ Invalid card details! Payment failed.")
        except ValueError:
            print("❌ Please enter a valid number for medicines.")
        except Exception as e:
            print("⚠️ Error:", e)

   
    def view_orders(self):
        try:
            data = []
            with open("Pharmacy Management System/orderData.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(", ")
                    data.append(parts)

            if data:
                print("\n--- Orders ---")
                print(tabulate(data, headers=["User", "Medicine", "Qty", "Total"], tablefmt="grid"))
            else:
                print("❌ No orders yet!")
        except FileNotFoundError:
            print("❌ No orders yet!")


    def show_my_orders(self):
        
        try:
            data = []
            with open("Pharmacy Management System/orderData.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(", ")
                    if parts[0].lower() == globals.logged_in_user.lower():  
                        data.append(parts[1:])

            if data:
                print(f"\n--- Orders for {globals.logged_in_user.capitalize()} ---")
                print(tabulate(data, headers=["Medicine", "Qty", "Price", "Total"], tablefmt="grid"))
            else:
                print("❌ No orders found for you.")
        except FileNotFoundError:
            print("❌ No orders placed yet.")



    def delete_order(self):
        text = "DELETE THE ORDER"
        data = [[text.center(50)]]  
        print(tabulate(data, tablefmt="grid"))
        user= input("Enter the user name to delete: ").strip()
        found = False
        lines = []

        try:
            with open("Pharmacy Management System/orderData.txt", "r") as f:
                for line in f:
                    if line.strip().split(",")[0] != user:
                        lines.append(line)
                    else:
                        found = True
        except FileNotFoundError:
            print("⚠️ Error: orderData.txt file not found.")
            return
        except Exception as e:
            print("⚠️ Error reading file:", e)
            return
        
        try:
            with open("Pharmacy Management System/orderData.txt", "w") as f:
                f.writelines(lines)
        except Exception as e:
            print("⚠️ Error writing file:", e)
            return
        if found:
            print(" ✅ Order is deleted.")
        else:
            print(" ❌ Order not found.")

    

    

if __name__=='__main__':
    p=Pharmacy()
    # p.view_orders()
    p.show_medicines()
    p.order_medicine()
    # p.show_my_orders()
    # p.delete_order()

"""WeCare Beauty Products Management System - Simplified Version"""

import datetime
import random

# Initial welcome print statements
print("\n\n")
print("     " * 5 + "WeCare Beauty Products")
print("\n")
print("     " * 3 + "Manamaiju, Kathmandu | Phone No: 9849381818")
print("\n")
print("-" * 80)
now = datetime.datetime.now()
print("     " * 3 + "Welcome to the system! " + now.strftime('%Y-%m-%d %H:%M:%S'))
print("-" * 80)
print("\n")
print("Buy 3 Get 1 Free on all products!")
print("\n")

# Read inventory from file or create if not exists
try:
    file = open("inventory.txt", "r")
    data = file.readlines()
    file.close()

    inventory_dict = {}
    p_id = 1
    for line in data:
        line = line.replace("\n", "").split(",")
        cleaned_line = []
        for item in line:
            if item.startswith(" "):
                item = item[1:]
            if item.endswith(" "):
                item = item[:-1]
            cleaned_line.append(item)
        inventory_dict[p_id] = cleaned_line
        p_id += 1

except:
    print("Inventory file 'inventory.txt' not found. Creating a new one with sample data.")
    products = [
        "Vitamin C Serum, Garnier, 200, 1000, France",
        "Skin Cleanser, Cetaphil, 100, 280, Switzerland",
        "Sunscreen, Aqualogica, 200, 700, India",
    ]

    try:
        file = open("inventory.txt", "w")
        for product in products:
            file.write(product + "\n")
        file.close()
        print("Inventory file created successfully!")

        # Read the newly created file
        file = open("inventory.txt", "r")
        data = file.readlines()
        file.close()

        inventory_dict = {}
        p_id = 1
        for line in data:
            line = line.replace("\n", "").split(",")
            cleaned_line = []
            for item in line:
                if item.startswith(" "):
                    item = item[1:]
                if item.endswith(" "):
                    item = item[:-1]
                cleaned_line.append(item)
            inventory_dict[p_id] = cleaned_line
            p_id += 1
    except:
        print("Error creating inventory file.")
        exit()

# Display inventory in a formatted table
print("*" * 80)
print("ID\t\tName\t\t\tBrand\t\tQty\tCost Price\tSelling Price\tOrigin")
print("*" * 80)

for key, value in inventory_dict.items():
    try:
        selling_price = float(value[3]) * 3  # 200% markup
        print(str(key) + "\t" + value[0] + "\t\t" + value[1] + "\t\t" + value[2] + "\t" +
              value[3] + "\t\t" + str(round(selling_price, 2)) + "\t\t" + value[4])
    except:
        print("Error displaying product " + str(key))

# Main application loop
main_loop = True
while main_loop:
    try:
        # Display main menu
        print("\n" + "=" * 30)
        print("MAIN MENU")
        print("=" * 30)
        print("1. Purchase (Restock)")
        print("2. Sale")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # OPTION 1: PURCHASE/RESTOCK PRODUCTS
        if choice == 1:
            print("\n" + "=" * 40)
            print("PURCHASE/RESTOCK PRODUCTS")
            print("=" * 40)

            try:
                # Get supplier information
                supplier_name = input("Enter supplier name: ")
                while supplier_name == "":
                    print("Input cannot be empty.")
                    supplier_name = input("Enter supplier name: ")

                items_to_restock = []

                more_items = "y"
                while more_items.lower() == "y":
                    # Display available products
                    print("\nAvailable products:")
                    for pid, product in inventory_dict.items():
                        print(str(pid) + ". " + product[0] + " (" + product[1] + ") - Current Stock: " +
                              product[2] + " - Cost: " + product[3])

                    # Get product to restock
                    max_pid = max(inventory_dict.keys())
                    pid = int(input("\nEnter product ID to restock: "))
                    while pid < 1 or pid > max_pid:
                        print(f"Please enter a valid product ID between 1 and {max_pid}.")
                        pid = int(input("Enter product ID to restock: "))

                    # Get quantity to restock
                    qty = int(input("Enter quantity to restock: "))
                    while qty < 1:
                        print("Value must be at least 1.")
                        qty = int(input("Enter quantity to restock: "))

                    # Option to change price
                    change_price = input("Change cost price? (y/n): ")
                    new_cost = None
                    if change_price.lower() == "y":
                        new_cost = float(input("Enter new cost price: "))
                        while new_cost <= 0:
                            print("Value must be greater than 0.")
                            new_cost = float(input("Enter new cost price: "))

                    # Add to list of items to restock
                    items_to_restock.append({
                        "id": pid,
                        "quantity": qty,
                        "new_cost": new_cost
                    })

                    # Ask if more items
                    more_items = input("Add more items? (y/n): ")

                # Generate restock invoice
                if items_to_restock:
                    now = datetime.datetime.now()
                    today = now.strftime("%Y-%m-%d")
                    time_stamp = now.strftime("%H%M%S")
                    invoice_number = "RESTOCK-" + str(random.randint(1000, 9999))

                    clean_name = ""
                    for char in supplier_name:
                        if char == ' ':
                            clean_name += '_'
                        else:
                            clean_name += char
                    filename = invoice_number + "_" + clean_name + "_" + today + "_" + time_stamp + ".txt"

                    total_amount = 0

                    try:
                        file = open(filename, "w")
                        file.write("\t \t \t \t WeCare BEAUTY PRODUCTS\n")
                        file.write("\t \t \t \t RESTOCK INVOICE\n")
                        file.write("=" * 80 + "\n\n")
                        file.write("Invoice Number: " + invoice_number + "\n")
                        file.write("Date: " + today + "\n")
                        file.write("Supplier: " + supplier_name + "\n\n")
                        file.write("-" * 80 + "\n")
                        file.write("Product         Brand          Qty   Cost Price Amount     \n")
                        file.write("-" * 80 + "\n")

                        # Also print to screen
                        print("\n\t \t \t \t WeCare BEAUTY PRODUCTS")
                        print("\t \t \t \t RESTOCK INVOICE")
                        print("=" * 80 + "\n")
                        print("Invoice Number: " + invoice_number)
                        print("Date: " + today)
                        print("Supplier: " + supplier_name + "\n")
                        print("-" * 80)
                        print("Product         Brand          Qty   Cost Price Amount     ")
                        print("-" * 80)

                        for item in items_to_restock:
                            pid = item["id"]
                            qty_restocked = item["quantity"]
                            new_cost = item.get("new_cost", None)

                            product = inventory_dict[pid]
                            product_name = product[0]
                            brand = product[1]
                            current_qty = int(product[2])

                            # Update cost price if provided
                            if new_cost:
                                product[3] = str(new_cost)

                            cost_price = float(product[3])
                            amount = cost_price * qty_restocked
                            total_amount += amount

                            # Format for fixed width
                            product_name_fmt = product_name + " " * (15 - len(product_name))
                            brand_fmt = brand + " " * (15 - len(brand))
                            qty_fmt = str(qty_restocked) + " " * (5 - len(str(qty_restocked)))
                            price_fmt = str(round(cost_price, 2)) + " " * (10 - len(str(round(cost_price, 2))))
                            amount_fmt = str(round(amount, 2)) + " " * (10 - len(str(round(amount, 2))))

                            # Write to file
                            file.write(product_name_fmt + brand_fmt + qty_fmt + price_fmt + amount_fmt + "\n")

                            # Also print to screen
                            print(product_name_fmt + brand_fmt + qty_fmt + price_fmt + amount_fmt)

                            # Update inventory
                            inventory_dict[pid][2] = str(current_qty + qty_restocked)

                        # Write total
                        file.write("-" * 80 + "\n")
                        total_str = "Total Amount:" + " " * (45 - 13) + str(round(total_amount, 2))
                        file.write(total_str + "\n")
                        file.write("=" * 80 + "\n")
                        file.close()

                        # Also print to screen
                        print("-" * 80)
                        print(total_str)

                        #split, len, list functions, lower, datetime,
                        print("=" * 80)

                        print("\nRestock invoice generated: " + filename)

                        # Update inventory file
                        file = open("inventory.txt", "w")
                        for pid, product in inventory_dict.items():
                            line = ""
                            for i, item in enumerate(product):
                                line += item
                                if i < len(product) - 1:
                                    line += ", "
                            file.write(line + "\n")
                        file.close()
                        print("Inventory updated successfully!")
                    except:
                        print("Error generating restock invoice.")
                else:
                    print("No items were restocked.")
            except:
                print("Error during purchase process.")

        # OPTION 2: SELL PRODUCTS
        elif choice == 2:
            print("\n" + "=" * 40)
            print("SELL PRODUCTS")
            print("=" * 40)

            try:
                # Get customer information
                customer_name = input("Enter customer name: ")
                while customer_name == "":
                    print("Input cannot be empty.")
                    customer_name = input("Enter customer name: ")

                phone_number = input("Enter phone number: ")
                while phone_number == "":
                    print("Input cannot be empty.")
                    phone_number = input("Enter phone number: ")

                items_to_sell = []

                more_items = "y"
                while more_items.lower() == "y":
                    # Display available products with selling price
                    print("\nAvailable products:")
                    for pid, product in inventory_dict.items():
                        selling_price = float(product[3]) * 3  # 200% markup
                        print(str(pid) + ". " + product[0] + " (" + product[1] + ") - Price: $" +
                              str(round(selling_price, 2)) + " - Stock: " + product[2])

                    # Get product to sell
                    max_pid = max(inventory_dict.keys())
                    pid = int(input("\nEnter product ID to sell: "))
                    while pid < 1 or pid > max_pid:
                        print(f"Please enter a valid product ID between 1 and {max_pid}.")
                        pid = int(input("Enter product ID to sell: "))

                    # Check current stock
                    current_stock = int(inventory_dict[pid][2])
                    print("Available stock: " + str(current_stock))

                    # Get quantity to sell
                    qty = int(input("Enter quantity to sell: "))
                    while qty < 1:
                        print("Value must be at least 1.")
                        qty = int(input("Enter quantity to sell: "))

                    # Calculate free items (Buy 3 Get 1 Free)
                    free_items = qty // 3
                    total_items_needed = qty + free_items

                    # Check if enough stock
                    while total_items_needed > current_stock:
                        print("Not enough stock! Available: " + str(current_stock) +
                              ", Required: " + str(total_items_needed) + " (including " + str(free_items) + " free)")
                        print("Please choose a different quantity or product.")
                        qty = int(input("Enter quantity to sell: "))
                        free_items = qty // 3
                        total_items_needed = qty + free_items

                    # Add to list of items to sell
                    items_to_sell.append({
                        "id": pid,
                        "quantity": qty,
                        "free_items": free_items
                    })

                    # Inform about free items
                    print("Customer will receive " + str(free_items) + " free items with this purchase!")

                    # Ask if more items
                    more_items = input("Add more items? (y/n): ")

                # Generate sale invoice if items were added
                if items_to_sell:
                    now = datetime.datetime.now()
                    today = now.strftime("%Y-%m-%d")
                    time_stamp = now.strftime("%H%M%S")
                    invoice_number = "SALE-" + str(random.randint(1000, 9999))

                    clean_name = ""
                    for char in customer_name:
                        if char == ' ':
                            clean_name += '_'
                        else:
                            clean_name += char
                    filename = invoice_number + "_" + clean_name + "_" + today + "_" + time_stamp + ".txt"

                    total_amount = 0
                    shipping_cost = 0

                    try:
                        file = open(filename, "w")
                        file.write("\t \t \t \t WeCare BEAUTY PRODUCTS\n")
                        file.write("\t \t Manamaiju, Kathmandu | Phone No: 9811112255\n")
                        file.write("=" * 80 + "\n\n")
                        file.write("Invoice Number: " + invoice_number + "\n")
                        file.write("Date: " + today + "\n")
                        file.write("Customer Name: " + customer_name + "\n")
                        file.write("Phone Number: " + phone_number + "\n\n")
                        file.write("-" * 80 + "\n")
                        file.write("Product         Brand          Qty   Free  Price      Amount     \n")
                        file.write("-" * 80 + "\n")

                        # Also print to screen
                        print("\n\t \t \t \t WeCare BEAUTY PRODUCTS")
                        print("\t \t Manamaiju, Kathmandu | Phone No: 9811112255")
                        print("=" * 80 + "\n")
                        print("Invoice Number: " + invoice_number)
                        print("Date: " + today)
                        print("Customer Name: " + customer_name)
                        print("Phone Number: " + phone_number + "\n")
                        print("-" * 80)
                        print("Product         Brand          Qty   Free  Price      Amount     ")
                        print("-" * 80)

                        for item in items_to_sell:
                            pid = item["id"]
                            qty_purchased = item["quantity"]
                            free_items = item["free_items"]

                            product = inventory_dict[pid]
                            product_name = product[0]
                            brand = product[1]
                            current_qty = int(product[2])
                            cost_price = float(product[3])

                            # Calculate selling price (200% markup)
                            selling_price = cost_price * 3

                            # Calculate amount
                            amount = selling_price * qty_purchased
                            total_amount += amount

                            # Format for fixed width
                            product_name_fmt = product_name + " " * (15 - len(product_name))
                            brand_fmt = brand + " " * (15 - len(brand))
                            qty_fmt = str(qty_purchased) + " " * (5 - len(str(qty_purchased)))
                            free_fmt = str(free_items) + " " * (5 - len(str(free_items)))
                            price_fmt = str(round(selling_price, 2)) + " " * (10 - len(str(round(selling_price, 2))))
                            amount_fmt = str(round(amount, 2)) + " " * (10 - len(str(round(amount, 2))))

                            # Write to file
                            file.write(product_name_fmt + brand_fmt + qty_fmt + free_fmt + price_fmt + amount_fmt + "\n")

                            # Also print to screen
                            print(product_name_fmt + brand_fmt + qty_fmt + free_fmt + price_fmt + amount_fmt)

                            # Update inventory
                            inventory_dict[pid][2] = str(current_qty - (qty_purchased + free_items))

                        # Ask about shipping
                        shipping_input = input("\nDo you want your products to be shipped? (Y/N): ")
                        if shipping_input.upper() == "Y":
                            shipping_cost = 500
                            shipping_str = "Shipping Cost:" + " " * (45 - 14) + str(shipping_cost)
                            file.write(shipping_str + "\n")
                            print(shipping_str)

                        # Write total
                        grand_total = total_amount + shipping_cost
                        file.write("-" * 80 + "\n")
                        total_str = "Total Amount:" + " " * (45 - 13) + str(round(grand_total, 2))
                        file.write(total_str + "\n")
                        file.write("=" * 80 + "\n")
                        file.write("\nThank you for shopping with us!\n")
                        file.write("Buy 3 Get 1 Free on all products!\n")
                        file.close()

                        # Also print to screen
                        print("-" * 80)
                        print(total_str)
                        print("=" * 80)
                        print("\nThank you for shopping with us!")
                        print("Buy 3 Get 1 Free on all products!")

                        print("\nInvoice generated: " + filename)

                        # Update inventory file
                        file = open("inventory.txt", "w")
                        for pid, product in inventory_dict.items():
                            line = ""
                            for i, item in enumerate(product):
                                line += item
                                if i < len(product) - 1:
                                    line += ", "
                            file.write(line + "\n")
                        file.close()
                        print("Inventory updated successfully!")

                    except:
                        print("Error generating sale invoice.")
                else:
                    print("No items were sold.")
            except:
                print("Error during sale process.")

        # OPTION 3: EXIT
        elif choice == 3:
            print("Thank you for using WeCare Beauty Products")
            main_loop = False

        else:
            print("Invalid choice! Please try again.")

    except:
        print("An error occurred. Please try again.")

print("The application has exited. Goodbye!")

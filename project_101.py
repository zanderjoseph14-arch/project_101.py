inventory = []


def save_items():
    with open("inventory.txt", "w") as file:
        for item in inventory:
            file.write(f"{item['name']},{item['quantity']},{item['price']}\n")


def load_items():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                name, quantity, price = line.strip().split(",")

                item = {
                    "name": name,
                    "quantity": int(quantity),
                    "price": float(price)
                }

                inventory.append(item)

    except FileNotFoundError:
        pass


load_items()


def add_item():
    name = input("Enter item name: ")
    
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    item = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    inventory.append(item)

    save_items()

    print("Item added successfully!")


def view_items():
    if len(inventory) == 0:
        print("\nInventory is empty.")
        return

    print("\n===== INVENTORY LIST =====")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']}")
        print(f"   Quantity: {item['quantity']}")
        print(f"   Price: ₱{item['price']:.2f}")
        print("-------------------------")


def update_item():
    view_items()

    if len(inventory) == 0:
        return

    try:
        item_num = int(input("Enter item number to update: "))

        if 1 <= item_num <= len(inventory):
            item = inventory[item_num - 1]

            print(f"Updating {item['name']}")

            item['name'] = input("New item name: ")

            item['quantity'] = int(input("New quantity: "))
            item['price'] = float(input("New price: "))

            save_items()

            print("Item updated successfully!")

        else:
            print("Invalid item number.")

    except ValueError:
        print("Invalid input.")


def delete_item():
    view_items()

    if len(inventory) == 0:
        return

    try:
        item_num = int(input("Enter item number to delete: "))

        if 1 <= item_num <= len(inventory):
            removed = inventory.pop(item_num - 1)

            save_items()

            print(f"{removed['name']} deleted successfully!")

        else:
            print("Invalid item number.")

    except ValueError:
        print("Invalid input.")

while True:
    print("\n===== INVENTORY MENU =====")
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        add_item()

    elif choice == "2":
        view_items()

    elif choice == "3":
        update_item()

    elif choice == "4":
        delete_item()

    elif choice == "5":
        print("Exiting Inventory System...")
        break

    else:
        print("Invalid choice. Please try again.")
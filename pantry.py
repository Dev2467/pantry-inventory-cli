#import a list of items and store items in jason file
import json
import csv
def load_inventory(filename="inventory.json"):
    """Load the inventory list from a JSON file, or return an empty list if it doesn't exist."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print("Warning: inventory file is not a list. Starting with empty inventory.")
                return []
    except FileNotFoundError:
        # First time running the app: no file yet
        return []
    except json.JSONDecodeError:
        # File exists but has invalid JSON
        print("Warning: inventory file is corrupted. Starting with empty inventory.")
        return []
    
def save_inventory(inventory, filename="inventory.json"):
    """Save the inventory list to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=2)

def print_menu():
    #    print("\n=== Pantry Menu ===")
    print("\n=== Pantry Menu ===")
    print("1. View inventory")
    print("2. Add item(s)")
    print("3. Update item quantity")
    print("4. Remove item")
    print("5. View low-stock items")
    print("6. Export inventory.csv")
    print("7. Exit")
    
def find_item_index(inventory,name):
    #    """Return the index of the item with this name (case-insensitive), or -1 if not found."""
    target = name.strip().lower()
    for index, item in enumerate(inventory):
        if item["name"].strip().lower() == target:
            return index
    return -1 

def print_low_stock(inventory):
    #    """Show only items where quantity is at or below the minimum quantity."""
    low_items = []
    for item in inventory:
        quantity = item["quantity"]
        min_q = item["min_quantity"]
        #"""Show only items where quantity is at or below the minimum quantity."""
        if min_q and quantity <= min_q:
            low_items.append(item)

        if not low_items:
            print("\nNo low-stock items. You're good!")
        return

    print("\nLow-stock items:")
    for item in low_items:
        print(f"- {item['name']}: {item['quantity']} {item['unit']} (min: {item['min_quantity']})")

def export_inventory_to_csv(inventory,filename="inventory.csv"):
    #"""Export the current inventory to a csv file"""
    if not inventory:
        print("Inventory is Empty.Nothing to export.")
        return
    #"Choose the coloums for the csv file(header rows)"
    fieldnames = ["name", "quantity", "unit", "min_quantity"]

    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            #write the header
            writer.writeheader()

            #write each item as a row
            for item in inventory:
                writer.writerow(item)

        print(f"Inventory exported to {filename}")
    except OSError as e:
        print(f,"Error exporting inventory: {e}")

def main():
    #Collecting info from user
    print("Welcome to the Pantry App")

    inventory = load_inventory()
    print(f"Loaded {len(inventory)} item(s) from inventory.json")
    # Add the item to the inventory list using a loop 
    while True:
        print_menu()
        choice = input ("Select an option(1-7) :").strip()
        if choice == "1":
            #view inventory
            print_inventory(inventory)
            
        elif choice == "2": 
            #add items 
            while True:
                add_more = input("Add a new item? (y/n): ").strip().lower()
                if add_more != "y":
                    break
                item = get_item_from_user()
                inventory.append(item)
                save_inventory(inventory)
                print("Item added and inventory saved.\n")

        elif choice == "3":
        # Update item quantity
            name = input("Enter the item name to update: ").strip()
            index = find_item_index(inventory, name)

            if index == -1:
                print(f"Item '{name}' not found.")
            else:
                new_qty_text = input("Enter new quantity: ").strip()
                new_qty = float(new_qty_text)
                inventory[index]["quantity"] = new_qty
                save_inventory(inventory)
                print(f"Quantity for '{name}' updated to {new_qty}.")
            
        elif choice == "4":
            # Remove item
            name = input("Enter the item name to remove: ").strip()
            index = find_item_index(inventory, name)
            if index == -1:
                print(f"Item '{name}' not found.")
            else:
                removed = inventory.pop(index)
                save_inventory(inventory)
                print(f"Removed '{removed['name']}' from inventory.")

        elif choice == "5":
            # View low-stock items
            print_low_stock(inventory)

        elif choice == "6":
            #Export inventory.csv
            export_inventory_to_csv(inventory)

        elif choice == "7":
            # Exit
            print("\nSession finished.")
            print_inventory(inventory)
            break
    
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

def get_item_from_user():
     #1 Get info from user
    name = input("Item name: ").strip()
    quantity_text = input("Quantity (number): ")
    unit = input("Unit (can,pack,jar,etc):").strip()
    min_quantity = input("Minimum quantity before restocking (number, optional): ")

    #2 Convert text into numbers where needed
    #the iput function always returns a string.The following function will convert this into a number 
    quantity = float(quantity_text)

    # If the user just presses Enter for min quantity, treat it as 0
    if min_quantity.strip() == "":
        min_quantity = 0.0
    else:
        min_quantity = float(min_quantity)

     #3 Build a dictionary to represent an item 
    item = {
        "name" : name,
        "quantity" : quantity,
        "unit" : unit,
        "min_quantity" : min_quantity,
}
    
    return item

def print_inventory(inventory):
    """Print the current inventory in a human readable way"""
    if not inventory:
        print("Your pantry is empty")
        return 
    
    print("\nCurrent panty inventory:")
    for item in inventory:
        name = item["name"]
        quantity = item["quantity"]
        unit = item["unit"]
        min_q = item["min_quantity"]
        print(f"- {name} : {quantity} {unit} (min: {min_q})")

if __name__ == "__main__":
   main()




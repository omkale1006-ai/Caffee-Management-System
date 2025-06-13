# Step 1: Caffe name and menu items
# Café Management System (Python Project)
cafe_name = "Cafe Delight"
menu = {
    "Coffee": 50,
    "Tea": 30,
    "Sandwich": 80,
    "Pastry": 60,
    "Burger": 100
}

# Step 2: caffee name and menu display
def display_menu():
    print(f"\nWelcome to {cafe_name}!")
    print("📜 Menu:")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

# Step 3: customer order taking
def take_order():
    name = input("Aapka naam kya hai?\n")
    print(f"Namaste {name}! Aapka swagat hai {cafe_name} mein.")
    
    order = []
    while True:
        item = input("Aap kya order karna chahte hain? (type 'done' to finish):\n")
        if item.lower() == 'done':
            break
        elif item in menu:
            order.append(item)
            print(f"{item} aapke order mein add ho gaya.")
        else:
            print("⚠️ Yeh item menu mein nahi hai. Kripya sahi item chuniye.")
    
    return name, order

# Step 4: calculate total bill
def calculate_bill(order):
    total = 0
    for item in order:
        total += menu[item]
    return total

# Step 5: bill display
def display_bill(name, order, total):
    print(f"\nBill for {name}")
    print("Aapka order:")
    for item in order:
        print(f"{item}: ₹{menu[item]}")
    print(f"Total Bill: ₹{total}")

# important function to run the program
def main():
    display_menu()
    name, order = take_order()
    total = calculate_bill(order)
    display_bill(name, order, total)
    print("🙏 Dhanyavaad! Aapka Cafe Delight mein aane ke liye shukriya!")

if __name__ == "__main__":
    main()

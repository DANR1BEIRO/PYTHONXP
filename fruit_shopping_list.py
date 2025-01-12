import time

def fruit_list():
    """
    A function that displays a list of available fruits for purchase with
    their respective prices and asks the user which item and quantity they
    want to add to their shopping list. At the end, it shows the quantity
    of each item and the total purchase amount
    """
    # dict to store the selected fruits, their quantities and prices 
    fruit_list = {} 
    # dict of available items in the menu             
    fruits_available = { #
        1: ("Banana (dozen)", 7.00),
        2: ("Apple (kg)", 10.50),
        3: ("Pineapple (each)", 5.00),
        4: ("Orange (kg)", 5.00),
        5: ("Strawberry (1 tray 250g)", 6.00),
        0: ("Quit", None)}
    
    while True:
        try: 
            print("\nAvailable options:")
            for key, (fruit_name, price) in fruits_available.items():
                if fruit_name != "Quit":
                    print(f"[{key}] {fruit_name} ${price:.2f}")
                else:
                    print(f"[{key}] {fruit_name}")
                
            choose = int(input("\nChoose one of the available options: "))
        
            if choose in fruits_available:
                fruit_name, price = fruits_available[choose]
                
                if fruit_name == "Quit":
                    print("Exiting the selection...")
                    time.sleep(2)
                    break
            
                quantity = float(input(f"\nHow many {fruit_name}(s) do you want to add? "))
                time.sleep(2)
            
                if fruit_name in fruit_list:
                    fruit_list[fruit_name]["quantity"] += quantity
                else:
                    fruit_list[fruit_name] = {"quantity": quantity, "price": price}
                
                print(f"{quantity} {fruit_name}(s) added to your list!")
 
            else:
                print("Pick up one of the five options or 6 to quit!")
        except ValueError:
            print("Only integer numbers are allowed!")
        
        
    total_cost = sum(item["quantity"] * item["price"] for item in fruit_list.values())
    
    print("\nThis is your fruit list:")
    for fruit, details in fruit_list.items():
        quantity = details["quantity"]
        price = details["price"]
        cost = quantity * price
        print(f"- {fruit}: {quantity} (${price:.2f} each) = ${cost:.2f}")
        
    print(f"\nTotal cost of your list: ${total_cost:.2f}")
            
if __name__=="__main__":
    fruit_list()


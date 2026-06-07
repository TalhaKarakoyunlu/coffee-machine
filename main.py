MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    inserted_quarters = int(input("how many quarters?: "))
    inserted_dimes = int(input("how many dimes?: "))
    inserted_nickles = int(input("how many nickles?: "))
    inserted_pennies = int(input("how many pennies?: "))
    total_inserted_money = inserted_quarters*0.25 + inserted_dimes*0.10 + inserted_nickles*0.05 + inserted_pennies*0.01
    print(f"You have inserted ${total_inserted_money}")
    return total_inserted_money

def is_transaction_successful(money_received, drink_cost):
    if money_received == 0:
        print("Please insert money next time.")
        return False
    elif money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if money_received == drink_cost:
            print("Exactly right amount inserted. There will be no change money given.")
        else:
            print(f"Here is ${round(money_received - drink_cost, 2)} in change.")
        return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Please enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\n")
    elif choice not in MENU:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            inserted_money = process_coins()
            if is_transaction_successful(inserted_money, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
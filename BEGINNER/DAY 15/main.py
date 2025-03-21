MENU = {
    "espresso": {
            "water": 50,
            "coffee": 18,
            "milk":0,
        "cost": 1.5,
    },
    "latte": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        "cost": 2.5,
    },
    "cappuccino": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_in_machine=0

def resource_check(coffee_name,coffe_list,resource_data):
    if (resource_data["water"]>=coffe_list[coffee_name]["water"])and(resource_data["milk"]>=coffe_list[coffee_name]["milk"])and(resource_data["coffee"]>=coffe_list[coffee_name]["coffee"]):
        resource_data["water"]-=coffe_list[coffee_name]["water"]
        resource_data["milk"] -= coffe_list[coffee_name]["milk"]
        resource_data["coffee"] -= coffe_list[coffee_name]["coffee"]
        return True
    return False

def report_of_machine():
    print(f"""Water:{resources["water"]}ml\nMilk:{resources["milk"]}ml\nCoffee: {resources["coffee"]}gm\nMoney:{money_in_machine}$""")


def money_functionality(price_of_coffee):
    print("Please Insert Coin In The Machine :")

    quarters = int(input("How many quarters? (Each is $0.25): "))
    dimes = int(input("How many dimes? (Each is $0.10): "))
    nickles = int(input("How many nickels? (Each is $0.05): "))
    pennies = int(input("How many pennies? (Each is $0.01): "))

    money_given=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    if money_given<price_of_coffee:
        print("Sorry that's not enough money. Money refunded.")
        return
    global money_in_machine
    money_in_machine+=price_of_coffee
    print(f"Extra money returned {round(money_given-price_of_coffee,2)}$")
    print("Here Your Coffee sir Enjoy..")

coffee_machine=True

while coffee_machine:

    user_order=input("“What would you like? (espresso/latte/cappuccino):”")

    if user_order=="off":
        coffee_machine=False
        continue

    elif user_order=="report":
        report_of_machine()
        continue
    elif user_order in MENU:
        if resource_check(user_order,MENU,resources):
            money_functionality(MENU[user_order]["cost"])
        else:
            print("Sorry , Machine Run Out Of Resources")
    else:
        print("Please inter valid data")

road_per_100 = 6.5
city_per_100 = 11.6
average_per_100 = 8.2

def get_float(text, decimal_places=None):
    answer = input(text)
    try:
        return round(float(answer), decimal_places)
    except:
        print("Insert a floating-point number!")
        return get_float(text)

def print_instructions():
    print("\n1 - Get fuel per 100km\n2 - Get Euros per 100km\n3 - €->km\n4 - km->€\n5 - Set fuel price.\n")

def set_fuel_price():
    return get_float("Insert the fuel price! ", 3)
    
def get_100km_fuel(fuel_price):
    road_100km = round(road_per_100 * fuel_price, 2)
    city_100km = round(city_per_100 * fuel_price, 2)
    average_100km = round(average_per_100 * fuel_price, 2)
    print("\nFuel consumption:")
    print(f"Road: {road_per_100}l/100km")
    print(f"City: {city_per_100}l/100km")
    print(f"Avg: {average_per_100}l/100km")
    print()

def get_100km_price(fuel_price):
    road_100km = round(road_per_100 * fuel_price, 2)
    city_100km = round(city_per_100 * fuel_price, 2)
    average_100km = round(average_per_100 * fuel_price, 2)
    print("\n100km fuel price:")
    print(f"Road: {road_100km}€/100km")
    print(f"City: {city_100km}€/100km")
    print(f"Avg: {average_100km}€/100km")
    print()

def calculate_km(fuel_price):
    print()
    money_given = get_float("Insert the amount of money given!(0 - exit) ", 2)
    while money_given != 0:
        amount_of_fuel = round(money_given / fuel_price, 2)
        print(f"{money_given}€ gets about {amount_of_fuel}l of fuel.")
        road_mileage = round(amount_of_fuel / road_per_100 * 100, 3)
        city_mileage = round(amount_of_fuel / city_per_100 * 100, 3)
        average_mileage = round(amount_of_fuel / average_per_100 * 100, 3)
        print(f"Road mileage: {road_mileage}km")
        print(f"City mileage: {city_mileage}km")
        print(f"Avg mileage: {average_mileage}km")
        print()
        money_given = get_float("Insert the amount of money given!(0 - exit) ", 2)

def calculate_money_with_km(fuel_price):
    print()
    kilometres = get_float("Insert the number of km driven!(0 - exit) ", 3)
    while kilometres != 0:
        road_fuel = kilometres * road_per_100 / 100
        city_fuel = kilometres * city_per_100 / 100
        average_fuel = kilometres * average_per_100 / 100

        road_cost = round(road_fuel * fuel_price, 2)
        city_cost = round(city_fuel * fuel_price, 2)
        average_cost = round(average_fuel * fuel_price, 2)

        print(f"Road cost: {road_cost}€")
        print(f"City cost: {city_cost}€")
        print(f"Avg cost: {average_cost}€")
        print()
        kilometres = get_float("Insert the number of km driven!(0 - exit) ", 3)

    

if __name__ == "__main__":
    fuel_price = set_fuel_price()
    print_instructions()
    action_to_do = input("What do you wish to do? ")
    while action_to_do.lower() != "exit":
        if action_to_do == "1":
            get_100km_fuel(fuel_price)
        elif action_to_do == "2":
            get_100km_price(fuel_price)
        elif action_to_do == "3":
            calculate_km(fuel_price)
        elif action_to_do == "4":
            calculate_money_with_km(fuel_price)
        elif action_to_do == "5":
            fuel_price = set_fuel_price()
        elif action_to_do == "info":
            print_instructions()
        else:
            print('Invalid action! Insert "info" to get list of commands!')
        action_to_do = input("What do you wish to do? ")
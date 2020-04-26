# road, city, average
list_per_100 = [6.5, 11.6, 8.2]

###INPUT###

def get_float(text, decimal_places=None):
    answer = input(text)
    try:
        return round(float(answer), decimal_places)
    except:
        print("Insert a floating-point number!")
        return get_float(text)

def set_fuel_price():
    return get_float("Insert the fuel price! ", 3)

###PRINTS###

def print_instructions():
    instructions = ["1 - l / 100km", "2 - € / 100km", "3 - € -> km", "4 - km -> €", "5 - l -> km", "6 - Calculate fuel and cost based on the Route", "7 - Set fuel price."]
    print(*instructions, sep="\n")

def print_km_by_litres(amount_of_fuel):
    """
    Print out mileage with given amount of fuel.
    
    Input: Amount of fuel in litres
    """
    road_mileage, city_mileage, average_mileage = calculate_km_with_litres(amount_of_fuel)
    print(f"Road mileage: {road_mileage}km")
    print(f"City mileage: {city_mileage}km")
    print(f"Avg mileage: {average_mileage}km")
    print()

def print_100km_fuel():
    """
    Print Fuel consumption per 100km
    """
    print("\nFuel consumption:")
    print(f"Road: {list_per_100[0]}l/100km")
    print(f"City: {list_per_100[1]}l/100km")
    print(f"Avg: {list_per_100[2]}l/100km")
    print()

def print_100km_price(fuel_price):
    road_100km, city_100km, average_100km = get_100km_price(fuel_price)
    print("\n100km fuel price:")
    print(f"Road: {road_100km}€/100km")
    print(f"City: {city_100km}€/100km")
    print(f"Avg: {average_100km}€/100km")
    print()

def print_mileage_from_money(fuel_price):
    while (money_given := get_float("Insert the amount of money given!(0 - exit) ", 2)) != 0:
        amount_of_fuel = calculate_fuel_with_money(money_given)
        print(f"{money_given}€ gets about {amount_of_fuel}l of fuel.")
        print_km_by_litres(amount_of_fuel)
        print()

def print_money_with_fuel(fuel_price):
    while (kilometres := get_float("Insert the number of km driven!(0 - exit) ", 3)) != 0:
        road_cost, city_cost, average_cost = calculate_money_with_km(fuel_price, kilometres)
        print(f"Road cost: {road_cost}€")
        print(f"City cost: {city_cost}€")
        print(f"Avg cost: {average_cost}€")
        print()

def print_kilometres_with_fuel():
    while (amount_of_fuel := get_float("Insert the amount of fuel in litres!(0 - exit) ", 2)) != 0:
        print_km_by_litres(amount_of_fuel)
        print()

def print_route_fuel(fuel_price):
    while (road_km := get_float("Insert both 0 to exit!\nInsert km on road: ", 3)) != 0 and (city_km := get_float("Insert km in the city: ", 3)) != 0:
        fuel, cost = calculate_route(road_km, city_km, fuel_price)
        print(f"Total fuel usage is {fuel}l")
        print(f"Total cost would be {cost}€")
        print()

###MATHS###

def calculate_km_with_litres(amount_of_fuel):
    """
    Calculate how many km can be driven with given fuel.
    
    Input: Amount of fuel in litres.
    Return: Average mileages.
    """
    return [round(amount_of_fuel / per_100 * 100, 3) for per_100 in list_per_100]

def get_100km_price(fuel_price):
    """
    Get how much 100km of fuel costs.

    Input: amount_of_fuel
    Return: Price of 100km of fuel in Euros
    """
    return [round(per_100 * fuel_price, 2) for per_100 in list_per_100]

def calculate_fuel_with_money(money_given):
    """
    Calculate how much fuel you get with given money.
    
    Input: Money given in Euros
    Return: Fuel in litres
    """
    return round(money_given / fuel_price, 2)

def calculate_1km_fuel():
    """
    Calculate fuel per 1 km.
    """
    return [per_100 / 100 for per_100 in list_per_100]

def calculate_money_with_km(fuel_price, kilometres):
    """
    Calculate how much certain amount of kilometres cost.

    Input: Fuel_price, kilometres driven
    Return: Fuel cost in Euros
    """
    
    amount_of_fuel = [(kilometres * km) for km in calculate_1km_fuel()]

    return [round(fuel * fuel_price, 2) for fuel in amount_of_fuel]

def calculate_route(road_km, city_km, fuel_price):
    """
    Calculate fuel and it's cost, given km on road, in city and fuel price.

    Input: km on road, km in city, fuel price
    Return fuel usage and it's price.
    """
    return (fuel := (road_km * (km_fuel := calculate_1km_fuel())[0] + city_km * km_fuel[1])), round(fuel * fuel_price, 2)

###MAIN###

if __name__ == "__main__":
    fuel_price = set_fuel_price()
    print_instructions()
    while (action_to_do := input("What do you wish to do? ")).lower() != "exit":
        if action_to_do == "1":
            print_100km_fuel()
        elif action_to_do == "2":
            print_100km_price(fuel_price)
        elif action_to_do == "3":
            print_mileage_from_money(fuel_price)
        elif action_to_do == "4":
            print_money_with_fuel(fuel_price)
        elif action_to_do == "5":
            print_kilometres_with_fuel()
        elif action_to_do == "6":
            print_route_fuel(fuel_price)
        elif action_to_do == "7":
            fuel_price = set_fuel_price()
        elif action_to_do == "info":
            print_instructions()
        else:
            print('Invalid action! Insert "info" to get list of commands!')

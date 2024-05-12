import db

from objects import Restaurant, Lineup



def add_restaurant(restaurants):    
    name = input("Restaurant Name: ").title()
    style = input("Menu Type: ") 
    notes = input("Notes: ")

    restaurant = Restaurant(name, style, notes)
    restaurants.add(restaurant)
    db.add_restaurant(restaurant)
    print(f"{restaurant.name} was added.\n")


def display_list(restaurants):
    if restaurants == None:
        print("There are currently no restaurants to list.")        
    else:
        print(f"{'':3}{'Name':25}{'Style':20}{'Notes':>6}")
        for restaurant in restaurants:
            print(f"{restaurant.name:25}{restaurant.style:20}{restaurant.notes:6}")
    print() 


def display_menu():
    print("MENU OPTIONS")
    print("1 – Display List")
    print("2 - Add Restaurant")
    print("3 - Exit program")
    print()


def main():

    display_menu()

    db.connect()
    restaurants = db.get_restaurants()

    
    while True:
        try:
            option = int(input("Menu option: "))
        except ValueError:
            option = -1
            
        if option == 1:
            display_list(restaurants)
        elif option == 2:
            add_restaurant(restaurants)
            restaurants = db.get_restaurants()
        elif option == 3:
            db.close()
            print("Bye!")
            break
        else:
            print("Not a valid option. Please try again.\n")
            display_menu()



if __name__ == "__main__":
    main()

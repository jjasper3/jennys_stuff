from dataclasses import dataclass

@dataclass
class Restaurant:
    name:str = ""
    style:str = ""
    notes:str = ""


class Lineup:
    def __init__(self):
        self.__list = []

    @property
    def count(self):
        return len(self.__list)

    def add(self, restaurant):
        return self.__list.append(restaurant)
    
    def remove(self, number):
        return self.__list.pop(number-1)
    
    def get(self, number):
        return self.__list[number-1]
    
    def set(self, number, restaurant):
        self.__list[number-1] = restaurant
        
    def move(self, oldNumber, newNumber):
        restaurant = self.__list.pop(oldNumber-1)
        self.__list.insert(newNumber-1, restaurant)

    def __iter__(self):
        for restaurant in self.__list:
            yield restaurant
            
        
def main():
    lineup = Lineup()
    for restaurant in lineup:
        print(restaurant.name, restaurant.style, restaurant.notes)
        
    print("Bye!")

if __name__ == "__main__":
    main()

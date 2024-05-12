
import sqlite3 


from contextlib import closing

from objects import Restaurant, Lineup

conn = None

def connect():
    global conn
    if not conn:

        DB_FILE = "restaurant.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_new(row):
    return Restaurant(row["name"], row["style"],
                  row["notes"])

def add_restaurant(restaurant):
    sql = '''INSERT INTO restaurant
                (name, style, notes)
              VALUES
                 (?,?,?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (restaurant.name, restaurant.style, restaurant.notes))
        conn.commit()


def get_restaurants():    
    query = '''SELECT name, style, notes
                from restaurant
                '''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    restaurants = Lineup()
    for row in results:
        restaurant = make_new(row)
        restaurants.add(restaurant)
    return restaurants


def main():
    connect()
    restaurants = get_restaurants()
    for restaurant in restaurants:
        print(restaurant.name, restaurant.style, restaurant.notes)


if __name__ == "__main__":
    main()

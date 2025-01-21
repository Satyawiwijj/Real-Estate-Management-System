# Real Estate Management System
# Author: Satya
import mysql.connector
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="",  
        database="real_estate_db"
    )
    print("Connected to the database successfully!")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit()
def show_menu():
    print("\n=== Real Estate Management System ===")
    print("1. Add Property")
    print("2. View Properties")
    print("3. Search Property by Location")
    print("4. Delete Property")
    print("5. Exit")
def add_property():
    property_name = input("Enter property name: ")
    location = input("Enter property location: ")
    price = float(input("Enter property price: "))
    property_type = input("Enter property type (e.g., Apartment, Villa): ")
    query = "INSERT INTO properties (name, location, price, type) VALUES (%s, %s, %s, %s)"
    values = (property_name, location, price, property_type)
    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        print("Property added successfully!")
    except mysql.connector.Error as e:
        print(f"Error adding property: {e}")
def view_properties():
    query = "SELECT * FROM properties"
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n=== Property List ===")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Location: {row[2]}, Price: {row[3]}, Type: {row[4]}")
    except mysql.connector.Error as e:
        print(f"Error fetching properties: {e}")
def search_property():
    location = input("Enter location to search: ")
    query = "SELECT * FROM properties WHERE location = %s"
    values = (location,)
    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        results = cursor.fetchall()
        if results:
            print("\n=== Search Results ===")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Location: {row[2]}, Price: {row[3]}, Type: {row[4]}")
        else:
            print("No properties found in this location.")
    except mysql.connector.Error as e:
        print(f"Error searching properties: {e}")
def delete_property():
    property_id = int(input("Enter property ID to delete: "))
    query = "DELETE FROM properties WHERE id = %s"
    values = (property_id,)
    try:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        print("Property deleted successfully!" if cursor.rowcount > 0 else "Property not found.")
    except mysql.connector.Error as e:
        print(f"Error deleting property: {e}")
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_property()
    elif choice == "2":
        view_properties()
    elif choice == "3":
        search_property()
    elif choice == "4":
        delete_property()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
connection.close()

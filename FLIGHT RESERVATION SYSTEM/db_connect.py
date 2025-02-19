import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rudr@2oo1",
        database="flight_reservation"
    )

def add_flight(airline, source, destination, departure, arrival, seats):
    db = connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO flights (airline, source, destination, departure_time, arrival_time, seats_available) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (airline, source, destination, departure, arrival, seats))
    db.commit()
    print("Flight added successfully!")
    db.close()

def add_passenger(name, email, phone):
    db = connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO passengers (name, email, phone) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, email, phone))
    db.commit()
    print("Passenger added successfully!")
    db.close()

def book_flight(passenger_id, flight_id):
    db = connect_db()
    cursor = db.cursor()

    # Check seat availability
    cursor.execute("SELECT seats_available FROM flights WHERE flight_id = %s", (flight_id,))
    flight = cursor.fetchone()
    
    if flight and flight[0] > 0:
        sql = "INSERT INTO reservations (passenger_id, flight_id) VALUES (%s, %s)"
        cursor.execute(sql, (passenger_id, flight_id))
        
        # Reduce seat count
        cursor.execute("UPDATE flights SET seats_available = seats_available - 1 WHERE flight_id = %s", (flight_id,))
        db.commit()
        print("Flight booked successfully!")
    else:
        print("No seats available!")
    
    db.close()

def main():
    while True:
        print("\nFlight Reservation System")
        print("1. Add Flight")
        print("2. Add Passenger")
        print("3. Book Flight")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            airline = input("Enter airline name: ")
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            departure = input("Enter departure time (YYYY-MM-DD HH:MM:SS): ")
            arrival = input("Enter arrival time (YYYY-MM-DD HH:MM:SS): ")
            seats = int(input("Enter available seats: "))
            add_flight(airline, source, destination, departure, arrival, seats)

        elif choice == "2":
            name = input("Enter passenger name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            add_passenger(name, email, phone)

        elif choice == "3":
            passenger_id = int(input("Enter passenger ID: "))
            flight_id = int(input("Enter flight ID: "))
            book_flight(passenger_id, flight_id)

        elif choice == "4":
            print("Exiting system.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

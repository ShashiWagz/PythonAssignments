import mysql.connector

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1093',
    autocommit=True
)


def get_airports_by_ident(icao):
    try:
        # Prepare the SQL query to fetch airport details by ICAO code
        sql = f"SELECT name, municipality FROM airport WHERE ident = %s"

        # Create a cursor to execute the query
        cursor = connection.cursor()
        cursor.execute(sql, (icao,))  # Passing ICAO code as a parameter to avoid SQL injection

        # Fetch the result
        results = cursor.fetchone()

        # Check if any airport is found
        if results:
            name, location = results
            print(f"Airport Name: '{name}', Location: '{location}'")
        else:
            print(f"No airports found with ICAO code: {icao}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()  # Ensure the cursor is closed


# Main program entry
if __name__ == "__main__":
    icao_code = input("Enter the ICAO code (e.g., EFHK for Helsinki-Vantaa): ").upper()
    get_airports_by_ident(icao_code)

# Close the database connection after the operation is complete
connection.close()

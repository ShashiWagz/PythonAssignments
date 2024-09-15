import mysql.connector
from geopy.distance import great_circle

connection = mysql.connector.connect (
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2011'
)

def get_airport_coordinates(icao):
    """Fetches the latitude and longitude of the airport based on ICAO code."""
    cursor = connection.cursor()
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao,))
    result = cursor.fetchone()
    return result

def calculate_distance(icao1, icao2):
    """Calculates the distance between two airports using ICAO codes."""
    coord1 = get_airport_coordinates(icao1)
    coord2 = get_airport_coordinates(icao2)

    if coord1 and coord2:
        distance = great_circle(coord1, coord2).kilometers
        print(f"The distance between {icao1} and {icao2} is {distance:.2f} kilometers.")
    else:
        print("One or both ICAO codes are invalid or not found in the database.")

if __name__ == "__main__":
    icao_code1 = input("Enter the ICAO code of the second airport: ").upper()
    calculate_distance(icao_code1, icao_code2)


connection.close()

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='1093',
    autocommit=True
)

def get_airports_by_ident(icao):
    sql = (f"SELECT name, muncipality FROM airport WHERE ident='{icao}'"
    cursor = connection.cursor())
    cursor.execute(sql,icao)
    results = cursor.fetchone()

    if results:
        name, location = results
        print(f"Airport Name: '{name}', Location: '{location}':")

    else:
        print(f"No airports found with ICAO code: {icao}")

if _name_ == "_main_":

    icao_code= input("Enter the country code (e.g., FI for Finland): ").upper()
    get_airports_by_ident(icao)

connection.close()
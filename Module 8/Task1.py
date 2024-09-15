import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2011',
    autocommit=True
)

def get_airports_by_country_code(country_code):

    sql = f"""
    SELECT type, COUNT(*) AS count
    FROM airport
    WHERE iso_country = '{country_code}'
    GROUP BY type
    ORDER BY count DESC
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        print(f"Airports in country code '{country_code}':")
        for row in results:
            airport_type, count = row
            print(f"{count} {airport_type} airports")
    else:
        print(f"No airports found for country code: {country_code}")

if _name_ == "_main_":
    country_code = input("Enter the country code (e.g., FI for Finland): ").upper()
    get_airports_by_country_code(country_code)

connection.close()
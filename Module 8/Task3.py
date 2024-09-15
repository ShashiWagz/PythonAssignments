from geopy.distance import geodesic

airport_coordinates = {
    "KJFK": (40.6413, -73.7781),  # JFK Airport (New York)
    "EGLL": (51.4700, -0.4543),  # Heathrow Airport (London)
    "KLAX": (33.9416, -118.4085),  # Los Angeles International Airport
    "LFPG": (49.0097, 2.5479),  # Charles de Gaulle Airport (Paris)
    "RJTT": (35.5494, 139.7798),  # Tokyo Haneda Airport
}

def get_coordinates(icao_code):
    return airport_coordinates.get(icao_code.upper())

def calculate_distance(icao1, icao2):
    coords_1 = get_coordinates(icao1)
    coords_2 = get_coordinates(icao2)

    if coords_1 and coords_2:
        distance = geodesic(coords_1, coords_2).kilometers
        print(f"The distance between {icao1.upper()} and {icao2.upper()} is {distance:.2f} kilometers.")
    else:
        print("One or both of the provided ICAO codes are invalid.")



def main():
    icao1 = input("Enter the ICAO code for the first airport: ").strip()
    icao2 = input("Enter the ICAO code for the second airport: ").strip()

    calculate_distance(icao1, icao2)


if __name__ == "__main__":
    main()

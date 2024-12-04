from flask import Flask, jsonify

app = Flask(__name__)

# Sample airport database
airport_db = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "KJFK": {"Name": "John F. Kennedy International Airport", "Location": "New York"},
    "EGLL": {"Name": "London Heathrow Airport", "Location": "London"},
    "EDDF": {"Name": "Frankfurt Airport", "Location": "Frankfurt"},
    "ZBAA": {"Name": "Beijing Capital International Airport", "Location": "Beijing"}
}

@app.route('/airport/<string:icao>', methods=['GET'])
def get_airport(icao):
    """Endpoint to fetch airport information by ICAO code."""
    airport_info = airport_db.get(icao.upper())
    if airport_info:
        response = {
            "ICAO": icao.upper(),
            "Name": airport_info["Name"],
            "Location": airport_info["Location"]
        }
    else:
        response = {
            "error": "Airport not found"
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        print("Chuck Norris Joke:")
        print(joke_data["value"])
    else:
        print("Failed to retrieve a joke. Please try again.")

# Run the function
get_chuck_norris_joke()

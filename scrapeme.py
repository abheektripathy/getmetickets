import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def scrape_flights(departure, destination, date):
    # Construct the URL for the Google Flights search
    url = f"https://www.google.com/flights?hl=en#flt={departure}.{destination}.{date}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the flight rows in the search results
    rows = soup.select('.gws-flights-results__result-item')

    flights = []
    for row in rows:
        # Extract the flight details from each row
        airline = row.select_one('.gws-flights-results__carriers').text.strip()
        departure_time = row.select_one('.gws-flights-results__times').text.strip()
        price = row.select_one('.gws-flights-results__price').text.strip()

        flights.append([airline, departure_time, price])

    return flights

if __name__ == '__main__':
    # Get user input for departure, destination, and date
    departure = input("Departure airport: ")
    destination = input("Destination airport: ")
    date = input("Date (YYYY-MM-DD): ")

    # Scrape the flights
    flights = scrape_flights(departure, destination, date)

    # Display the flights in a table
    headers = ["Airline", "Departure Time", "Price"]
    print(tabulate(flights, headers=headers))

import requests
from bs4 import BeautifulSoup
import csv

# Target URL
url = "http://quotes.toscrape.com"

# Send GET request
response = requests.get(url)

# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote containers
quotes = soup.find_all("div", class_="quote")

# Open a CSV file in write mode
with open("quotes.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header
    writer.writerow(["Quote", "Author"])
    
    # Loop through quotes and save them to the CSV file
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        writer.writerow([text, author])

print("Quotes have been saved to 'quotes.csv'.")

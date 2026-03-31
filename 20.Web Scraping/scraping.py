import requests
import pandas as pd
from bs4 import BeautifulSoup

books_info = []

# 1. Start the loop to iterate through all 50 pages
for i in range(1, 51):
    # Ensure the URL updates with each iteration of 'i'
    website = f"https://books.toscrape.com/catalogue/page-{i}.html"
    
    # 2. Make the network request
    request = requests.get(website)
    soup = BeautifulSoup(request.content, "html.parser")
    
    # 3. Find all book containers on the current page
    books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    # 4. Loop through each book found on the page
    for item in books:
        tag = item.find("h3").find("a")
        name = tag["title"]  # Use ['title'] because text is often truncated with '...'
        link = tag["href"]
        price = item.find("p", class_="price_color").text.strip()

        # Create a dictionary for the book data
        product = {
            "Name": name,
            "Price": price,
            "Link": link
        }

        # Add the dictionary to our list
        books_info.append(product)
    
    print(f"Finished scraping page {i}")

# 5. Convert the list of dictionaries into a DataFrame and save
df = pd.DataFrame(books_info)
df.to_csv("books_info.csv", index=False)

print("Scraping complete! File saved as books_info.csv")
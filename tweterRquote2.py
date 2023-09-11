# Imports
from bs4 import BeautifulSoup
import requests
import random
import pyautogui
import time
import clipboard  
# Import all the  library

# Function to scrape a random quote from the website with character count less than 270
def random_goodreads_quote():
    while True:
        # Send an HTTP GET request to the Goodreads website
        response = requests.get("https://www.goodreads.com/quotes")

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the quote elements on the page
            quotes = soup.find_all('div', class_='quoteText')

            # Select a random quote from the list
            selected_quote = random.choice(quotes).text.strip()

            # Split the quote to separate the text and author
            parts = selected_quote.split('―')
            quote_text = parts[0].strip()
            author = parts[1].strip()

            # Check if the character count is less than 270
            if len(selected_quote) <= 270:
                return f'"{quote_text}" - {author}'

        else:
            print('Failed to retrieve a quote. Trying again...')

# Rest of the code remains the same...
def post_quote(count):
    message = f"{random_goodreads_quote()}\n -@lenevos307 {count}\n HUM TOH DEEWANE MV SOON"  # Include the correct hashtag

    # Copy the message to the clipboard
    clipboard.copy(message)

    # Paste the message from the clipboard
    pyautogui.hotkey('ctrl', 'v')

    # Send Ctrl+Enter to post the tweet
    pyautogui.hotkey('ctrl', 'enter')

    # Update the count in the text file
    with open("count.txt", "w") as file:
        file.write(str(count))
# Main loop
time.sleep(5)

# Read the count from the text file if it exists, otherwise start from 0
try:
    with open("count.txt", "r") as file:
        count = int(file.read())
except FileNotFoundError:
    count = 0

while True:
    post_quote(count)
    count += 1

    # Sleep for 5 seconds before sending the next message
    time.sleep(5)
    #for i in range(3):#Remove # for the comments sending
    for i in range(2):#Add # for the comment sending
        pyautogui.hotkey('tab')

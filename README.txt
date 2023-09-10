
# Twitter Quote Bot

This is a Python script for posting random quotes from Goodreads to Twitter. It uses web scraping to fetch quotes and the PyAutoGUI library to automate the posting process.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Required Python libraries installed (`bs4`, `requests`, `pyautogui`, `time`, `clipboard`)
- Twitter account with access tokens (for posting tweets)
- Goodreads account (for fetching quotes)

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/twitter-quote-bot.git
   ```

2. Install the required Python libraries:

   ```bash
   pip install bs4 requests pyautogui clipboard
   ```

3. Create a Twitter Developer App and obtain access tokens. Replace the placeholders in your Python script with your Twitter API credentials.

4. Run the script:

   ```bash
   python tweterRquote2.py
   ```

## Usage

- The script fetches random quotes from Goodreads.
- Quotes with a character count less than or equal to 270 are posted on Twitter.
- The script keeps track of the count and posts quotes periodically.

## Customization

- You can customize the script to use a different source for quotes or change the posting frequency.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Goodreads](https://www.goodreads.com) for providing the quotes.

---

**Note**: This README is a template. Make sure to update it with relevant information about your project.

```

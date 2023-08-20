## Amazon Web Scraping Tool README

This Python script is designed to scrape product data from Amazon India's website. It utilizes the BeautifulSoup library to parse HTML and extract relevant information from Amazon product listings. The tool allows users to customize the search query and the number of pages to scrape, enabling them to gather data on specific products.

### Prerequisites

Before using this tool, make sure you have the following installed:

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using the following commands:

```bash
pip install requests
pip install beautifulsoup4
```

### Usage

1. Open the `amazon_scraper.py` file in a Python editor or IDE of your choice.

2. Customize the script to suit your needs. You can modify the following parameters:

   - `search_query`: The query to search for on Amazon (e.g., 'bags', 'shoes', 'electronics').
   - `pages_to_scrape`: The number of pages to scrape for each search query.

3. Save your changes.

4. Run the script using the command:

```bash
python amazon_scraper.py
```

### Customization

You can customize the script in the following ways:

1. **Search Query**: Change the `search_query` variable to target specific products or categories.

2. **Number of Pages**: Modify the `pages_to_scrape` variable to control how many pages of search results to scrape.

3. **Data Export**: By default, the scraped data is saved to a CSV file named `amazon_data.csv`. You can change the filename in the `with open()` statement if desired.

4. **Data Fields**: If you want to extract additional information from the product listings, you can inspect the HTML structure of the Amazon product pages and modify the parsing logic accordingly.

### Notes

- Keep in mind that web scraping might violate Amazon's terms of use. Ensure you are aware of Amazon's policies and use this tool responsibly.

- The script is set up to scrape data from Amazon India (`https://www.amazon.in`). If you intend to use it for other Amazon websites, you might need to adjust the base URL and other elements accordingly.

- This script provides a basic framework for web scraping Amazon. Depending on changes to Amazon's website structure, the script may need to be updated to continue functioning properly.

- The script is provided as-is, and any modifications or use of the script are at your own risk.

### Contact

For questions, feedback, or issues related to this tool, you can reach out to the author at [kamalsoni383@gmail.com](mailto:kamalsoni3839@gmail.com).

Happy scraping!
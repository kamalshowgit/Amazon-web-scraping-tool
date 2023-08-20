import csv
import requests
from bs4 import BeautifulSoup

def scrape_product_listing(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    data = []
    for product in products:
        product_url = 'https://www.amazon.in' + product.find('a', class_='a-link-normal').get('href')
        product_name = product.find('span', class_='a-size-medium').text.strip()
        product_price = product.find('span', class_='a-price-whole').text.strip()

        rating_element = product.find('span', {'class': 'a-icon-alt'})
        rating = rating_element.text.split()[0] if rating_element else 'N/A'

        review_count_element = product.find('span', {'class': 'a-size-base'})
        review_count = review_count_element.text.split()[0] if review_count_element else 'N/A'

        data.append({
            'Product URL': product_url,
            'Product Name': product_name,
            'Product Price': product_price,
            'Rating': rating,
            'Number of Reviews': review_count
        })

    return data

def scrape_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    description_element = soup.find('div', {'id': 'productDescription'})
    description = description_element.text.strip() if description_element else 'N/A'

    asin_element = soup.find('th', text='ASIN')
    asin = asin_element.find_next_sibling('td').text.strip() if asin_element else 'N/A'

    product_description_element = soup.find('div', {'id': 'productDescription_feature_div'})
    product_description = product_description_element.text.strip() if product_description_element else 'N/A'

    manufacturer_element = soup.find('a', {'id': 'bylineInfo'})
    manufacturer = manufacturer_element.text.strip() if manufacturer_element else 'N/A'

    return {
        'Description': description,
        'ASIN': asin,
        'Product Description': product_description,
        'Manufacturer': manufacturer
    }

def scrape_amazon_data():
    base_url = 'https://www.amazon.in/s'
    search_query = 'bags'
    pages_to_scrape = 20

    product_listing_data = []
    product_details_data = []

    for page in range(1, pages_to_scrape + 1):
        params = {
            'k': search_query,
            'crid': '2M096C61O4MLT',
            'qid': '1653308124',
            'sprefix': 'ba%2Caps%2C283',
            'ref': f'sr_pg_{page}'
        }

        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.content, 'html.parser')

        products = soup.find_all('div', {'data-component-type': 's-search-result'})

        for product in products:
            product_url = 'https://www.amazon.in' + product.find('a', class_='a-link-normal').get('href')
            product_listing_data.append({
                'Product URL': product_url,
                'Product Name': product.find('span', class_='a-size-medium').string.strip(),
                'Product Price': product.find('span', class_='a-price-whole').string.strip(),
                'Rating': product.find('span', {'class': 'a-icon-alt'}).string.split()[0],
                'Number of Reviews': product.find('span', {'class': 'a-size-base'}).string.split()[0]
            })

    for product_data in product_listing_data[:200]:
        url = product_data['Product URL']
        product_details = scrape_product_details(url)
        product_details.update(product_data)
        product_details_data.append(product_details)

    keys = ['Product URL', 'Product Name', 'Product Price', 'Rating', 'Number of Reviews',
            'Description', 'ASIN', 'Product Description', 'Manufacturer']

    with open('amazon_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(product_details_data)

    print('Scraping and data export complete.')

scrape_amazon_data()

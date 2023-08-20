import requests
from lxml import etree
import pandas as pd

def export_data_to_excel(url, output_file):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors

        # Parse the HTML content using lxml
        tree = etree.HTML(response.content)

        # Extract all the text elements within the webpage
        elements = tree.xpath('//*[not(self::script)][not(self::style)]/text()')
        elements = [elem.strip() for elem in elements if elem.strip()]

        # Identify column boundaries based on certain patterns or criteria
        column_boundaries = []
        for i, elem in enumerate(elements):
            if elem.isnumeric():
                if i > 0 and not elements[i-1].isnumeric():
                    column_boundaries.append(i)

        # Extract data based on identified column boundaries
        rows = []
        prev_boundary = 0
        for boundary in column_boundaries:
            row_data = elements[prev_boundary:boundary]
            rows.append(row_data)
            prev_boundary = boundary
        if prev_boundary < len(elements):
            row_data = elements[prev_boundary:]
            rows.append(row_data)

        # Create a DataFrame using the extracted data
        df = pd.DataFrame(rows).T

        # Export the DataFrame to Excel
        df.to_excel(output_file, index=False, header=False)
        print("Data exported to Excel successfully!")
    except requests.exceptions.RequestException as e:
        print("An error occurred with the request:", str(e))
    except Exception as e:
        print("An error occurred:", str(e))
        
# Example usage
url = "https://www.partsbigboss.in/brake"  # Replace with your desired URL
output_file = "output.xlsx"  # Replace with the desired output filename

export_data_to_excel(url, output_file)

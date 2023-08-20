import tkinter as tk
from tkinter import messagebox, filedialog
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

        # Prompt the user to select a file name and location
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx")

        if output_file:
            # Export the DataFrame to Excel
            df.to_excel(output_file, index=False, header=False)
            messagebox.showinfo("Success", "Data exported to Excel successfully!")
        else:
            messagebox.showwarning("Warning", "No file name selected.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "An error occurred with the request:\n" + str(e))
    except Exception as e:
        messagebox.showerror("Error", "An error occurred:\n" + str(e))

def export_button_click():
    url = url_entry.get()
    export_data_to_excel(url, "")

# Create the main window
window = tk.Tk()
window.title("Data Exporter")

# URL Entry
url_label = tk.Label(window, text="URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Export Button
export_button = tk.Button(window, text="Export", command=export_button_click)
export_button.pack()

# Run the main event loop
window.mainloop()
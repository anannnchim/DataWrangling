from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
class DataExtractor:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.table = None

    def fetch_page(self):
        try:
            page = urlopen(self.url)
            self.soup = BeautifulSoup(page, "html.parser")
        except Exception as e:
            print(f"An error occurred while fetching the page: {e}")

    def extract_table(self, table_index):
        if self.soup:
            try:
                tables = self.soup.find_all('table')
                if len(tables) < table_index:
                    print(f"Table index {table_index} is out of range.")
                    return
                self.table = tables[table_index]
            except IndexError:
                print(f"Table index {table_index} is out of range.")
        else:
            print("Soup object is None. Please fetch the page first.")

    def get_table_data(self):
        if self.table:
            rows = self.table.find_all('tr')
            table_data = []
            for row in rows:
                cells = row.find_all(['th', 'td'])
                row_data = [cell.get_text(strip=True) for cell in cells]
                table_data.append(row_data)
            return table_data
        else:
            print("Table object is None. Please extract the table first.")
            return None

    def display_table_data(self):
        table_data = self.get_table_data()
        if table_data:
            for row in table_data:
                print("\t".join(row))

    def to_dataframe(self):
        table_data = self.get_table_data()
        if table_data:
            header = table_data[0]
            data = table_data[1:]
            df = pd.DataFrame(data, columns=header)
            return df
        else:
            print("No table data available.")
            return None


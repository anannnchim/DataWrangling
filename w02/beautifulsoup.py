from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

if __name__ == "__main__":

    page = urlopen("https://en.wikipedia.org/wiki/States_and_territories_of_Australia")
    soup = BeautifulSoup(page, "html.parser")

    my_table = soup.find_all('table')[2]
    print(my_table)





from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

if __name__ == "__main__":

    page = urlopen("https://en.wikipedia.org/wiki/States_and_territories_of_Australia")
    soup = BeautifulSoup(page, "html.parser")

    my_table = soup.find_all('table')[2]




    A = [], B = []
    for row in my_table.find_all('tr'):
        col = row.find_all('td')
    if (len(col) > 0):
        A.append(col[1].find(text=True))
    B.append(col[5].find(text=True))
    df = pd.DataFrame(A, columns=['State'])
    df['Population'] = B
    print(df)


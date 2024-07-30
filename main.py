import pandas as pd
from data_extraction.data_extractor import DataExtractor
from data_quality_assessment.data_quality_checker import DataQualityChecker
import matplotlib.pyplot as plt

def main():

    # Input
    url = "https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?reportID=920&language=EN"
    table_index = 0

    # Extract data
    print("Extraction Process ---------------------------------")
    extractor = DataExtractor(url)
    extractor.fetch_page()
    extractor.extract_table(table_index)
    extractor.display_table_data()
    df = extractor.to_dataframe()

    # Quality Assessment
    print("Quality Assessment Process ---------------------------------")
    checker = DataQualityChecker(df)
    completeness = checker.calculate_completeness()
    print(completeness)

    # Data Profiling
    print("Data Profiling Process ---------------------------------")
    print(df.describe())
    df = df.iloc[1:] # remove the first row
    fig, ax = plt.subplots()
    ax.plot(df.iloc[:,0],df.iloc[:, 3])
    plt.show()



    #
    # import matplotlib.pyplot as plt
    # import numpy as np
    #
    # x = np.linspace(0, 2 * np.pi, 200)
    # y = np.sin(x)
    #
    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # plt.show()



if __name__ == "__main__":
    main()

import pandas as pd
from data_extraction.data_extractor import DataExtractor
from data_quality_assessment.data_quality_checker import DataQualityChecker
def main():

    # Input
    url = "https://app.bot.or.th/BTWS_STAT/statistics/BOTWEBSTAT.aspx?reportID=920&language=EN"
    table_index = 0

    # Extract data
    extractor = DataExtractor(url)
    extractor.fetch_page()
    extractor.extract_table(table_index)
    extractor.display_table_data()
    df = extractor.to_dataframe()

    # Quality Assessment
    checker = DataQualityChecker(df)
    completeness = checker.calculate_completeness()
    print(completeness)



if __name__ == "__main__":
    main()


class DataQualityChecker:

    def __init__(self, df):
        self.df = df
        self.completeness = None
        self.consistency = None
        self.uniqueness = None
        self.validity = None
        self.Accuracy = None
        self.Timeliness = None


    def calculate_completeness(self):
        """
        Calculate the completeness for each column in the DataFrame.
        Completeness is defined as the proportion of non-missing values.
        """
        total_records = len(self.df)
        completeness_dict = {}

        for column in self.df.columns:
            non_missing_values = self.df[column].notna().sum()
            completeness_percentage = (non_missing_values / total_records) * 100
            completeness_dict[column] = completeness_percentage

        self.completeness = completeness_dict
        return self.completeness




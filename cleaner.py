class DataCleaner:
    def clean(self, df):
        df_cleaned = df.dropna()
        df_cleaned = df_cleaned.drop_duplicates()
        print(f"Remaining rows: {len(df_cleaned)}")
        return df_cleaned
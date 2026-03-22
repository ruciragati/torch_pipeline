from loader import DataLoader
from cleaner import DataCleaner
from transformer import DataTransformer

def run_pipeline():
    loader = DataLoader("data.csv")
    cleaner = DataCleaner()
    transformer = DataTransformer()

    raw_df = loader.load_data()
    
    if raw_df is not None:
        clean_df = cleaner.clean(raw_df)
        final_tensor = transformer.to_tensor(clean_df)
        
        print("\nFinal Tensor Result:")
        print(final_tensor)

run_pipeline()
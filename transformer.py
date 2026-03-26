import torch
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

class DataTransformer:
    def __init__(self):
        self.encoders = {}

    def to_tensor(self, df):
        try:
            df_numeric = df.copy()
            
            for column in df_numeric.columns:
                if not pd.api.types.is_numeric_dtype(df_numeric[column]):
                    le = LabelEncoder()
                    df_numeric[column] = le.fit_transform(df_numeric[column].astype(str))
                    self.encoders[column] = le
            
            numeric_array = df_numeric.to_numpy(dtype=np.float32)
            
            tensor_data = torch.from_numpy(numeric_array)
            
            print(f"Tensor Shape: {tensor_data.shape}")
            return tensor_data
            
        except Exception as e:
            print(f"Error: {e}")
            return None
        
# comment 
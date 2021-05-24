import numpy as np
import pandas as pd

def find_missing(data, normalized=False, missing_values=[]): 
    
    if missing_values: 
        try: 
            for value in missing_values: 
                data = data.replace(value, np.nan)
        except TypeError: 
            raise Exception("missing_values not a list")
            
    missing_data = data.isnull().sum().sort_values(ascending=False)

    if normalized:
        missing_data = missing_data / len(data)

    return missing_data    
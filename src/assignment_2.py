import pandas as pd
import numpy as np

def calculate_total_spending(df: pd.DataFrame) -> pd.DataFrame:
    cols = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    
    df['TotalSpending'] = df[cols].fillna(0).sum(axis=1)
    
    return df

def parse_cabin(df: pd.DataFrame) -> pd.DataFrame:
    cabin_split = df['Cabin'].str.split('/', expand=True)
    
    df['Deck'] = cabin_split[0]
    df['CabinNum'] = pd.to_numeric(cabin_split[1])
    df['Side'] = cabin_split[2]
    
    return df


def filter_outliers_iqr(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    q1 = df[column_name].quantile(0.25)
    q3 = df[column_name].quantile(0.75)
    
    iqr = q3 - q1
    
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    
    mask = (df[column_name] >= lower) & (df[column_name] <= upper)

    return df.loc[mask].copy()


if __name__ == "__main__":
    print("Assignment 2 ready")

    # Test your logic here
    try:
        # Assuming assignment_1.py functions are used or mock data is loaded
        print("Assignment 2 template ready for implementation.")
    except Exception as e:
        print(f"Error: {e}")


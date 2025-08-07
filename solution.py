import pandas as pd
import numpy as np
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    
    #Input error handling
    if not isinstance(df, pd.DataFrame):
        return pd.DataFrame([])
    
    if new_column in df.columns:
        return pd.DataFrame([])
    
    if not re.match(r"^[A-Za-z_]+$", new_column):
        return pd.DataFrame([])
    
    role = role.strip().replace(' ', '')
    role_match = re.match(r"^([A-Za-z_]+)([+\-*])([A-Za-z_]+)$", role)
    if not role_match:
        return pd.DataFrame([])
    
    col1, operator, col2 = role_match.groups()

    if col1 not in df.columns or col2 not in df.columns:
        return pd.DataFrame([])
    
    if not np.issubdtype(df[col1].dtype, np.number) or not np.issubdtype(df[col2].dtype, np.number):
        return pd.DataFrame([])

    #Function logic
    df = df.copy()

    if operator == '+':
        df[new_column] = df[col1] + df[col2]
    elif operator == '-':
        df[new_column] = df[col1] - df[col2]
    elif operator == '*':
        df[new_column] = df[col1] * df[col2]
    else:
        return pd.DataFrame()
    # Optional printing - can be safely removed if not necessary
    print(df)
    return df


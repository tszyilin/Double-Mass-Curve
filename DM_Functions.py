
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import io

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df


def extract_station_number(file_name):
    station_number = file_name.split('_')[1]
    return station_number

def set_up_template_dataframe():
    date_range = pd.date_range(start="1800-01-01", end=pd.Timestamp.today(), freq='D').date
    df = pd.DataFrame(date_range, columns=['Date'])
    return df


def drop_columns(columns_name_list, df):
    df.drop(columns=columns_name_list, inplace=True)
    return df


def read_column_name(df):
    column_name = df.columns.tolist()
    return column_name

def turn_into_date(df):
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']]).dt.date
    
    # Move to the fourth column
    cols = list(df.columns)
    cols.insert(3, cols.pop(cols.index('Date')))
    df = df[cols]
    
    return df


def rename_column(df, rename_dict):
    df.rename(columns=rename_dict, inplace=True)
    

def drop_nan_row(df, column_list):
    df.dropna(subset=column_list, inplace=True)
    

def cumulative_column(df, column_str):
    column_name = 'Cumulative ' + column_str
    df[column_name] = df[column_str].cumsum()
    

def regression(df, x_column, y_column):
    slope, intercept = np.polyfit(df[x_column], df[y_column], 1)
    
    regression_line = slope * df[x_column] + intercept
    
    return slope, intercept, regression_line
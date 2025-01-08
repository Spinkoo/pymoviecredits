from pandas import read_csv, read_excel
import pandas as pd

def read_credits_from_csv(csv_file_path):
    """
    Reads credits from a CSV file and returns a dictionary.
    CSV should have two columns: 'Title' and 'Name'
    
    Args:
        csv_file_path (str): Path to the CSV file
    
    Returns:
        dict: Credits dictionary with titles as keys and names as values
    """
    try:
        df = read_csv(csv_file_path)
        # Convert DataFrame to dictionary, fill NaN with empty string
        credits_dict = dict(zip(df['Title'], df['Name'].fillna('')))
        return credits_dict
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return {}

def read_credits_from_excel(excel_file_path, sheet_name=0):
    """
    Reads credits from an Excel file and returns a dictionary.
    Excel should have two columns: 'Title' and 'Name'
    
    Args:
        excel_file_path (str): Path to the Excel file
        sheet_name: Name or index of the sheet (default is first sheet)
    
    Returns:
        dict: Credits dictionary with titles as keys and names as values
    """
    try:
        df = read_excel(excel_file_path, sheet_name=sheet_name)
        # Convert DataFrame to dictionary, fill NaN with empty string
        credits_dict = dict(zip(df['Title'], df['Name'].fillna('')))
        return credits_dict
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return {}
    
def read_credits_static():
        
    # Example usage
    return {
        "Directors": "",
        "Producer": "Spinkoo",
        "First Assistant Director": "Tyrion Lannister",
        "Second Assistant Director": "Chatgpt..",
        "CAST": "",
        "The Bar": "Y",
        "The legs by the start of the video": "Stephen H's",
        "CAMERA":"",
        "Camera Operator":"Bottle of water",
        "HAIR":"",
        "Hair Department Head":"Neighbourhood barber",
        "DIRECTOR THANKS":"",
        "The Director Wishes to Thank":"Git community",
    }

# Example usage:
# credits = read_credits_from_csv('credits.csv')
# credits = read_credits_from_excel('credits.xlsx')
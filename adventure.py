"""
Adventure Parser - The Lost Temple of Data
"""

import re
import pandas as pd

def load_artifact_data(excel_filepath):
    """
    Reads artifact data from a specific sheet ('Main Chamber') in an Excel file,
    skipping the first 3 rows.

    Args:
        excel_filepath (str): The path to the artifacts Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the artifact data.
    """
    return pd.read_excel(excel_filepath, sheet_name='Main Chamber', skiprows=3)

def load_location_notes(tsv_filepath):
    """
    Reads location data from a Tab-Separated Value (TSV) file.

    Args:
        tsv_filepath (str): The path to the locations TSV file.

    Returns:
        pandas.DataFrame: DataFrame containing the location data.
    """
    return pd.read_csv(tsv_filepath, sep='\t')

def extract_journal_dates(journal_text):
    """
    Extracts all valid dates in MM/DD/YYYY format from the journal text.

    Only includes dates where:
    - MM is 01–12
    - DD is 01–31
    - YYYY is any 4-digit year

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of valid date strings found in the text.
    """
    pattern = r'\b(?:0[1-9]|1[0-2])/(?:0[1-9]|[12][0-9]|3[01])/\d{4}\b'
    return re.findall(pattern, journal_text)


def extract_secret_codes(journal_text):
    """
    Extracts all secret codes in AZMAR-XXX format (XXX are digits) from the journal text.

    Args:
        journal_text (str): The full text content of the journal.

    Returns:
        list[str]: A list of secret code strings found in the text.
    """
    return re.findall(r'AZMAR-\d{3}', journal_text)

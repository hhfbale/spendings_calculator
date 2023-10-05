import csv
from dotenv import load_env
load_dotenv
import os

trigger1 = os.environ.get('TRIG1')
trigger2 = os.environ.get('TRIG2')

def spendings_from_csv():
    """
    Reads a transaction log from csv file and calculates the spendings.
    
    Assumptions:
        - CSV file has field 'Beskrivelse' for trancsaction description and 'Beløp' for amount.
        - CSV uses semicolon as delimiter.
    """

    total = 0.0

    #Change to your desired path
    file_name = "transaksjoner.csv"

    try:
        with open(file_name, 'r', encoding='utf-8-sig') as file:
            data = csv.DictReader(file, delimiter=';')
            for row in data:
                description = row['Beskrivelse']
                amount = row['Beløp'].replace(',','.')
                if should_be_ignored(description):
                    continue
                total += float(amount)
        print(round(total,2))
    except IOError:
        print('Could not read file')

def should_be_ignored(desc):
    """
    Decides wether a transaction should be ignored based on a trigger in the description.
    """
    ignore = [trigger1, trigger2]
    for trigger in ignore:
        if trigger in desc:
            return True
    return False


import os
import tradingeconomics as te
import pandas as pd

def get_clean_data(country, indicator, initDate, value_name, filename):


    # te.login(api_key)
    te.login()

    columns = ["Country", "Category", "Frequency", "HistoricalDataSymbol", "LastUpdate"]
    if os.path.exists(filename):
        print(f"Loading data from {filename}...")
        df = pd.read_csv(filename)
        df['DateTime'] = pd.to_datetime(df['DateTime'], errors='coerce')  # Ensure datetime format
    else:
        print(f"Fetching data from API for {indicator}...")
        try:
            # Attempt to fetch data from the API
            df = te.getHistoricalData(country=country, indicator=indicator, initDate=initDate, output_type='df')
            df.rename(columns={"Value": value_name}, inplace=True)
            df.drop(columns=columns, axis=1, inplace=True)

            # Clean problematic DateTime values
            df['DateTime'] = df['DateTime'].str.split('.').str[0]  # Drop microseconds and timezone
            df['DateTime'] = df['DateTime'].str.replace('T', ' ')  # Replace 'T' with space for odd first row
            df['DateTime'] = pd.to_datetime(df['DateTime'], errors='coerce')

            # Save to CSV
            df.to_csv(filename, index=False)
            print(f"Data saved to {filename}")

        except Exception as e:
            print(f"Error occurred while fetching data: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

    return df
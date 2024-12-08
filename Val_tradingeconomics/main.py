from data import get_clean_data
from plotter import plot
import pandas as pd

def run_indicators():

    initDate = '2015-01-01'
    # File paths to save data
    MXNUSD_file = 'MXNUSD_data.csv'
    MXN_10year_file = 'MXN_10year.csv'

    # Fetch or load data
    MXNUSD = get_clean_data(country='Mexico',
                            indicator='Currency',
                            initDate=initDate,
                            value_name='MXNUSD',
                            filename=MXNUSD_file)
    MXN_10year = get_clean_data(country='Mexico',
                                indicator='Government Bond 10Y',
                                initDate=initDate,
                                value_name='Government Bond 10Y',
                                filename=MXN_10year_file)

    MXNUSD_10year_df = pd.merge(MXNUSD, MXN_10year, on='DateTime', how='inner')

    plot(MXNUSD_10year_df)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_indicators()

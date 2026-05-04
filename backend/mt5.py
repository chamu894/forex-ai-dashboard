import MetaTrader5 as mt5
import pandas as pd

def get_market_data():
    mt5.initialize()

    rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1, 0, 200)

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')

    return df
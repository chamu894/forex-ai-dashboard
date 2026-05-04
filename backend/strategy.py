import ta

def generate_signal(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()

    last_rsi = df['rsi'].iloc[-1]

    if last_rsi < 30:
        return "BUY"
    elif last_rsi > 70:
        return "SELL"
    else:
        return "WAIT"
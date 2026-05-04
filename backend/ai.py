import requests

def ask_ai(df):
    rsi = df['close'].iloc[-1]

    prompt = f"""
    You are a Forex expert.

    Current RSI: {rsi}

    Give short analysis and confirm BUY/SELL/WAIT.
    """

    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.1:8b",
        "prompt": prompt,
        "stream": False
    })

    return res.json()['response']
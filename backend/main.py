from fastapi import FastAPI
from mt5 import get_market_data
from strategy import generate_signal
from ai import ask_ai

app = FastAPI()

@app.get("/signal")
def get_signal():
    df = get_market_data()

    signal = generate_signal(df)

    ai_response = ask_ai(df)

    return {
        "signal": signal,
        "ai": ai_response
    }
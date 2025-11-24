from pandas import DataFrame

from app.stocks import fetch_stocks_csv


def test_fetch_data():
    df = fetch_stocks_csv("NFLX")
    assert isinstance(df, DataFrame)
    assert "adjusted_close" in df.columns
    assert "timestamp" in df.columns
import pandas as pd 
import streamlit as st
import yfinance as yf


st.write(
    """
    # Stock price analyzer

    shown apple stock prices
    """
)

ticker_symbol='AAPL'

#getting date inputs from the user


ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="max", start='2019-01-01',end='2026-06-26')

st.dataframe(ticker_df) 

## showcasing charts

st.write(""" # Daily Closing price chart 
         """)

st.line_chart(ticker_df.Close)

st.write(""" # Daily Volume traded 
         """)

st.line_chart(ticker_df.Volume)
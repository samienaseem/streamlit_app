import pandas as pd 
import streamlit as st
import yfinance as yf
import datetime


st.write(
    """
    # Stock price analyzer

    shown apple stock prices
    """
)


ticker_symbol=st.text_input("Enter Stock symbol", "AAPL", key='placeholder')

# ticker_symbol='AAPL'

col1,col2=st.columns(2)



#getting date inputs from the user
with col1:
    start_date=st.date_input("Input starting date", datetime.date(2019,1,1))
with col2:
    end_date=st.date_input("Input Ending date", datetime.date(2026,12,31))


ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(period="max", start=f"{start_date}",end=f"{end_date}")

st.write(f"""
### {ticker_symbol}'s EOD prices """)

st.dataframe(ticker_df) 

## showcasing charts

st.write(""" # Daily Closing price chart 
         """)

st.line_chart(ticker_df.Close)

st.write(""" # Daily Volume traded 
         """)

st.line_chart(ticker_df.Volume)
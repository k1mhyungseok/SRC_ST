import yfinance as yf
import streamlit as st


st.sidebar.header('Input Stock id')

form=st.sidebar.form(key='my_form')
name=form.text_input('Enter stock name')
submit=form.form_submit_button('Submit')
if submit:
    st.title(name)

exp = st.expander("Stock info")

tickerData = yf.Ticker(name)
exp.write(tickerData.info)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-6-30')


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
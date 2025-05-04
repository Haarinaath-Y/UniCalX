import streamlit as st
from currencyconverter.currencyconverter import CurrencyConverter
from currencyconverter.currencyconverterui import CurrencyConverterUI

title = "️‍Currency"
st.set_page_config(
    page_title=f'{title} Converter'
)

def currency_converter():
    # Initialize the converter with your API key
    api_key=st.secrets["currency"]["api_key"]
    converter = CurrencyConverter(api_key=api_key)
    currency_converter_ui = CurrencyConverterUI(converter, title=title)
    converter.update_rates()
    currency_converter_ui.display_currency_converter()

if __name__ == "__main__":
    currency_converter()



import streamlit as st


class CurrencyConverterUI:
    def __init__(self, converter, title):
        self.converter = converter
        self.title = title

    def display_currency_converter(self):
        st.header(f"💱 {self.title} Converter")

        # Fetch available currencies
        currencies = list(self.converter.rates.keys())

        # User inputs
        amount = st.number_input("Enter amount:", min_value=0.0, value=1.0)
        from_currency = st.selectbox("From Currency:", currencies, index=currencies.index("USD"))
        to_currency = st.selectbox("To Currency:", currencies, index=currencies.index("EUR"))

        # Perform conversion
        if st.button("Convert"):
            try:
                converted_amount = self.converter.convert(amount, from_currency, to_currency)
                st.success(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
            except Exception as e:
                st.error(f"Error: {e}")

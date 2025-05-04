import requests
import streamlit as st

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.currencyfreaks.com/latest"
        self.rates = {}  # Initialize rates as an empty dictionary

    @staticmethod
    @st.cache_data(ttl=3600)
    def fetch_live_rates(api_url, api_key):
        try:
            response = requests.get(f"{api_url}?apikey={api_key}")
            response.raise_for_status()
            data = response.json()
            return data.get("rates", {})  # Return rates directly
        except Exception as e:
            raise RuntimeError(f"Failed to fetch live currency rates: {e}")

    def update_rates(self):
        # Fetch and store rates in the instance attribute
        self.rates = self.fetch_live_rates(self.api_url, self.api_key)

    def convert(self, amount, from_currency, to_currency):
        if not self.rates:
            raise ValueError("Currency rates are not available. Please update rates first.")
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Invalid currency code.")
        from_rate = float(self.rates[from_currency])
        to_rate = float(self.rates[to_currency])
        return amount * (to_rate / from_rate)
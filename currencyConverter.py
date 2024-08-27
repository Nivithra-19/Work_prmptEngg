import requests

API_KEY = "5f35b593b85a995dc9ee52e6"  
BASE_URL = "https://api.exchangerate-api.com/v4/latest/"

def get_exchange_rates(base_currency):
    url = BASE_URL + base_currency
    response = requests.get(url)
    data = response.json()
    return data['rates']

def currency_converter():
    currencies = {
        "ZAR": "South African Rand",
        "CNY": "Chinese Yuan",
        "USD": "US Dollar",
        "GBP": "British Pound Sterling",
        "INR": "Indian Rupee"
    }

    print("Available currencies:")
    for code, name in currencies.items():
        print(f"{code}: {name}")

    from_currency = input("Enter the currency code you're converting from: ").upper()
    to_currency = input("Enter the currency code you're converting to: ").upper()

    if from_currency not in currencies or to_currency not in currencies:
        print("Invalid currency code. Please try again.")
        return

    amount = float(input(f"Enter the amount in {currencies[from_currency]}: "))

    rates = get_exchange_rates(from_currency)

    if to_currency in rates:
        rate = rates[to_currency]
        converted_amount = amount * rate
        print(f"{amount} {currencies[from_currency]} = {converted_amount:.2f} {currencies[to_currency]}")
    else:
        print("Unable to fetch exchange rate. Please try again later.")

if __name__ == "__main__":
    currency_converter()
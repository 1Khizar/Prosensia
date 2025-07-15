import requests

url ='https://api.exchangerate-api.com/v4/latest/USD'

try:
    response = requests.get(url)
    data = response.json()
    
    base = data['base']
    result =data['rates']
    
    selected_currencies = ["PKR", "EUR", "GBP"]

    print(f"Exchange Rate Report (Base: {base})")
    for currency in selected_currencies:
        print(f"{currency} :  {result[currency]}")
    
    with open(r'Day_13_Task\btc_price_report.txt', 'w') as file:
        file.write(f"Exchange Rate Report (Base: {base})\n")
        for currency in selected_currencies:
            file.write(f"{currency} :  {result[currency]}\n")
    
except Exception as e:
    print('Error fetching data : ', e)
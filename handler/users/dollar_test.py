import requests  # API (internet orqali ma'lumot olish) bilan ishlash uchun `requests` kutubxonasini import qilamiz

API_KEY = "88fbb07fc673850d9416f2f1"
currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
json_data = response.json()
kurs = json_data['conversion_rate']


import smtplib
import requests
from bs4 import BeautifulSoup
my_email = "your email"
password = "your email password"
PRICE_OK = 100
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
}
response = requests.get(url=AMAZON_URL, headers=header)
webpage = response.text
soup = BeautifulSoup(webpage, 'lxml')
price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
print(price)
if price < PRICE_OK:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Amazon rice cooker\n\nNow there is great price to by rice cooker"
                                                                       f", only for {price}")
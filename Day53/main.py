import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
DIRE = r'direction to firefix profile'
LINK_TO_FORM = 'Link to form'
URL_ZILLOW = 'https://appbrewery.github.io/Zillow-Clone/'
EMAIL = 'email'
response = requests.get(url=URL_ZILLOW)
zillow_page = response.text
soup = BeautifulSoup(zillow_page, 'html.parser')
all_cost = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
all_addre = soup.find_all(name='address')
al_links = soup.find_all(name="div", class_='StyledPropertyCardDataWrapper')
cost_list = []
addre_list = []
link_list = []

for item in all_cost:
    cost_list.append(item.getText().replace("+", " ").replace('/', ' ').split()[0])

for item in all_addre:
    addre_list.append((' '.join(item.getText().split())).replace('|', '').replace('  ', ' '))

for item in al_links:
    link_list.append(item.a.get('href'))


driver = webdriver.Firefox()
driver.get(LINK_TO_FORM)
time.sleep(4)
for x in range(0, len(link_list)):
    driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(addre_list[x])
    driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(cost_list[x])
    driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(link_list[x])
    driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    time.sleep(2)

options = Options()
options.add_argument('--profile')
options.add_argument(DIRE)
driver = webdriver.Firefox(options=options)
driver.get("link to forms answer")
time.sleep(3)
driver.find_element(By.XPATH, value='/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div').click()
time.sleep(3)
driver.find_element(By.XPATH, value='/html/body/div[14]/div/div[2]/div[3]/div[2]').click()
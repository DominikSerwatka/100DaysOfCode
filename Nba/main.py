from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

def get_all_players():
    driver.get("https://www.nba.com/players")
    time.sleep(6)
    driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]').click()
    time.sleep(2)
    # driver.find_element(By.XPATH, value='//*[@id="__next"]/div[2]/div[2]/main/div[2]/section/div/div[2]/div[1]/div[7]/div/div[3]/div/label/div/select').click()
    driver.find_element(By.XPATH, value='//*[@id="__next"]/div[2]/div[2]/main/div[2]/section/div/div[2]/div[1]/div[7]/div/div[3]/div/label/div/select/option[1]').click()
    time.sleep(2)
    all_players = driver.find_elements(By.CSS_SELECTOR, value='.players-list tr')

    for n in range(1, len(all_players)):
        print(all_players[n].text.split())

def get_all_palyers_with_stats():
    driver.get('https://www.nba.com/stats/leaders')
    time.sleep(5)
    driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, value='//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select/option[1]').click()
    time.sleep(3)
    all_players = driver.find_elements(By.CSS_SELECTOR, value='.Crom_body__UYOcU tr')
    print(all_players[1].text.split())
    with open("players.txt", mode="w") as file:
        for n in range(0, len(all_players)):
            file.write(f'{all_players[n].text.split()[1]},{all_players[n].text.split()[2]},'
                       f'{all_players[n].text.split()[3]},{all_players[n].text.split()[6]},'
                       f'{all_players[n].text.split()[18]},{all_players[n].text.split()[19]},#\n')

get_all_palyers_with_stats()
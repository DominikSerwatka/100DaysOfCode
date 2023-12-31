from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')
start_game = time.time()
start = time.time()
while True:
    cookie.click()
    end = time.time()
    x = end - start
    if (end - start_game) > 5*60:
        result = driver.find_element(By.ID, value="cps")
        print(result.text)
        break
    if x >= 1:
        cookie.click()
        start = time.time()
        num_of_cookies = int(driver.find_element(By.ID, value='money').text)
        store = driver.find_elements(By.CSS_SELECTOR, value="#store div  b ")
        max = 0
        num = 0
        for n in range(0, len(store)-1):
            cost = int(store[n].text.split("\n")[0].split(" - ")[1].replace(',', ''))
            if cost > max and cost <= num_of_cookies:
                max = cost
                num = n
        if max != 0:
            store[num].click()






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time
SIMILAR_ACCOUNT = 'chefsteps'
USERNAME = 'insta name'
PASSWORD = 'insta password'
EMAIL = 'insta email'


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(3)
        self.driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click()
        self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(USERNAME)
        self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(7)
        button = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Zapisz informacje')]")
        button.click()
        time.sleep(3)
        button_two = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Nie teraz')]")
        button_two.click()

    def find_followers(self):
        self.driver.get('https://www.instagram.com/chefsteps/followers/')
        time.sleep(4)

        path = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        '/html/body/div[6]/div[1]/div/div[2]/div/div/div'
        '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div'
        '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]'
        modal = self.driver.find_element(By.XPATH, value=path)
        for n in range(0, 5):
            time.sleep(3)
            self.follow(n)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

    def follow(self, number):
        for n in range(0, 6):
            path = f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{number*6+n+1}]/div/div/div/div[3]/div/button'
            try:
                self.driver.find_element(By.XPATH, value=path).click()
            except ElementClickInterceptedException:
                self.driver.find_element(By.XPATH, value='/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]').click()
                self.driver.find_element(By.XPATH, value=path).click()
            time.sleep(2)


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()

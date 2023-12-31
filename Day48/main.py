from selenium import webdriver
from selenium.webdriver.common.by import By
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com")
# driver.get(AMAZON_URL)
# driver.implicitly_wait(10)
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


# events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
# print(events[0].text.split('\n'))
#
# event_dict = {}
# iter = 0
# for event in events:
#     x = event.text.split("\n")
#     event_dict[f'event{iter}'] = {"time": x[0],
#                                   "name": x[1]
#                                   }
#     iter += 1
# print(event_dict)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for time in event_times:
    print(time.text)
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for name in event_name:
    print(name.text)
events = {}
for n in range(0, len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_name[n].text,
    }
print(events)
# close one chrome tab
# driver.close()
# close all chrome tabs
driver.quit()

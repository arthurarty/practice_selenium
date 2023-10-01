"""
Run a search on duckduckgo.
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
driver.implicitly_wait(10)
# fill in form and wait press return
search_box = driver.find_element(By.ID, 'searchbox_input')
search_box.send_keys("realpython")
search_box.send_keys(Keys.RETURN)
# wait for page to load
driver.implicitly_wait(10)
sleep(5)
result_list = driver.find_element(By.CSS_SELECTOR, 'ol.react-results--main')
result_list_items = result_list.find_elements(By.TAG_NAME, 'li')
for li in result_list_items:
    print(li.text)
sleep(5)

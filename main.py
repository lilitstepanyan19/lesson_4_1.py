from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

browser = webdriver.Chrome()
browser.get(link)

LOGIN_LINK = browser.find_element(By.CSS_SELECTOR, '#login_link')
LOGIN_LINK.click()

# browser.quit()
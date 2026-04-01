import time
import math

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Создаем опции браузера
options = Options()
options.page_load_strategy = 'normal'  # 'normal', 'eager' или 'none'

# Явно указываем путь к драйверу
service = Service(executable_path=r"C:\chromedriver\chromedriver.exe")
time.sleep(5)

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(service=service, options=options)
    browser.get("http://suninjuly.github.io/wait1.html")
    time.sleep(5)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
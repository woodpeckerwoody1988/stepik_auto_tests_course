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
    browser.get(link)
    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #confirm = browser.switch_to.alert
    #confirm.accept()

    value = browser.find_element(By.ID, "input_value").text

    def calc(value):
        return str(math.log(abs(12*math.sin(int(value)))))

    browser.find_element(By.ID, "answer").send_keys(calc(value))
   
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
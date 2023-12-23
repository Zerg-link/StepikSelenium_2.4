from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    book_button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button.click()

    submit_button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)

    submit_button.click()

    # выводим информацию из алерта
    alert = browser.switch_to.alert
    alert_resp = alert.text
    alert_resp1 = alert_resp.split(': ')[-1]
    print('ответ из алерта - ', alert_resp)
    print('ответ из алерта только цифры - ', alert_resp1)
    time.sleep(4)
    alert.accept()

finally:
    time.sleep(6)
    browser.quit()

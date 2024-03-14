import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Ініціалізація драйвера браузера
driver = webdriver.Chrome()

# URL початкової сторінки з меню
url = 'http://localhost:8080/dz.html'
driver.get(url)

# frame1 = driver.find_element(By.ID, 'frame1')
# frame2 = driver.find_element(By.ID, 'frame2')
# driver.switch_to.frame(frame1)
# input1 = driver.find_element(By.ID, 'input1')
# input1.send_keys('Frame1_Secret')
# time.sleep(4)
# button1 = driver.find_element(By.TAG_NAME, 'button')
# button1.click()
# WebDriverWait(driver, 5).until(EC.alert_is_present())
# alert = driver.switch_to.alert
# # Верифікація пройшла успішно!
# assert alert.text == 'Верифікація пройшла успішно!', 'Wrong secret'
# time.sleep(2)
# alert.accept()
# time.sleep(2)
#
# driver.switch_to.default_content()
# driver.switch_to.frame(frame2)
# input2 = driver.find_element(By.ID, 'input2')
# input2.send_keys('Frame2_Secret')
# time.sleep(4)
# button1 = driver.find_element(By.TAG_NAME, 'button')
# button1.click()
# WebDriverWait(driver, 5).until(EC.alert_is_present())
# alert = driver.switch_to.alert
# # Верифікація пройшла успішно!
# assert alert.text == 'Верифікація пройшла успішно!', 'Wrong secret'
# time.sleep(2)
# alert.accept()
# time.sleep(2)
# driver.quit()


# Перебір пунктів меню
for i in range(1, 3):

    # Перемикаємося до фрейму
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.ID, f'frame{i}'))

    # Знаходження поля вводу та кнопки в фреймі
    input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    input_field.clear()
    input_field.send_keys(f'Frame{i}_Secret')
    time.sleep(1)

    submit_button = driver.find_element(By.CSS_SELECTOR, 'button')
    submit_button.click()
    time.sleep(1)

    # Очікування діалогового вікна та його закриття
    alert = Alert(driver)
    alert_text = alert.text
    if alert_text == "Верифікація пройшла успішно!":
        print(f"Підтверджено, що Frame{i} верифікація пройшла успішно")
    else:
        print("Помилка: неправильний текст в діалоговому вікні")
    alert.accept()

    # Перехід назад до основного фрейму
    driver.switch_to.default_content()

# Закриття драйвера
driver.quit()

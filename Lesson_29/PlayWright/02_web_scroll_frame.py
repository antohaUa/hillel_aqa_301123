from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://localhost:8080/scroll_frame.html")

    # Знаходимо елемент scrollbar на сторінці
    scrollbar = page.query_selector('div[style="height: 1000px; background-color: #f0f0f0;"]')
    time.sleep(2)

    # Прокрутка вниз
    page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Прокрутка вгору
    page.evaluate("window.scrollTo(0, 0);")
    time.sleep(1)

    # Переходимо у фрейм
    frame = page.frame(name='myFrame')

    if frame:
        # Проверяем наличие кнопки внутри фрейма
        button = frame.query_selector("#myButton")
        if button:
            # Натискаємо кнопку три рази
            for _ in range(3):
                button.click()
                time.sleep(1)  # Даємо час для реакції на натискання кнопки
        else:
            print("Button not found")
    else:
        print("Frame not found")

    browser.close()

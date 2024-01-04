import time
from playwright.sync_api import Playwright, sync_playwright

WAIT_TIME = 2


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.ukrposhta.ua/ua")
    page.locator("#bottom-line").get_by_role("link", name="Відділення").click()
    time.sleep(WAIT_TIME)
    page.get_by_placeholder("Введіть населений пункт або індекс").click()
    time.sleep(WAIT_TIME)
    page.get_by_placeholder("Введіть населений пункт або індекс").fill("Шепет")
    time.sleep(WAIT_TIME)
    page.get_by_role("button", name="").click()
    time.sleep(WAIT_TIME)
    page.get_by_role("button", name="м. Шепетівка, Шепетівський р-н, Хмельницька обл").click()
    time.sleep(WAIT_TIME)
    page.locator("#map").get_by_role("img").first.click()
    page.get_by_label("Zoom in").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

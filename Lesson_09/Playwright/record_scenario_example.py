"""
Example how to record FE scenario

playwright codegen demo.playwright.dev/todomvc
"""
import time
from playwright.sync_api import Playwright, sync_playwright, expect

WAIT_TIME = 2


def run(pw: Playwright) -> None:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/")
    time.sleep(WAIT_TIME)
    page.get_by_placeholder("What needs to be done?").click()
    time.sleep(WAIT_TIME)
    page.get_by_placeholder("What needs to be done?").fill("Search")
    time.sleep(WAIT_TIME)
    page.get_by_placeholder("What needs to be done?").press("Enter")
    time.sleep(WAIT_TIME)
    page.get_by_placeholder("What needs to be done?").fill("Test")
    time.sleep(WAIT_TIME)
    page.get_by_placeholder("What needs to be done?").press("Enter")
    time.sleep(WAIT_TIME)
    page.get_by_role("link", name="Completed").click()
    time.sleep(WAIT_TIME)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

import re
import time

import pytest
from playwright.sync_api import sync_playwright

CONTENT_LOAD_TIMEOUT = 2
RECORDS_COUNT = 4
UKR_CAP_LETTERS = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'"
EXPECTED_EXP = 5


class TestDobrobut:

    @pytest.fixture(scope="class")
    def page(self):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            context = browser.new_context()
            pw_page = context.new_page()
            yield pw_page
            context.close()
            browser.close()

    def test_xray_dep(self, page):
        page.goto("https://dobrobut.com/ua")
        page.get_by_role("banner").locator("li").filter(has_text=re.compile(r"^Лікарі$")).get_by_role("link").click()
        page.get_by_text("Рентгенологія").click()
        time.sleep(CONTENT_LOAD_TIMEOUT)
        doctors_info = {}
        doctors = page.locator(".doctor")
        for idx in range(RECORDS_COUNT):
            curr_name = doctors.locator('.doctor__name').nth(idx).inner_text()
            curr_exp = doctors.locator('.exp__top').nth(idx).inner_text()
            doctors_info[curr_name] = curr_exp
        print('\n')

        for curr_name, curr_exp in doctors_info.items():
            s1 = set(curr_name.replace(' ', ''))
            s2 = set(UKR_CAP_LETTERS)
            print(f'{curr_name}: {curr_exp}')
            assert len(s1 - s2) == 0, f'"{curr_name}" has non capital ukr letters'
            assert int(curr_exp) >= EXPECTED_EXP
        print('-' * 20)
        print('All checks passed')

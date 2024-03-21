import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from conftest_plugin import Cfg

_log = logging.getLogger('Main')
WEB_BASE_URL = Cfg.params.get('web_base_url', 'http://localhost:8000')


@pytest.mark.web_selenium
class TestWebSelenium:

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome()
        url = f'{WEB_BASE_URL}/dz.html'
        driver.get(url)
        yield driver
        driver.quit()

    @pytest.fixture(scope='function', autouse=True)
    def switch_to_main_content(self, driver):
        yield
        _log.debug('Switching to default content')
        driver.switch_to.default_content()

    @staticmethod
    def _input_in_frame_secret(driver, frame_id):
        frame = driver.find_element(By.ID, f'frame{frame_id}')
        driver.switch_to.frame(frame)
        input_frm = driver.find_element(By.ID, f'input{frame_id}')
        input_frm.send_keys(f'Frame{frame_id}_Secret')
        button = driver.find_element(By.TAG_NAME, 'button')
        button.click()
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        return alert

    def test_frame1_positive_check(self, driver):
        alert = self._input_in_frame_secret(driver=driver, frame_id=1)
        assert alert.text == 'Верифікація пройшла успішно!', 'Wrong secret'
        alert.accept()

    def test_frame1_negative_check(self, driver):
        alert = self._input_in_frame_secret(driver=driver, frame_id=1)
        assert alert.text == 'Введено неправильний текст!', 'Correct secret'
        alert.accept()

    def test_frame2_positive_check(self, driver):
        alert = self._input_in_frame_secret(driver=driver, frame_id=2)
        assert alert.text == 'Верифікація пройшла успішно!', 'Wrong secret'
        alert.accept()

    def test_frame2_negative_check(self, driver):
        alert = self._input_in_frame_secret(driver=driver, frame_id=2)
        assert alert.text == 'Введено неправильний текст!', 'Correct secret'
        alert.accept()

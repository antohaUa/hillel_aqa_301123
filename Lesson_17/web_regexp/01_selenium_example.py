"""
Web data parsing example:

https://www.selenium.dev/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
import re
import json
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time

# Set up the Selenium WebDriver (make sure to replace the path with the location of your webdriver executable)
driver = webdriver.Chrome()

# Open the HTML page in the browser
driver.get('http://localhost/tt/purchase.html')
purchase_json = '/absolute_path_to_dir/web_regexp/purchase_data.json'
color = {'V': 'violet', 'O': 'orange', 'Y': 'yellow'}

try:
    # Wait for the form elements to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'buyDate')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'buyAmount')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'buyModel')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'buyDescription')))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Add Buy"]')))

    with open(purchase_json, 'rt') as data_fh:
        purchase_data = json.load(data_fh)

    # Input data into the form
    for model, descr in purchase_data.items():
        driver.find_element(By.ID, 'buyDate').send_keys('01-02-2024')
        driver.find_element(By.ID, 'buyAmount').send_keys(str(random.randint(20, 50)))
        driver.find_element(By.ID, 'buyModel').send_keys(model)
        driver.find_element(By.ID, 'buyDescription').send_keys(descr)

        # Click the "Add Buy" button
        time.sleep(1)
        driver.find_element(By.XPATH, '//button[text()="Add Buy"]').click()

    # Wait for some time to let the JavaScript execute and update the table
    time.sleep(2)

    # Extract the updated HTML content after JavaScript execution
    html_content = driver.page_source

finally:
    # Close the browser
    time.sleep(5)
    driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table body by its ID
table_body = soup.find('tbody', {'id': 'buyTableBody'})

# Extract rows from the table body
rows = table_body.find_all('tr')

# Iterate over rows and extract data
for row in rows:
    cells = row.find_all('td')
    date = cells[0].text
    amount = cells[1].text
    name = cells[2].text
    descr = cells[3].text

    print(f"Date: {date}, Amount: {amount}, Name: {name}, Descr: {descr}")


# task starts here -> we have rows
target_models = []
for row in rows:
    cells = row.find_all('td')
    model = cells[2].text
    amount = cells[1].text
    print(f"Model: {model}")
    model_color = 'Unknown'
    if result := re.match(pattern='SM-S928BZ(.).', string=model):
        #color_letter = result.group('color')
        color_letter = result.group(1)
        # print(color_letter)
        model_color = color.get(color_letter, 'Unknown')

    descr = cells[3].text
    mem = '0'
    android_ver = 'Unknown'
    if result := re.search(pattern=r"Пам'ять:\s(\d+)\sГБ.*Android\s(\d+)", string=descr):
        mem = result.group(1)
        android_ver = result.group(2)
    current_info = {"model": model, "amount": amount, "color": model_color, "Memory": f'{mem} GB',
                    "Android": android_ver}
    target_models.append(current_info)

    with open('/absolute_path_to_dir/web_regexp/out.json', 'w') as out_fh:
        json.dump(target_models, out_fh, indent=4)

print(target_models)

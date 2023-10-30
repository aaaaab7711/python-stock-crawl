import os
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

file_path = 'companys.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

batch_size = 1095
wait_time = random.uniform(5, 10)  

for i in range(0, len(lines), batch_size):
    batch = lines[i:i + batch_size]

    for j in range(0, len(batch), 2):
        line1 = batch[j].strip()
        line2 = batch[j + 1].strip()

        download_folder = f'/Users/JinBin/Desktop/大學課程/大三上/機器學習/final_project/company_info/{line1}/Bias'
        os.makedirs(download_folder, exist_ok=True)

        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': download_folder}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(options=options)

        driver.get(f"https://goodinfo.tw/tw/ShowK_ChartFlow.asp?STOCK_ID={line2}")

        wait = WebDriverWait(driver, 10)
        download_button = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='匯出XLS']")))

        select = Select(wait.until(EC.presence_of_element_located((By.ID, "selK_ChartFlowPeriod"))))
        select.select_by_value("3650")

        wait.until(EC.staleness_of(download_button))

        download_button = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='匯出XLS']")))
        download_button.click()

        while not os.path.exists(os.path.join(download_folder, 'K_ChartFlow.xls')):
            time.sleep(1)

        driver.quit()

    time.sleep(wait_time)

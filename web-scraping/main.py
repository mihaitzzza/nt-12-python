import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utility.departments import Department

if __name__ == '__main__':
    shutil.rmtree('images/')
    os.mkdir('images/')

    chrome_executable = Service(executable_path='./chromedriver')

    driver = webdriver.Chrome(service=chrome_executable)
    driver.set_window_position(0, 0)
    driver.maximize_window()

    driver.get('https://www.emag.ro/all-departments')

    department_elements = driver.find_elements(By.XPATH, './/div[@class="page-section"]//div[@class="panel-body"]')
    for department_element in department_elements[:-1]:
        department = Department(department_element, driver=driver)
        department.extract_data()

        break

    driver.close()

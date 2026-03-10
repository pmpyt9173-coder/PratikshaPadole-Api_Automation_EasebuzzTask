from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_practice_page():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    # Select radio button
    driver.find_element(By.XPATH, "//input[@value='radio2']").click()

    # Select dropdown option
    dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
    dropdown.select_by_visible_text("Option2")

    # Enter text
    driver.find_element(By.ID, "name").send_keys("QA Tester")

    # Click alert button
    driver.find_element(By.ID, "alertbtn").click()

    time.sleep(2)

    driver.quit()
import time
from pytest import PytestWarning
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#pytest_plugins = ["docker_compose"]
delay = 3 # seconds
def test_setup():
    try:
        global driver 
        driver = webdriver.Edge(executable_path="../drivers/Linux/msedgedriver")
        driver.implicitly_wait(10)
        driver.maximize_window()
    except TimeoutException:
        print("Timeout")
def test_youtube():
    driver.get("https://www.youtube.com/")
    driver.find_element(By.XPATH, '//ytd-button-renderer[2]//a[1]//tp-yt-paper-button[1]//yt-formatted-string[1]').click()

    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
    except TimeoutException:
        print("Timed out waiting for page to load")

    time.sleep(2.5)
    print("Typing to search box...")
    driver.find_element(By.XPATH,"//input[@id='search']").send_keys("never gonna give you up")
    time.sleep(2.5)
    print("Press search button")
    driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]').click()

    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//body[1]/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-search[1]/div[1]/ytd-two-column-search-results-renderer[1]/div[1]/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[1]/div[1]/div[1]/div[3]/yt-formatted-string[1]/span[2]")))
    except TimeoutException:
        print("Timed out waiting for page to load")

    driver.find_element(By.XPATH, "//body[1]/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-search[1]/div[1]/ytd-two-column-search-results-renderer[1]/div[1]/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[1]/div[1]/div[1]/div[3]/yt-formatted-string[1]/span[2]").click()
    time.sleep(15.5)
def test_end():
    driver.close()
    driver.quit()
    print("Test on Firefox completed")

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from config.config import get_config


def setup_driver():
    config = get_config()
    options = Options()
    options.add_argument("--headless")
    firefox_binary_path = config['firefox_binary_path']
    #service = Service(config['gecko_driver_path'])
    options.set_preference("profile", str(config['firefox_profile_path']))
    options.binary_location = firefox_binary_path
    driver = webdriver.Firefox(options=options)
    return driver


def teardown_driver(driver):
    driver.quit()

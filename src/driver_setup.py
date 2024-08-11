from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from config.config import get_config


def setup_driver():
    config = get_config()
    options = Options()
    options.headless = False
    options.set_preference("profile", str(config['firefox_profile_path']))
    service = Service(config['gecko_driver_path'])
    driver = webdriver.Firefox(service=service, options=options)
    return driver


def teardown_driver(driver):
    driver.quit()

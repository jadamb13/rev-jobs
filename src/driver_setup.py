from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from config.config import get_config

config = get_config()


def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.set_preference("profile", str(config['firefox_profile_path']))
    options.binary_location = config['firefox_binary_path']
    driver = webdriver.Firefox(options=options)
    return driver


def teardown_driver(driver):
    driver.quit()

import configparser
from selenium.webdriver.common.by import By

import configparser
from selenium.webdriver.common.by import By

def getLocator(section, key):
    reader = configparser.ConfigParser()
    reader.read("/Users/priyanka/PycharmProjects/testAssignmentR/SeleniumTestA/testdata/locators.cfg")
    locator_value = reader.get(section, key)
    return (By.XPATH, locator_value)  # Ensure locators are returned as tuples



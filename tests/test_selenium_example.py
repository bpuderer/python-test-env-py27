from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.testbase import BaseTestCase


class SeleniumExample(BaseTestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_selenium_example(self):
        driver = self.driver
        driver.get("https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "John Cleese"))).click()
        WebDriverWait(driver, 5).until(EC.title_is("John Cleese - Wikipedia"))

        driver.get_screenshot_as_file('screenshots/jmc.png')

        ps = driver.page_source
        self.assertIn("John Marwood Cleese", ps)

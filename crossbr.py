# Two browsers test for webpage California Real Estate
import time
import unittest

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import HtmlTestRunner


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test" keyword
    def test_search(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")
        print("California Real Estate Url has ", requests.get("https://qasvus.wordpress.com/").status_code,
              " as status Code")
        driver.implicitly_wait(3)

        # Checking page title and print it
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page has", driver.title + " as Page title")

        # workflow
        driver.find_element_by_id("g2-name").clear()
        driver.find_element_by_id("g2-name").send_keys("Vika")
        driver.find_element_by_id("g2-email").clear()
        driver.find_element_by_id("g2-email").send_keys("abc@gmail.com")
        driver.find_element_by_id("contact-form-comment-g2-message").clear()
        driver.find_element_by_id("contact-form-comment-g2-message").send_keys("Hi guys!")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").send_keys('\n')

        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'go "
                                                                                       "back')]")))
            driver.find_element(By.XPATH, "//a[contains(.,'go back')]").send_keys('\n')
            print("Go back is visible")
        except TimeoutException:
            print("Go back is NOT visible!")

        driver.implicitly_wait(3)

        # Check visibility of images
        driver.execute_script('window.scrollTo(0, 1000)')
        try:
            wait = WebDriverWait(driver, 3)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/condominium-690086_1920.jpg?w=740']")))
            print("Image 1 is ready!")
            driver.get_screenshot_as_file('Screeshot1.png')
        except TimeoutException:
            print("I can't find 1st image!")

        driver.execute_script('window.scrollTo(0, 1500)')
        try:
            wait = WebDriverWait(driver, 3)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//img[@src='https://qasvus.files.wordpress.com/2019/09/pexels-photo-1063991.jpeg?w=740']")))
            print("Image 2 is ready!")
            driver.get_screenshot_as_file('Screeshot2.png')
        except TimeoutException:
            print("I can't find 2nd image!")

        driver.execute_script('window.scrollTo(0, 2000)')
        try:
            wait = WebDriverWait(driver, 3)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/living-room-2732939_1920.jpg?w=740']")))
            print("Image 3 is ready!")
            driver.get_screenshot_as_file('Screeshot3.png')
        except TimeoutException:
            print("I can't find 3rd image!")

        driver.execute_script('window.scrollTo(0, 2500)')
        try:
            wait = WebDriverWait(driver, 3)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/kitchen-stove-sink-kitchen-counter-3497491.jpeg?w=740']")))
            print("Image 4 is ready!")
            driver.get_screenshot_as_file('Screeshot4.png')
        except TimeoutException:
            print("I can't find 4th image!")

    def test_site_chrome_1120x550(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 550)
        driver_chrome.get("https://qasvus.wordpress.com/")
        print("California Real Estate Url has ", requests.get("https://qasvus.wordpress.com/").status_code,
              " as status Code")
        driver_chrome.implicitly_wait(3)

        # Checking page title and print it
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver_chrome.title)
        print("Page has", driver_chrome.title + " as Page title")

        # workflow
        driver_chrome.find_element_by_id("g2-name").clear()
        driver_chrome.find_element_by_id("g2-name").send_keys("Vika")
        driver_chrome.find_element_by_id("g2-email").clear()
        driver_chrome.find_element_by_id("g2-email").send_keys("abc@gmail.com")
        driver_chrome.find_element_by_id("contact-form-comment-g2-message").clear()
        driver_chrome.find_element_by_id("contact-form-comment-g2-message").send_keys("Hi guys!")
        time.sleep(1)
        driver_chrome.find_element(By.XPATH, "//button[@class='pushbutton-wide']").send_keys('\n')

        try:
            WebDriverWait(driver_chrome, 2).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'go "
                                                                                              "back')]")))
            driver_chrome.find_element(By.XPATH, "//a[contains(.,'go back')]").send_keys('\n')
            print("Go back is visible")
        except TimeoutException:
            print("Go back is NOT visible!")

        driver_chrome.implicitly_wait(3)

        # Check visibility of images

        driver_chrome.execute_script('window.scrollTo(0, 1000)')
        try:
            wait = WebDriverWait(driver_chrome, 3)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/condominium-690086_1920.jpg?w=740']")))
            print("Image 1 is ready!")
            driver_chrome.get_screenshot_as_file('Screeshot1.png')
        except TimeoutException:
            print("I can't find 1st image!")

        driver_chrome.execute_script('window.scrollTo(0, 1500)')
        try:
            wait = WebDriverWait(driver_chrome, 3)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//img[@src='https://qasvus.files.wordpress.com/2019/09/pexels-photo-1063991.jpeg?w=740']")))
            print("Image 2 is ready!")
            driver_chrome.get_screenshot_as_file('Screeshot2.png')
        except TimeoutException:
            print("I can't find 2nd image!")

        driver_chrome.execute_script('window.scrollTo(0, 2000)')
        try:
            wait = WebDriverWait(driver_chrome, 3)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/living-room-2732939_1920.jpg?w=740']")))
            print("Image 3 is ready!")
            driver_chrome.get_screenshot_as_file('Screeshot3.png')
        except TimeoutException:
            print("I can't find 3rd image!")

        driver_chrome.execute_script('window.scrollTo(0, 2500)')
        try:
            wait = WebDriverWait(driver_chrome, 3)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/kitchen-stove-sink-kitchen-counter-3497491.jpeg?w=740']")))
            print("Image 4 is ready!")
            driver_chrome.get_screenshot_as_file('Screeshot4.png')
        except TimeoutException:
            print("I can't find 4th image!")

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test" keyword
    def test_search(self):
        driver_firefox = self.driver
        driver_firefox.get("https://qasvus.wordpress.com/")
        print("California Real Estate Url has ", requests.get("https://qasvus.wordpress.com/").status_code,
              " as status Code")
        driver_firefox.implicitly_wait(5)

        # Check that an element textarea is present on the DOM of a page and visible.
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")))
        time.sleep(1)

        # Checking page title and print it
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver_firefox.title)
        print("Page has", driver_firefox.title + " as Page title")

        # workflow
        driver_firefox.find_element_by_id("g2-name").clear()
        driver_firefox.find_element_by_id("g2-name").send_keys("Vika")
        driver_firefox.find_element_by_id("g2-email").clear()
        driver_firefox.find_element_by_id("g2-email").send_keys("abc@gmail.com")
        driver_firefox.find_element_by_id("contact-form-comment-g2-message").clear()
        driver_firefox.find_element_by_id("contact-form-comment-g2-message").send_keys("Hi guys!")
        time.sleep(1)
        driver_firefox.find_element(By.XPATH, "//button[@class='pushbutton-wide']").send_keys('\n')

        try:
            WebDriverWait(driver_firefox, 3).until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'go back')]")))
            driver_firefox.find_element(By.XPATH, "//a[contains(.,'go back')]").send_keys('\n')
            print("Go back is visible")
        except TimeoutException:
            print("Go back is NOT visible!")

        driver_firefox.implicitly_wait(5)

        # Check visibility of images
        driver_firefox.execute_script('window.scrollTo(0, 1000)')
        try:
            wait = WebDriverWait(driver_firefox, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/condominium-690086_1920.jpg?w=740']")))
            print("Image 1 is ready!")
            driver_firefox.get_screenshot_as_file('Screeshot1.png')
        except TimeoutException:
            print("I can't find 1st image!")

        driver_firefox.execute_script('window.scrollTo(0, 1500)')
        try:
            wait = WebDriverWait(driver_firefox, 2)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//img[@src='https://qasvus.files.wordpress.com/2019/09/pexels-photo-1063991.jpeg?w=740']")))
            print("Image 2 is ready!")
            driver_firefox.get_screenshot_as_file('Screeshot2.png')
        except TimeoutException:
            print("I can't find 2nd image!")

        driver_firefox.execute_script('window.scrollTo(0, 2000)')
        try:
            wait = WebDriverWait(driver_firefox, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/living-room-2732939_1920.jpg?w=740']")))
            print("Image 3 is ready!")
            driver_firefox.get_screenshot_as_file('Screeshot3.png')
        except TimeoutException:
            print("I can't find 3rd image!")

        driver_firefox.execute_script('window.scrollTo(0, 2500)')
        try:
            wait = WebDriverWait(driver_firefox, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/kitchen-stove-sink-kitchen-counter-3497491.jpeg?w=740']")))
            print("Image 4 is ready!")
            driver_firefox.get_screenshot_as_file('Screeshot4.png')
        except TimeoutException:
            print("I can't find 4th image!")

    def test_site_firefox_1250x850(self):
        driver = self.driver
        driver.set_window_size(1250, 850)
        driver.get("https://qasvus.wordpress.com/")
        print("California Real Estate Url has ", requests.get("https://qasvus.wordpress.com/").status_code,
              " as status Code")
        driver.implicitly_wait(5)

        # Check that an element textarea is present on the DOM of a page and visible.
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")))
        time.sleep(1)

        # Checking page title and print it
        self.assertIn("California Real Estate – QA at Silicon Valley Real Estate", driver.title)
        print("Page has", driver.title + " as Page title")

        # workflow
        driver.find_element_by_id("g2-name").clear()
        driver.find_element_by_id("g2-name").send_keys("Vika")
        driver.find_element_by_id("g2-email").clear()
        driver.find_element_by_id("g2-email").send_keys("abc@gmail.com")
        driver.find_element_by_id("contact-form-comment-g2-message").clear()
        driver.find_element_by_id("contact-form-comment-g2-message").send_keys("Hi guys!")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").send_keys('\n')

        try:
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(.,'go back')]")))
            driver.find_element(By.XPATH, "//a[contains(.,'go back')]").send_keys('\n')
            print("Go back is visible")
        except TimeoutException:
            print("Go back is NOT visible!")
            driver.implicitly_wait(5)

        # Check visibility of images
        driver.execute_script('window.scrollTo(0, 1000)')
        try:
            wait = WebDriverWait(driver, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/condominium-690086_1920.jpg?w=740']")))
            print("Image 1 is ready!")
            driver.get_screenshot_as_file('Screeshot1.png')
        except TimeoutException:
            print("I can't find 1st image!")

            driver.execute_script('window.scrollTo(0, 1500)')
        try:
            wait = WebDriverWait(driver, 2)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//img[@src='https://qasvus.files.wordpress.com/2019/09/pexels-photo-1063991.jpeg?w=740']")))
            print("Image 2 is ready!")
            driver.get_screenshot_as_file('Screeshot2.png')
        except TimeoutException:
            print("I can't find 2nd image!")

            driver.execute_script('window.scrollTo(0, 2000)')
        try:
            wait = WebDriverWait(driver, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/living-room-2732939_1920.jpg?w=740']")))
            print("Image 3 is ready!")
            driver.get_screenshot_as_file('Screeshot3.png')
        except TimeoutException:
            print("I can't find 3rd image!")

            driver.execute_script('window.scrollTo(0, 2500)')
        try:
            wait = WebDriverWait(driver, 2)
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://qasvus.files.wordpress.com/2019/09/kitchen-stove-sink-kitchen-counter-3497491.jpeg?w=740']")))
            print("Image 4 is ready!")
            driver.get_screenshot_as_file('Screeshot4.png')
        except TimeoutException:
            print("I can't find 4th image!")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/vikov/PycharmProjects/HW10_Py/HtmlReports"))

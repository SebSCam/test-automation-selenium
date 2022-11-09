from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import unittest

class LumaTest(unittest.TestCase):

    count = 0

    @classmethod
    def setUpClass(cls):
        print("Init Tests!")
        cls.URL = "https://magento.softwaretestingboard.com/"
        cls.PATH = "/home/sebscam/Documentos/luma-webdriver-test/web-driver/chromedriver"
        options = Options()
        options.add_argument("start-maximized")
        cls.driver = webdriver.Chrome(
            service=Service(cls.PATH), options=options)
        cls.driver.get(cls.URL)

    @classmethod
    def tearDownClass(cls):
        print("Completed!")
        cls.driver.close()

    @unittest.skip("First time test - Create account")
    def test_createAccount(self):
        personalName = 'Jimmy'
        personalLastName = 'Fast'

        signInButton = self.driver.find_element(
            By.LINK_TEXT, 'Create an Account')
        signInButton.click()

        firstName = self.driver.find_element(By.NAME, 'firstname')
        firstName.send_keys(personalName)

        lastName = self.driver.find_element(By.NAME, 'lastname')
        lastName.send_keys(personalLastName)

        mailText = self.driver.find_element(By.NAME, 'email')
        mailText.send_keys('selenium_test000@example.com')

        passText = self.driver.find_element(By.NAME, 'password')
        passText.send_keys('@Password123')

        confirm = self.driver.find_element(By.NAME, 'password_confirmation')
        confirm.send_keys('@Password123')
        confirm.submit()

        time.sleep(3)

        notify = self.driver.find_element(By.CLASS_NAME, 'logged-in')

        self.assertEqual(
            notify.text, f'Welcome, {personalName} {personalLastName}!')

        index = self.driver.find_element(By.CLASS_NAME, 'logo')
        index.click()

    def test_cartAddWithOptions(self):
        time.sleep(4)
        element = self.driver.find_element(
            By.CSS_SELECTOR, '.swatch-opt-1812 #option-label-size-143-item-168')
        element.click()

        element = self.driver.find_element(
            By.CSS_SELECTOR, '#option-label-color-93-item-59')
        element.click()

        element = self.driver.find_element(
            By.CSS_SELECTOR, '.product-item:nth-child(2) .actions-primary .action')
        element.click()

        time.sleep(3)
        element = self.driver.find_element(By.CSS_SELECTOR, '.counter-number')

        self.assertEqual(element.text, '1')

    def test_cartAddWithoutOptions(self):
        time.sleep(4)
        element = self.driver.find_element(
            By.CSS_SELECTOR, '.product-item:nth-child(6) .product-image-photo')
        element.click()

        time.sleep(3)
        element = self.driver.find_element(By.ID, 'product-addtocart-button')
        element.click()

        time.sleep(3)
        element = self.driver.find_element(By.CSS_SELECTOR, '.counter-number')
        self.assertEqual(element.text, '2')

    def test_checkoutCart(self):
        element = self.driver.find_element(By.CLASS_NAME, 'showcart')
        element.click()
        time.sleep(3)

        element = self.driver.find_element(By.CLASS_NAME, 'checkout')
        element.click()
        time.sleep(3)

        if (self.driver.find_element(By.ID, 'customer-email')):
            element = self.driver.find_element(By.ID, 'customer-email')
            element.send_keys('test@mail.co')

        element = self.driver.find_element(By.NAME, 'firstname')
        element.send_keys('Carlos')

        element = self.driver.find_element(By.NAME, 'firstname')
        element.send_keys('Carlos')

        element = self.driver.find_element(By.NAME, 'lastname')
        element.send_keys('Vega')

        element = self.driver.find_element(By.NAME, 'company')
        element.send_keys('Industry')

        element = self.driver.find_element(By.NAME, 'street[0]')
        element.send_keys('Address')

        element = self.driver.find_element(By.NAME, 'city')
        element.send_keys('Castilla')

        element = self.driver.find_element(
            By.XPATH, "//select[@name='country_id']/option[text()='Spain']").click()

        element = self.driver.find_element(By.NAME, 'postcode')
        element.send_keys('150001')

        element = self.driver.find_element(
            By.XPATH, "//select[@name='region_id']/option[text()='Albacete']").click()

        element = self.driver.find_element(By.NAME, 'telephone')
        element.send_keys('32589846')

        element = self.driver.find_element(
            By.CSS_SELECTOR, 'tbody .col:nth-child(1)')
        element.click()
        element.submit()

        time.sleep(3)


if __name__ == '__main_':
    unittest.main()

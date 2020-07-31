from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import unittest

class test(unittest.TestCase):
    def login(self):
        driver_path = "/Users/weijhehuang/tools/webdriver/chromedriver"
        self.browser = webdriver.Chrome(driver_path)
        self.browser.maximize_window()
        self.browser.get("http://127.0.0.1:3000")
        self.browser.find_element_by_xpath("//*[@id='navbar-collapse']/ul[2]/li[2]/a").click()
        self.browser.find_element_by_name('email').send_keys("demo@keystonejs.com")
        self.browser.find_element_by_name('password').send_keys("demo")
        self.browser.find_element_by_class_name('css-2960tt').submit()
        time.sleep(1)

    def test_1_create_enquiry(self):
        self.login()
        global_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav/div/ul[2]/li[1]/a/span")
        global_btn.click()
        time.sleep(1)
        contact_page = self.browser.find_element_by_xpath("//*[@id='navbar-collapse']/ul[1]/li[4]/a")
        contact_page.click()
        time.sleep(1)
        self.browser.find_element_by_name('name.full').send_keys("王小明")
        time.sleep(1)
        self.browser.find_element_by_name('email').send_keys("demo@keystonejs.com")
        time.sleep(1)
        self.browser.find_element_by_name('phone').send_keys("0912345678")
        time.sleep(1)
        regarding = Select(self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div[4]/div/select"))
        regarding.select_by_index(1)
        time.sleep(1)
        self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div[5]/div/textarea").send_keys("Hi ...")
        time.sleep(1)
        submit_btn = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div[6]/div/button")
        submit_btn.submit()
        time.sleep(1)
        admin_ui_btn = self.browser.find_element_by_xpath("/html/body/div/div[1]/a")
        admin_ui_btn.click()
        time.sleep(1)
        name = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/a").text
        email = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[3]/a").text
        enquiry_type = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[4]/div").text

        self.assertEqual(name, '王小明')
        self.assertEqual(email, 'demo@keystonejs.com')
        self.assertEqual(enquiry_type, 'Just leaving a message')

    def test_2_delete_enquiry(self):
        self.login()
        enquiry_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav/div/ul[1]/li[4]/a")
        enquiry_page.click()
        time.sleep(1)
        delete_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[1]/button/span")
        delete_btn.click()
        time.sleep(1)
        confirm_btn = self.browser.find_element_by_xpath("/html/body/div[8]/div/div/div/div/div[2]/button[1]")
        confirm_btn.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div/h2").text

        self.assertEqual(result, 'No enquiries found...')


if __name__ == "__main__":
    unittest.main()
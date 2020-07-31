from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

    def test_1_create_first_post(self):
        self.login()
        post_page = self.browser.find_element_by_link_text('Posts')
        post_page.click()
        time.sleep(1)
        create_post_button = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div/button")
        create_post_button.click()
        time.sleep(1)
        self.browser.find_element_by_name('name').send_keys("first post")
        time.sleep(1)
        self.browser.find_element_by_name('name').send_keys(Keys.ENTER)
        time.sleep(1)
        drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-3--value']/div[1]")
        drop_down_list.click()
        time.sleep(1)
        selected_option = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/form/div[1]/div[1]/div/div[4]/div/div/div/div[2]")
        selected_option.click()
        time.sleep(1)
        save_btn = self.browser.find_element_by_class_name('css-2960tt')
        save_btn.click()
        time.sleep(1)
        back_to_post_page = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div/div[1]/div/div[1]/a')
        back_to_post_page.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath(
        "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a").text
        time.sleep(1)
        self.browser.close()
        self.assertEqual(result, 'first post')

    def test_2_create_second_post(self):
        self.login()
        time.sleep(1)
        self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div[2]/div/div[1]/div[2]/div[1]/span/a[2]").click()
        time.sleep(1)
        self.browser.find_element_by_name('name').send_keys("second post")
        time.sleep(1)
        create_btn = self.browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div/form/div[3]/button[1]')
        create_btn.click()
        time.sleep(1)
        drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-3--value']/div[1]")
        drop_down_list.click()
        time.sleep(1)
        selected_option = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/form/div[1]/div[1]/div/div[4]/div/div/div/div[2]")
        selected_option.click()
        time.sleep(1)
        save_btn = self.browser.find_element_by_class_name('css-2960tt')
        save_btn.click()
        time.sleep(1)
        back_to_post_page = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div/div[1]/div/div[1]/a')
        back_to_post_page.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[2]/td[2]/a").text
        time.sleep(1)
        self.browser.close()
        self.assertEqual(result, 'second post')

    def test_3_edit_first_post(self):
        self.login()
        time.sleep(1)
        self.browser.find_element_by_link_text('Posts').click()
        time.sleep(1)
        first_post = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/a")
        first_post.click()
        time.sleep(1)
        self.browser.find_element_by_name('name').send_keys('edit-')
        time.sleep(1)
        save_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/form/div[2]/div/div/button[1]")
        save_btn.click()
        time.sleep(1)
        back_to_post_page = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/div/main/div/div/div[1]/div/div[1]/a')
        back_to_post_page.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a").text
        time.sleep(1)
        self.browser.close()
        self.assertEqual(result, 'edit-first post')

    def test_4_search_posts(self):
        self.login()
        time.sleep(1)
        self.browser.find_element_by_link_text('Posts').click()
        time.sleep(1)
        searchBar = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/div[1]/div[1]/div/input")
        searchBar.send_keys("edit-first post")
        time.sleep(1)
        searchResult = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a").text
        self.browser.close()
        self.assertEqual(searchResult, 'edit-first post')

    def test_5_delete_all_post(self):
        self.login()
        time.sleep(1)
        self.browser.find_element_by_link_text('Posts').click()
        time.sleep(1)
        first_post = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/a")
        first_post.click()
        time.sleep(1)
        delete_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/form/div[2]/div/div/button[3]")
        delete_btn.click()
        yes_btn = self.browser.find_element_by_class_name('css-t4884')
        yes_btn.click()
        time.sleep(1)
        second_post = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/a")
        second_post.click()
        time.sleep(1)
        delete_btn = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/form/div[2]/div/div/button[3]")
        delete_btn.click()
        yes_btn = self.browser.find_element_by_class_name('css-t4884')
        yes_btn.click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav[1]/div/ul[1]/li[1]/a").click()
        time.sleep(1)
        result = self.browser.find_element_by_class_name('dashboard-group__list-count').text
        self.browser.close()
        self.assertEqual(result, '0 Items')

if __name__ == "__main__":
    unittest.main()
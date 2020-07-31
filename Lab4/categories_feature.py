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

    def test_1_create_first_category(self):
        self.login()
        create_category_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div[2]/div/div[1]/div[2]/div[3]/span/a[2]")
        create_category_btn.click()
        time.sleep(1)
        self.browser.find_element_by_name('name').send_keys('first category')
        time.sleep(1)
        create_btn = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/form/div[3]/button[1]')
        create_btn.submit()
        time.sleep(1)
        back_to_categories_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/div/div[1]/a")
        back_to_categories_page.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a").text

        self.assertEqual(result, 'first category')

        self.browser.close()


    def test_2_show_posts_of_the_specific_category_by_pressing_category_name_on_the_Blog_page(self):
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
        state_drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-2--value']/div[1]")
        state_drop_down_list.click()
        time.sleep(1)
        selected_publish = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/form/div[1]/div[1]/div/div[3]/div/div/div/div[2]")
        selected_publish.click()
        time.sleep(1)
        author_drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-3--value']/div[1]")
        author_drop_down_list.click()
        time.sleep(1)
        selected_option = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/form/div[1]/div[1]/div/div[4]/div/div/div/div[2]")
        selected_option.click()
        time.sleep(1)
        categories_drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-4--value']/div[1]")
        js = "var q=document.documentElement.scrollTop=100000"
        self.browser.execute_script(js)
        time.sleep(3)
        categories_drop_down_list.click()
        time.sleep(1)
        selected_first_category = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/form/div[1]/div[1]/div/div[9]/div/div/div/div[2]")
        selected_first_category.click()
        time.sleep(1)
        save_btn = self.browser.find_element_by_class_name('css-2960tt')
        save_btn.click()
        time.sleep(1)
        back_to_post_page = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/div/main/div/div/div[1]/div/div[1]/a')
        back_to_post_page.click()
        time.sleep(1)
        global_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav[1]/div/ul[2]/li[1]/a")
        global_btn.click()
        time.sleep(1)
        blog_page = self.browser.find_element_by_xpath("//*[@id='navbar-collapse']/ul[1]/li[2]/a")
        blog_page.click()
        time.sleep(1)
        first_category = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[2]/a")
        first_category.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/article/div[2]/h3/a").text

        self.assertEqual(result, 'first post')

        self.browser.close()

if __name__ == "__main__":
    unittest.main()
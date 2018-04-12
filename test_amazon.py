from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time, re
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Amazon(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox(executable_path=r'./geckodriver')
        cls.driver.implicitly_wait(30)
       # cls.base_url = "https://www.amazin.in/"
        cls.driver.get("https://www.amazon.in/")
        cls.driver.maximize_window()


    def test_amazon(self):

    
#a.find_element_by_id("searchDropdownBox").click()
#Select(a.find_element_by_id("searchDropdownBox")).select_by_visible_text("Books") 
        self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("data catalog")
        self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").submit()
        self.driver.implicitly_wait(5)                               
        print("done")
        
        first_book_title = "The Condensed Chemical Dictionary; A Reference Volume for All Requiring Quick Access to a Large Amount of Essential Data Regarding Chemicals, and ... Used in Manufacturing and Laboratory Work"

        title = self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/h2').text
        self.assertEqual(first_book_title,title)
        
        
        author = self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[2]/span[2]').text
        paperback = self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/div[2]/a/span').text
        hardcover = self.driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[2]/div[2]/div[1]/div[7]/a/span').text

        print("Title = ", title)
        print("Author = ", author)
        print("Paperback Price = " , paperback)
        print("Hard Cover Price = " , hardcover)
        
    @classmethod    
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()        

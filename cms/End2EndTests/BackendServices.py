from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class BackendServices(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_backend_services(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Groups").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Tokens").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Assignment submissions").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Assignments").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Course rosters").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Course sections").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Graded Assignments").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Lessons").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Lessons").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Syllabuses").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Teams").click()
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_link_text("Evolutions").click()
        driver.find_element_by_link_text("Home").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class AddLesson(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_lesson(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/cms/")
        driver.find_element_by_link_text("Lessons").click()
        driver.find_element_by_link_text("#1023982 CMS 101 : Intro to Course Management Systems").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("Add Lesson").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Unit test")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_week_no").clear()
        driver.find_element_by_id("id_week_no").send_keys("12")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_name("_save").click()
        driver.find_element_by_id("id_assignments-0-name").clear()
        driver.find_element_by_id("id_assignments-0-name").send_keys("Doug")
        driver.find_element_by_name("_save").click()
    
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

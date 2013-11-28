from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class AddCourseRoster(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_course_roster(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[6]").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
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

class AddCourse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_course(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[8]").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Project Managment")
        driver.find_element_by_id("id_full_name").clear()
        driver.find_element_by_id("id_full_name").send_keys("Project management, and leadership development.")
        driver.find_element_by_id("id_schedule_no").clear()
        driver.find_element_by_id("id_schedule_no").send_keys("105")
        driver.find_element_by_css_selector("img[alt=\"Calendar\"]").click()
        driver.find_element_by_link_text("24").click()
        driver.find_element_by_css_selector("#calendarlink1 > img[alt=\"Calendar\"]").click()
        driver.find_element_by_css_selector("#calendarbox1 > div > a.calendarnav-next").click()
        driver.find_element_by_css_selector("#calendarbox1 > div > a.calendarnav-next").click()
        driver.find_element_by_xpath("(//a[contains(text(),'3')])[5]").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_lessons-0-name").clear()
        driver.find_element_by_id("id_lessons-0-name").send_keys("Chris")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_lessons-0-name").clear()
        driver.find_element_by_id("id_lessons-0-name").send_keys("Lesson 1")
        driver.find_element_by_id("id_syllabus-0-name").clear()
        driver.find_element_by_id("id_syllabus-0-name").send_keys("Syllabus 1")
        driver.find_element_by_id("id_sections-0-section_no").clear()
        driver.find_element_by_id("id_sections-0-section_no").send_keys("105")
        driver.find_element_by_name("_save").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Project")
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

class AddCourse(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_course(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[8]").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Project Managment")
        driver.find_element_by_id("id_full_name").clear()
        driver.find_element_by_id("id_full_name").send_keys("Project management, and leadership development.")
        driver.find_element_by_id("id_schedule_no").clear()
        driver.find_element_by_id("id_schedule_no").send_keys("105")
        driver.find_element_by_css_selector("img[alt=\"Calendar\"]").click()
        driver.find_element_by_link_text("24").click()
        driver.find_element_by_css_selector("#calendarlink1 > img[alt=\"Calendar\"]").click()
        driver.find_element_by_css_selector("#calendarbox1 > div > a.calendarnav-next").click()
        driver.find_element_by_css_selector("#calendarbox1 > div > a.calendarnav-next").click()
        driver.find_element_by_xpath("(//a[contains(text(),'3')])[5]").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_lessons-0-name").clear()
        driver.find_element_by_id("id_lessons-0-name").send_keys("Chris")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_lessons-0-name").clear()
        driver.find_element_by_id("id_lessons-0-name").send_keys("Lesson 1")
        driver.find_element_by_id("id_syllabus-0-name").clear()
        driver.find_element_by_id("id_syllabus-0-name").send_keys("Syllabus 1")
        driver.find_element_by_id("id_sections-0-section_no").clear()
        driver.find_element_by_id("id_sections-0-section_no").send_keys("105")
        driver.find_element_by_name("_save").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Project")
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

class Syllabus(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_syllabus(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Syllabuses").click()
        driver.find_element_by_link_text("#1023982 CMS 101 : Intro to Course Management Systems").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("Add Syllabus").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Advanced Software")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_css_selector("#add_id_course > img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | id_course | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=id_course | ]]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("CMS 102")
        driver.find_element_by_id("id_full_name").clear()
        driver.find_element_by_id("id_full_name").send_keys("Advanced Software")
        driver.find_element_by_id("id_schedule_no").clear()
        driver.find_element_by_id("id_schedule_no").send_keys("102")
        driver.find_element_by_css_selector("img[alt=\"Calendar\"]").click()
        driver.find_element_by_link_text("23").click()
        driver.find_element_by_css_selector("#calendarlink1 > img[alt=\"Calendar\"]").click()
        driver.find_element_by_css_selector("#calendarbox1 > div > a.calendarnav-next").click()
        driver.find_element_by_css_selector("#calendarbox1 > div > a.calendarnav-next").click()
        driver.find_element_by_xpath("(//a[contains(text(),'3')])[5]").click()
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
class Courses(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_courses(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[8]").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Advanced Software Engineering")
        driver.find_element_by_id("id_full_name").clear()
        driver.find_element_by_id("id_full_name").send_keys("This is the Advanced Software Engineering.")
        driver.find_element_by_id("id_schedule_no").clear()
        driver.find_element_by_id("id_schedule_no").send_keys("105")
        driver.find_element_by_id("id_schedule_no").clear()
        driver.find_element_by_id("id_schedule_no").send_keys("110")
        driver.find_element_by_css_selector("img[alt=\"Calendar\"]").click()
        driver.find_element_by_link_text("25").click()
        driver.find_element_by_css_selector("#calendarlink1 > img[alt=\"Calendar\"]").click()
        driver.find_element_by_css_selector("#calendarbox1 > div > a.calendarnav-next").click()
        driver.find_element_by_xpath("(//a[contains(text(),'19')])[2]").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_lessons-0-name").clear()
        driver.find_element_by_id("id_lessons-0-name").send_keys("Lesson 1")
        driver.find_element_by_id("id_lessons-0-week_no").clear()
        driver.find_element_by_id("id_lessons-0-week_no").send_keys("1")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_syllabus-0-name").clear()
        driver.find_element_by_id("id_syllabus-0-name").send_keys("Syllabus 1")
        driver.find_element_by_id("id_sections-0-section_no").clear()
        driver.find_element_by_id("id_sections-0-section_no").send_keys("110")
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

class BackendServices(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
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

class CourseSection(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_course_section(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[7]").click()
        driver.find_element_by_id("id_section_no").clear()
        driver.find_element_by_id("id_section_no").send_keys("SWENG")
        driver.find_element_by_css_selector("img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | id_course | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=id_course | ]]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Software Testing")
        driver.find_element_by_id("id_full_name").clear()
        driver.find_element_by_id("id_full_name").send_keys("Software testing with unit tests")
        driver.find_element_by_id("id_schedule_no").clear()
        driver.find_element_by_id("id_schedule_no").send_keys("105")
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_css_selector("#calendarlink1 > img[alt=\"Calendar\"]").click()
        driver.find_element_by_css_selector("#calendarbox1 > div > a.calendarnav-next").click()
        driver.find_element_by_link_text("31").click()
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
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
class Coursesection(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_coursesection(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[7]").click()
        driver.find_element_by_id("id_section_no").clear()
        driver.find_element_by_id("id_section_no").send_keys("SWENG")
        driver.find_element_by_css_selector("img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | id_course | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=id_course | ]]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Software Testing")
        driver.find_element_by_id("id_full_name").clear()
        driver.find_element_by_id("id_full_name").send_keys("Software testing with unit tests")
        driver.find_element_by_id("id_schedule_no").clear()
        driver.find_element_by_id("id_schedule_no").send_keys("105")
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_css_selector("#calendarlink1 > img[alt=\"Calendar\"]").click()
        driver.find_element_by_css_selector("#calendarbox1 > div > a.calendarnav-next").click()
        driver.find_element_by_link_text("31").click()
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
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
class AddUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_user(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[2]").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin_01")
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("admin")
        driver.find_element_by_name("_save").click()
        self.assertFalse(self.is_alert_present())
        driver.find_element_by_id("id_groups_add_link").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_user_permissions_from | label=authtoken | token | Can add token]]
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_user_permissions_from | label=auth | user | Can delete user]]
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_user_permissions_from | label=authtoken | token | Can add token]]
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_user_permissions_from | label=auth | user | Can change user]]
        # ERROR: Caught exception [ERROR: Unsupported command [removeSelection | id=id_user_permissions_from | label=auth | user | Can delete user]]
        driver.find_element_by_id("id_user_permissions_add_link").click()
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

class GradeAssignment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_grade_assignment(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[9]").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Alsaidi")
        driver.find_element_by_css_selector("#add_id_submission > img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | id_submission | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=id_submission | ]]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Alsaidi")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_name("_save").click()
        driver.find_element_by_id("id_score").clear()
        driver.find_element_by_id("id_score").send_keys("100")
        driver.find_element_by_name("_save").click()
        driver.find_element_by_name("_save").click()
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

class AddAssignment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_assignment(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[5]").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Doug McCall")
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("This assignment was created by Doug!")
        driver.find_element_by_css_selector("img[alt=\"Calendar\"]").click()
        driver.find_element_by_link_text("24").click()
        driver.find_element_by_link_text("Now").click()
        driver.find_element_by_id("id_points").clear()
        driver.find_element_by_id("id_points").send_keys("100")
        driver.find_element_by_id("id_weight").clear()
        driver.find_element_by_id("id_weight").send_keys("100")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_name("_save").click()
        driver.find_element_by_id("id_weight").clear()
        driver.find_element_by_id("id_weight").send_keys("1")
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

class AddLesson(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
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
class Addlesson(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_addlesson(self):
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
class AddGradeAssignment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_grade_assignment(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[9]").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Assignment 1")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_score").clear()
        driver.find_element_by_id("id_score").send_keys("100")
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
class CourseRosters(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_course_rosters(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Course rosters").click()
        driver.find_element_by_xpath("(//a[contains(text(),'snc137')])[2]").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_css_selector("tr.row2 > th.nowrap > a").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_xpath("(//a[contains(text(),'dhm116')])[3]").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("Cms").click()
    
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

class Courserosters(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_courserosters(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Course rosters").click()
        driver.find_element_by_xpath("(//a[contains(text(),'snc137')])[2]").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_css_selector("tr.row2 > th.nowrap > a").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_xpath("(//a[contains(text(),'dhm116')])[3]").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("Cms").click()
    
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

class AddAdminUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_admin_user(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Add").click()
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Administrator")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_permissions_from | label=admin | log entry | Can add log entry]]
        driver.find_element_by_id("id_permissions_add_link").click()
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

class AddSyllabus(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_syllabus(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[11]").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Syllabus01")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
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

class AddCourseSection(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_course_section(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[6]").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
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

class AddCourseRoster(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_course_roster(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[6]").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
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

class AddTeam(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_team(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/cms/")
        driver.find_element_by_link_text("Teams").click()
        driver.find_element_by_link_text("Add team").click()
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_id("id_team_no").clear()
        driver.find_element_by_id("id_team_no").send_keys("5")
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

class LoginService(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_service(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/logout/")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Log out").click()
        driver.find_element_by_link_text("Log in again").click()
    
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
class Authentication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_authentication(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("124")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    
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

class AddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_group(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Groups").click()
        driver.find_element_by_link_text("Administrator").click()
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

class AddLesson(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_lesson(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Lessons").click()
        driver.find_element_by_link_text("#1023982 CMS 101 : Intro to Course Management Systems").click()
    
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

class AssignmentSubmission(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_assignment_submission(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Assignment submissions").click()
        driver.find_element_by_css_selector("th.nowrap > a").click()
    
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

class Token(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_token(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Tokens").click()
        driver.find_element_by_link_text("66f1b3a7ecc8824fc32c7f61d63df679218ad4c8").click()
    
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
class ChangeUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_change_user(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_link_text("aua230").click()
    
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

class AddTeam(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_team(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[12]").click()
    
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
class ChangePassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_change_password(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Change password").click()
    
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

class Team(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_team(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Teams").click()
    
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

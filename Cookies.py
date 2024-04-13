from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains


class LoginAutomation:

    def __init__(self, url="https://www.saucedemo.com/", username="standard_user", password="secret_sauce"):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def boot(self):
        """
        This method is used to start the webpage
        :return:
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(3)

    def quit(self):
        """
        This method is used to close the webpage
        :return:
        """
        self.driver.quit()

    def findelementbyID(self, value):
        """
        This method is used to find the element by its ID
        :return:
        """
        sleep(3)
        return self.driver.find_element(by=By.ID, value=value)

    def login(self):
        self.boot()
        cookies = self.driver.get_cookies()
        print("Bofere Login: ")
        for cookie in cookies:
            print(cookie)
        # this method is used to fill the username and password
        self.findelementbyID("user-name").send_keys(self.username)
        self.findelementbyID("password").send_keys(self.password)
        # this method is used to click on the login button
        self.findelementbyID("login-button").click()
        sleep(3)

        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            print("Login Successfully")
        else:
            print("Error")
        cookies = self.driver.get_cookies()
        print("After LOgin: ")
        for cookie in cookies:
            print(cookie)

    def findElementbyfullXPath(self, fulXpath):
        return self.driver.find_element(by=By.XPATH, value=fulXpath)

    def gotomenubar(self):
        # to find the path of the menubar
        Menubar = self.driver.find_element(by=By.ID, value="react-burger-menu-btn").click()
        sleep(3)

        Logout = self.driver.find_element(by=By.ID,value="logout_sidebar_link").click()
        sleep(3)
        self.quit()


obj = LoginAutomation()
obj.login()
obj.gotomenubar()


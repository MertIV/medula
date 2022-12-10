from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app import config

class Selenium():

    def __init__(self, remote=False):
        self.is_live = 0
        self.options = Options()
        if remote:
            self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=self.options)
        else:
            self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
            self.driver = webdriver.Chrome(options=self.options,executable_path=config['CHROMEDRIVER_PATH'])

    def setLive(self, flag):
        if isinstance(flag, int) and flag in [0, 1]:
            self.is_live = flag

    def isLive(self) -> bool:
        return self.is_live == 1 
    
    def get_web_driver_options(self):
        return self.driver.ChromeOptions()

    def set_ignore_certificate_error(self):
        self.options.add_argument('--ignore-certificate-errors')

    def set_browser_as_incognito(self):
        self.options.add_argument('--incognito')

    def set_automation_as_head_less(self):
        self.options.add_argument('--headless')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

CHROME_DRIVER_PATH = r"C:\Users\lebo1\PycharmProjects\Web_Dev\dev_software\chromedriver.exe"


class Cookie:
    def __init__(self, url):
        # self.score = ""
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)
        self.driver.get(url=url)
        self.select_language()
        self.cookie_btn = self.driver.find_element(by=By.ID, value="bigCookie")

    def cookie_click(self):
        """Click on the cookie."""
        self.cookie_btn.click()

    def check_cookies_available(self):
        """
        Check the amount of cookies you have
        :return: An integer number representing the number of cookies you have.
        """
        cookie_num_element = self.driver.find_element(by=By.ID, value="cookies")
        num = cookie_num_element.text.split()[0].replace(",", "")
        return int(num)

    def get_product_prices(self):
        """
        Get the prices of the multiple products
        :return: A List of the prices
        """
        prices = self.driver.find_elements(by=By.CSS_SELECTOR, value=".enabled span.price")
        prices_list = []

        for price in prices:
            prices_list.append(int(price.text.replace(",", "")))

        if len(prices_list) != 0:
            return prices_list

    def check_to_buy(self):
        current_cookies = self.check_cookies_available()
        prices_list = self.get_product_prices()

        if prices_list is not None:
            highest_price = max(prices_list)
            product_number = len(prices_list) - 1

            if current_cookies > highest_price:
                buy = self.driver.find_element(by=By.ID, value=f"product{product_number}")
                buy.click()

    # def cookies_per_second(self):
    #     """
    #     Retrieves the final score from the game.
    #     """
    #     # score_element = self.driver.find_element(by=By.ID, value="cookiesPerSecond")
    #     # print(type(score_element.text.split()[2]))
    #     # self.score = score_element.text.split()[2]
    #
    #     self.score = self.get_text(self.driver, (By.ID, "cookiesPerSecond"))

    # @staticmethod
    # def get_text(driver, locator):
    #     return WebDriverWait(driver, 30, ignored_exceptions=(StaleElementReferenceException,)).\
    #         until(presence_of_element_located(locator))

    def select_language(self):
        while True:
            try:
                language_select = self.driver.find_element(by=By.ID, value="langSelect-EN")
            except NoSuchElementException:
                continue
            else:
                language_select.click()
                break

    def close_window(self):
        self.driver.quit()

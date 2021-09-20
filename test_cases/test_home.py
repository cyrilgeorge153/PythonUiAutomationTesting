import pytest

from pages.home_page import Home_Page
from pages.login_page import Login_Page
from utilities.custom_logger import Generate_Log
from utilities.read_properties import Read_Config


class Test_Home:
    username = Read_Config.getUseremail()
    password = Read_Config.getPassword()
    logger = Generate_Log.generate_log()

    @pytest.mark.order(0)
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_verify_products_heading_after_home_page_loading(self, setup):
        self.logger.info("starting test case test_verify_products_heading_after_home_page_loading")
        self.driver = setup
        self.lp = Login_Page(self.driver)
        self.hp = Home_Page(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        assert self.hp.verify_products_heading_is_dislayed() == True
        self.logger.info("ending test case test_verify_products_heading_after_home_page_loading")

    @pytest.mark.order(5)
    @pytest.mark.regression
    def test_verify_your_cart_link_after_home_page_loading(self, setup):
        self.logger.info("starting test case test_verify_your_cart_link_after_home_page_loading")
        self.driver = setup
        self.lp = Login_Page(self.driver)
        self.hp = Home_Page(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        assert self.hp.verify_your_cart_link_is_dislayed() == True
        self.logger.info("ending test case test_verify_your_cart_link_after_home_page_loading")

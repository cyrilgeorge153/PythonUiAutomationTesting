import pytest

from pages.login_page import Login_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Generate_Log


class Test_Login:
    logger = Generate_Log.generate_log()

    @pytest.mark.order(1)
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_page_loading(self, setup):
        self.logger.info("starting test case test_login_page_loading")
        self.driver = setup
        assert "Swag Labs" in self.driver.title
        self.logger.info("ending test case test_login_page_loading")

    @pytest.mark.order(2)
    @pytest.mark.regression
    def test_swag_logo_is_displayed(self, setup):
        self.logger.info("starting test case test_swag_logo_is_displayed")
        self.driver = setup
        self.lp = Login_Page(self.driver)
        assert self.lp.verify_swag_labs_logo_is_dislayed() == True
        self.logger.info("ending test case test_swag_logo_is_displayed")

    @pytest.mark.order(3)
    @pytest.mark.regression
    def test_login_button_is_displayed(self, setup):
        self.logger.info("starting test case test_login_button_is_displayed")
        self.driver = setup
        self.lp = Login_Page(self.driver)
        assert self.lp.verify_login_button_is_dislayed() == True
        self.logger.info("ending test case test_login_button_is_displayed")

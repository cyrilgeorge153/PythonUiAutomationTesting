from pages.login_page import Login_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Generate_Log


class Test_Login:
    username = Read_Config.getUseremail()
    password = Read_Config.getPassword()
    logger = Generate_Log.generate_log()

    def test_login_page_loading(self, setup):
        self.logger.info("starting test case test_login_page_loading")
        self.driver = setup
        assert "Swag Labs" in self.driver.title
        self.logger.info("ending test case test_login_page_loading")

    def test_swag_logo_is_displayed(self, setup):
        self.logger.info("starting test case test_swag_logo_is_displayed")
        self.driver = setup
        self.lp = Login_Page(self.driver)
        assert self.lp.verify_swag_labs_logo_is_dislayed() == True
        self.logger.info("ending test case test_swag_logo_is_displayed")

    def test_login_button_is_displayed(self, setup):
        self.logger.info("starting test case test_login_button_is_displayed")
        self.driver = setup
        self.lp = Login_Page(self.driver)
        assert self.lp.verify_login_button_is_dislayed() == True
        self.logger.info("ending test case test_login_button_is_displayed")

    # def test_verify_valid_login(self, setup):
    #     self.logger.info("starting test case test_verify_valid_login")
    #     self.driver = setup
    #     self.lp = Login_Page(self.driver)
    #     self.lp.enter_username(self.username)
    #     self.lp.enter_password(self.password)
    #     self.lp.click_login()
    #     print(self.driver.title)
    #     assert "Swag Labs" in self.driver.title
    #     self.logger.info("ending test case test_verify_valid_login")
    # self.driver.close()

import allure


class TestJin:

    @allure.step('登录')
    def test_login(self):
        allure.attach('测试附件','测试名称')
        assert True
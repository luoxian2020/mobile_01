from Base.Base import Base1
import Page
import allure

class Login_Page(Base1):

    def __init__(self, driver):
        Base1.__init__(self, driver)

    @allure.step(title='点击我的')
    def click_btn(self):
        # 点击 我的
        self.click_ele(Page.my_btn_xpath)

    @allure.step(title='点击登录注册')
    def click_login_sign_btn(self):
        # 点击登录注册
        self.click_ele(Page.login_sing_btn_id)

    @allure.step(title='输入用户信息')
    def input_phone(self, username, password):
        # 输入手机号
        allure.attach('描述','输入手机号')
        self.send_ele(Page.login_name_id, username)
        # 输入密码
        allure.attach('描述','输入密码')
        self.send_ele(Page.login_pwd_id, password)
        # 点击登录按钮
        allure.attach('描述','点击登录按钮')
        self.click_ele(Page.login_btn_id)

    @allure.step(title='判断的我的订单存在状态')
    def if_my_order_status(self):
        # 判断 我的订单是否存在

        try:
            self.wait_ele(Page.my_order_btn)
            allure.attach('状态','存在')
            return True
        except Exception as e:
            allure.attach('状态','不存在')
            return False

    @allure.step(title='点击设置按钮')
    def click_setting_btn(self):
        # 点击设置按钮
        self.click_ele(Page.person_setting_btn_id)

    @allure.step(title='点击安全退出')
    def safe_logout(self):
        # 点击 安全退出
        self.click_ele(Page.logout_btn_id)

    @allure.step('点击关闭页面')
    def quit_login_page(self):
        #点击页面 关闭按钮
        try:
            self.click_ele(Page.login_close_page_id)
            allure.attach('状态','关闭成功')
        except Exception as e:
            allure.attach('状态','关闭失败')
            allure.attach('状态失败原因:','%s' % e)


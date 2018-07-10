import os
import sys
sys.path.append(os.getcwd())
import pytest

from Base.get_driver import get_driver
from Page.login_page import Login_Page
from Base.read_write import read_write_data


# 将数据导进来
def get_data():
    data_f = read_write_data('data.yaml')
    data = data_f.read_file().get('Login_data')
    # print(data)
    data_list = []
    for i in data:
        # print(i)
        for o in i.keys():
            data_list.append((o, i.get(o).get('phone'), i.get(o).get('passwd'), i.get(o).get('get_mess'),
                              i.get(o).get('expect_message'), i.get(o).get('tag')))
    return data_list


class Test_login:

    def setup_class(self):
        self.obj = Login_Page(get_driver())
        # 点击我的
        self.obj.click_btn()

    def teardown_class(self):
        self.obj.driver.quit()

    @pytest.mark.parametrize('test_login_num,username,passwd,get_mess,expect_message,tag', get_data())
    def test_login(self, test_login_num, username, passwd, get_mess, expect_message, tag):
        # 点击登录注册
        self.obj.click_login_sign_btn()
        self.obj.input_phone(username, passwd)

        # 分两种去情况 我的订单 和登录失败

        # 输入手机号  密码 点击登录
        # 输入正确的手机号和密码
        if tag:
            try:
                # 断言是否登录成功和是否有 我的订单内容
                login_toast = self.obj.get_toast(get_mess)
                login_status = self.obj.if_my_order_status()
                #点击设置
                self.obj.click_setting_btn()
                # 退出登录  点击安全退出
                self.obj.safe_logout()
                assert login_toast==expect_message and login_status

            except Exception as e:
                assert False
            finally:
                # 点击 登录页面的关闭按钮
                self.obj.quit_login_page()
        else:
            try:
                mess = self.obj.get_toast(get_mess)
                if mess:
                    assert mess == expect_message

                else:
                    assert False
            finally:
                self.obj.quit_login_page()

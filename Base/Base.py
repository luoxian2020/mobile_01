# 编辑定位方法
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base1:

    def __init__(self, driver):
        """
        初始化driver
        :param driver:
        """
        self.driver = driver

    def wait_ele(self, loc, timeout=30, poll=1.0):
        """
        显性等待 单元素定位
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def wait_eles(self, loc, timeout=30, poll=1.0):
        """
        多元素定位
        :param loc:
        :param driver:
        :param timeout:
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc):
        """
        点击某一个元素
        :param loc:
        :param driver:
        :return:
        """
        self.wait_ele(loc).click()

    def send_ele(self, loc, text):
        """
        输入内容
        :param loc:
        :param driver:
        :return:
        """
        send_e = self.wait_ele(loc)
        send_e.clear()
        send_e.send_keys(text)

    def get_toast(self, message):
        # 获取toast消息
        try:
            toast_mes = '//*[contains(@text,"{}")]'.format(message)
            to = self.wait_ele((By.XPATH, toast_mes))
            return to.text

        except Exception as e:
            return False






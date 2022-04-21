#!usr/bin/python
#-*- coding:utf-8 _*-
"""
@author:xiana
@file: ImagePage.py
@time: 2022/4/20  2:51 下午
"""


class ImagePage:

    def __init__(self, driver):
        self.driver = driver

    """
    搜索图片
    """
    def search(self, word):
        self.driver.find_element_by_css_selector("#kw").send_keys(word)
        self.driver.find_element_by_xpath('//span/input[@class="s_newBtn"]').click()
#!usr/bin/python
# -*- coding:utf-8 _*-
"""
@author:xiana
@file: BaseDriver.py
@time: 2022/4/20  2:36 下午
"""
from selenium import webdriver


class BaseDriver:

    def __init__(self, url, browser="Chrome"):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser == "Firefox":
            self.driver = webdriver.Firefox()
        elif browser == "Ie":
            self.driver = webdriver.Ie()
        elif browser == "Edge":
            self.driver = webdriver.Edge()
        elif browser == "Opera":
            self.driver = webdriver.Opera()
        elif browser == "PhantomJS":
            self.driver = webdriver.PhantomJS()
        self.driver.get(url)
        self.driver.maximize_window()

        # self.driver.find_element_by_css_selector()




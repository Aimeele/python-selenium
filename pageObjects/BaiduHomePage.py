#!usr/bin/python
#-*- coding:utf-8 _*-
"""
@author:xiana
@file: BaiduHomePage.py
@time: 2022/4/20  2:50 下午
"""
from common.BaseDriver import BaseDriver
from pageObjects.ImagePage import ImagePage


class BaiduHomePage:

    def __init__(self, driver):
        self.driver = driver

    """
    点击跳转百度首页的新闻
    """
    def click_news(self):
        currentWindowHandles = self.driver.window_handles
        self.driver\
            .find_element_by_xpath('//div[@id="s-top-left"]/a[@href="http://news.baidu.com/"]')\
            .click()
        windowHandles = self.driver.window_handles
        for handle in windowHandles:
            if handle not in currentWindowHandles:
                self.driver.switch_to_window(handle)
    """
    点击跳转百度首页的地图
    """
    def click_map(self):
        currentWindowHandles = self.driver.window_handles
        self.driver \
            .find_element_by_xpath('//div[@id="s-top-left"]/a[@href="http://map.baidu.com/"]') \
            .click()
        windowHandles = self.driver.window_handles
        for handle in windowHandles:
            if handle not in currentWindowHandles:
                self.driver.switch_to_window(handle)

    """
    点击跳转百度首页的视频
    """
    def click_video(self):
        currentWindowHandles = self.driver.window_handles
        self.driver \
            .find_element_by_xpath('//div[@id="s-top-left"]/a[@href="http://haokan.baidu.com/"]') \
            .click()
        windowHandles = self.driver.window_handles
        for handle in windowHandles:
            if handle not in currentWindowHandles:
                self.driver.switch_to_window(handle)

    """
    点击跳转百度首页的图片
    """
    def click_image(self):
        currentWindowHandles = self.driver.window_handles
        self.driver \
            .find_element_by_xpath('//div[@id="s-top-left"]/a[@href="http://image.baidu.com/"]') \
            .click()
        windowHandles = self.driver.window_handles
        for handle in windowHandles:
            if handle not in currentWindowHandles:
                self.driver.switch_to_window(handle)

    """
    点击跳转百度首页的磁盘
    """
    def click_disk(self):
        currentWindowHandles = self.driver.window_handles
        self.driver \
            .find_element_by_xpath('//div[@id="s-top-left"]/a[@href="http://pan.baidu.com/"]') \
            .click()
        windowHandles = self.driver.window_handles
        for handle in windowHandles:
            if handle not in currentWindowHandles:
                self.driver.switch_to_window(handle)



if __name__ == '__main__':
    baseDriver = BaseDriver("http://www.baidu.com")
    baiduHomePage = BaiduHomePage(baseDriver.driver)
    imagePage = ImagePage(baseDriver.driver)
    baiduHomePage.click_image()
    imagePage.search("hello")
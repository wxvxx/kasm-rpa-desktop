"""
Created on 2025/2/26 13:53
@File: main.py
---------
@summary: 
---------
@Author: luzihang
"""
from DrissionPage import Chromium

tab = Chromium().latest_tab
tab.get('https://DrissionPage.cn')

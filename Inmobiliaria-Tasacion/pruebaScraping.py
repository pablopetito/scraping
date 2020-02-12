# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 08:17:20 2020

@author: Pablo Sergio Petito
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
driver.get('https://duckduckgo.com/')
search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "q"))) 
search_box.send_keys("Selenium") 
search_box.submit()
elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='links']/div/div/div[2]")))
for ele in elements: 
     print(ele.text)
driver.quit()
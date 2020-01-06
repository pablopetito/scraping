# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:34:05 2019

@author: Pablo Sergio Petito
"""

from selenium import webdriver
import datetime 
import time

driver=webdriver.Chrome("chromedriver.exe")

horaInicio=datetime.datetime.now()
print("Inicio de la Extraccion: ", horaInicio)

driver.get("https://www.argenprop.com.ar")

time.sleep(2)

i=1
j=1

#titulos=driver.find_element_by_xpath("/html/body/section[3]/section/article[2]/div/div/div[{}]/h2/a/span".format(i))
#subtitulos=driver.find_element_by_xpath("/html/body/section[3]/section/article[2]/div/div/div[{}]/ul/li[{}]".format(i,j))


horaFinal=datetime.datetime.now()
print("Hora Final de la Extraccion: ", horaFinal)


tiempoFinal= horaFinal - horaInicio
print("Tiempo de la Extraccion: ", tiempoFinal)

driver.close()
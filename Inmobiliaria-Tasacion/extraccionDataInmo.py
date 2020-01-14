# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:34:05 2019

@author: Pablo Sergio Petito
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime 
import time

driver=webdriver.Chrome("chromedriver.exe")

def darHora():
    return datetime.datetime.now()    

def inicializaWeb(nombreWeb):
    driver.get(nombreWeb)
    print("Web Inicializada " + nombreWeb + " Ok")
     
horaInicio = darHora()
print("Inicio de la Extraccion: ", horaInicio)

inicializaWeb("https://www.argenprop.com.ar")

# --- Esperar un tiempo que se cargue la pagina ---
time.sleep(3)

# --- Inicializa variables a utilizar
i=1
j=1

element = driver.find_element_by_xpath("//*[@id='home-ubicacion']")
element1 = element.send_keys("Capital Federal")
time.sleep(3)
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ENTER)

time.sleep(3)
element = driver.find_element_by_xpath("//*[@id='suggestAlertPopup']/div/form/button[2]").click()

time.sleep(5)

#titulos=driver.find_element_by_xpath("/html/body/section[3]/section/article[2]/div/div/div[{}]/h2/a/span".format(i))
#subtitulos=driver.find_element_by_xpath("/html/body/section[3]/section/article[2]/div/div/div[{}]/ul/li[{}]".format(i,j))

horaFinal=darHora()
print("Hora Final de la Extraccion: ", horaFinal)

# --- Calculo tiempo transcurrido --- 
tiempoFinal= horaFinal - horaInicio
print("Tiempo trasncurrido de la Extraccion: ", tiempoFinal)

# --- Cierra navegador 
driver.close()
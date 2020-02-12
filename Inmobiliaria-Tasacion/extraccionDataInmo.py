# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:34:05 2019

@author: Pablo Sergio Petito
"""

#paquetes externos
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import datetime 
import time

#paquetes propios
   
#hora Inicial
hrsInicial=datetime.datetime.now()
print("Inicio de la Extraccion: ", hrsInicial)

#setEntornoWeb
useDriver="chromedriver.exe"
useWeb="https://www.argenprop.com.ar"

#iniciaWebDriver
driver=webdriver.Chrome(useDriver)
driver.get(useWeb)

# --- Esperar un tiempo que se cargue la pagina ---
time.sleep(3)

# --- Maximiza Navegador
driver.maximize_window()

# --- Inicializa variables a utilizar
i=1
j=1

element = driver.find_element_by_xpath("//*[@id='home-ubicacion']")
element1 = element.send_keys("Capital Federal")
time.sleep(3)
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ENTER)

# --- tiempo de espera
time.sleep(3)

# --- Presiona boton Cancelar de una ventana emergente
element = driver.find_element_by_xpath("//*[@id='suggestAlertPopup']/div/form/button[2]").click()

# --- tiempo de espera 
time.sleep(5)

# --- Borra todos los filtros de la busquedad
element = driver.find_element_by_xpath("/html/body/main/div[1]/sidebar/div[2]/div/button").click()

# --- Recolectar link PAISES 
#//*[@id="argentina"]
#//*[@id="locationFilter"]/ul[1]/li[1]
#/html/body/main/div[1]/sidebar/div[4]/div/div[1]/div/div[2]/ul[1]/li[1]/a

time.sleep(5)
pais = driver.find_element_by_xpath('//*[@id="argentina"]').text
paises = driver.find_element_by_xpath('//*[@id="locationFilter"]/ul[1]/li[1]/a').text
paises2 = driver.find_element_by_xpath('//*[@id="locationFilter"]/ul[1]').text
allPaises = driver.find_elements_by_xpath('//*[@id="locationFilter"]/ul[1]/li')
todosPaises = []
for paisesNom in allPaises:
    todosPaises.append(paisesNom.text)

time.sleep(5)
element = driver.find_element_by_xpath("/html/body/main/div[1]/sidebar/div[4]/div/div[1]/div/div[2]/ul[1]/li[1]/a").click()
print("pais")
print(pais)
print("paises")
print(paises)
print("paises2")
print(paises2)
print("paises de array")
for nombre in todosPaises:
    print("* " + nombre)

#titulos=driver.find_element_by_xpath("/html/body/section[3]/section/article[2]/div/div/div[{}]/h2/a/span".format(i))
#subtitulos=driver.find_element_by_xpath("/html/body/section[3]/section/article[2]/div/div/div[{}]/ul/li[{}]".format(i,j))

# --- Cierra navegador 
driver.close()

#hora Final

hrsFin=datetime.datetime.now()
print("Hora Final de la Extraccion: ", hrsFin)

print("Tiempo trasncurrido de la Extraccion: ", hrsFin - hrsInicial)